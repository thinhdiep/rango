from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from rango.models import Category, Page
from rango.forms import CategoryForm, UserForm, UserProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
	context_request = RequestContext(request)
	categories = Category.objects.order_by('-views')[:15]
	for category in categories:
		category.url = category.name.replace(' ','_')
	context_dictionary = {'bold_message' : 'this is bold message from server', 'context_details' : context_request, 'categories' : categories}
	return render(request,'rango/index.html',context_dictionary)
	# return render_to_response('rango/index.html', context_dictionary, context_request)

def about(request):
	return render(request,"rango/about.html")

def category(request, category_name_url):
	category_name  = category_name_url.replace('_',' ')
	context_dict = {'category_name':category_name}
	try:
		category = Category.objects.get(name = category_name)
		pages = Page.objects.filter(category = category)
		context_dict['category'] = category
		context_dict['pages'] = pages
	except Category.DoesNotExist:
		pass

	return render(request,'rango/category.html', context_dict)

def add_category(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		all_category = Category.objects.all()
		all_category_name = []
		for category in all_category:
			all_category_name.append(category.name)
		if form.is_valid():
			form.save(commit = True)
			return index(request)
		else: 
			print form.errors
	else:
		form = CategoryForm()
	return render(request,'rango/add_category.html', {'form' : form})

def register(request):
	registed = False
	if request.method == "POST":
		user_form = UserForm(request.POST)
		user_profile_form = UserProfileForm(request.POST)
		if user_form.is_valid() and user_profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			user_profile = user_profile_form.save(commit = False)
			user_profile.user = user
			if 'picture' in request.FILES:
				print "co picture"
				user_profile.picture = request.FILES['picture']
			user_profile.save()
			registed = True

	else:
		user_form = UserForm()
		user_profile_form = UserProfileForm()

	return render(request,'rango/register.html',{
		'user_form' : user_form,
		'user_profile_form' : user_profile_form,
		'registed' : registed,
		})

def user_login(request):
	if request.method == "POST":
		user_name = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=user_name,password=password)
		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect('/rango')
			else:
				return HttpResponse("Your account is disabled")
		else:
			return HttpResponse("invalid username or password")
		
	else:
		print "GET"
		return render(request,'rango/login.html',{})

@login_required
def log_out(request):
	logout(request)
	return HttpResponseRedirect('/rango')
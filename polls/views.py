from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
import logging
# Create your views here.
from .forms import HouseForm
from django.http import HttpResponse, HttpResponseRedirect
from .models import Poll,Country,Person
from django.db.models import Q,F,Count
from django.template import RequestContext, loader
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView

logger = logging.getLogger(__name__)

def index(request):
	latest_poll_list = Poll.objects.order_by('pub_date')[:2]
	output = ','.join([p.question for p in latest_poll_list])
	template = loader.get_template("polls/index.html")
	context = {
		'latest_poll_list' : latest_poll_list
	}
	return render(request,"polls/index.html",context)

def detail(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
	poll = get_object_or_404(Poll, pk=poll_id)
	return render(request, 'polls/results.html', {'poll': poll})

def vote(request, poll_id):
	p = get_object_or_404(Poll, pk=poll_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		 # Redisplay the poll voting form.
		return render(request, 'polls/detail.html', {
			'poll': p,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

def country(request):
	p = Country.objects.annotate(myperson = Count('person')).filter(myperson__gt = 1)
	return render(request,'polls/country.html', {'persons' : p})

def list_country(request):
	list_country = Country.objects.all()
	return render(request,'polls/list_country.html' ,{'list_country':list_country})

def country_detail(request,country_id):
	current_country = get_object_or_404(Country, pk=country_id)	
	return render(request,'polls/country_detail.html' ,{'current_country':current_country})	

def create_country(request):
	country_name = request.POST['country_name']
	country_language = request.POST['country_language']
	state_number = request.POST['country_state_number']
	mycountry = Country(name= country_name,language= country_language,state_number=state_number)
	mycountry.save()
	return render(request,'polls/country.html',{'message':country_name})

def update_country(request,country_id):
	current_country = get_object_or_404(Country, pk=country_id)
	current_country.name = request.POST['country_name']
	current_country.language = request.POST['country_language']
	current_country.state_number = request.POST['country_state_number']
	current_country.save()
	list_country = Country.objects.all()
	return render(request,'polls/list_country.html' ,{'list_country':list_country})

def delete_country(request,country_id):
	current_country = get_object_or_404(Country, pk=country_id)
	current_country.delete()
	list_country = Country.objects.all()
	return render(request,'polls/list_country.html' ,{'list_country':list_country})	

def search_country_by_name(request):
	search_text  = request.POST['search_param']
	if search_text.isdigit():
		state_number = int(search_text)
	else:
		state_number = 9999999999999
	list_country = Country.objects.filter(Q(name__contains = search_text) | Q(state_number = state_number) | Q(state_number__lt = F('city_number')))
	return render(request,'polls/list_country.html' ,{'list_country':list_country})


class PersonList(ListView):
	model = Person
	queryset = Person.objects.all()
	context_object_name = 'person_list'
	template_name = "polls/pl.html"

	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(PersonList, self).get_context_data(**kwargs)
		# Add in a QuerySet of all the books
		context['hello_world'] = "helloworld"
		return context


class PersonCreate(CreateView):
	model = Person
	fields = ["name", "age", "family", "country"]


class HouseView(FormView):
	template_name = 'polls/house.html'
	form_class = HouseForm
	success_url = '/list_country/'

	def form_valid(self, form):
		# This method is called when valid form data has been POSTed.
		# It should return an HttpResponse.
		form.create_house()
		return super(HouseView, self).form_valid(form)

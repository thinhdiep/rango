from django import forms
from rango.models import Category, Page, UserProfile
from django.contrib.auth.models import User
from rango import constant


class CategoryForm(forms.ModelForm):
	name = forms.CharField( help_text='Please enter category name',error_messages=constant.CATEGORY_ERRORS)
	views = forms.IntegerField(widget = forms.HiddenInput(), initial=0)


	class Meta:
		model = Category
		fields = ['name']

	def clean(self):
		#cleaned_data = self.cleaned_data
		cleaned_data = super(CategoryForm, self).clean()
		if Category.objects.filter(name=cleaned_data['name']).exists():
			print dir(forms)

			raise forms.ValidationError("You call that a title?!")
		else:
			return cleaned_data 

class UserForm(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput())


	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):


	class Meta:
		model = UserProfile
		fields = ['website','picture']

from django import forms

class HouseForm(forms.Form):
	
	address = forms.CharField()
	family = forms.IntegerField()

	def create_house(self):
		# send email using the self.cleaned_data dictionary
		pass
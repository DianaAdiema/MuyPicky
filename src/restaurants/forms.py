from django import forms

from .models import RestaurantLocation
from .validators import validate_category


class RestaurantCreateForm(forms.Form):
	name		 = forms.CharField()
	category 	 = forms.CharField(required=False)
	location 	 = forms.CharField(required=False)

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if name == "hello":
			raise forms.ValidationError("Not a valid name")
		return name





class RestaurantLocationCreateForm(forms.ModelForm):
	class Meta:
		model = RestaurantLocation
		fields = ['name', 'category', 'location',]

	def clean_name(self):
		name = self.cleaned_data.get('name')
		if name == "hello":
			raise forms.ValidationError("Not a valid name")
		return name




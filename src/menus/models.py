
from django.conf import settings #foreign keys
from django.db import models
from restaurants.models import RestaurantLocation
from django.core.urlresolvers import reverse

class Item(models.Model):
	#associations
	user 		= models.ForeignKey(settings.AUTH_USER_MODEL)
	restaurant 	= models.ForeignKey(RestaurantLocation)
	#menu items
	name		= models.CharField(max_length = 120)
	contents 	= models.TextField(help_text='separate each item by a comma')
	excludes 	= models.TextField(blank =True, null = True, help_text='separate each item by a comma')
	public 		= models.BooleanField(default = True)
	timestamp 	= models.DateField(auto_now_add = True)
	updated 	= models.DateField(auto_now = True)


	class Meta:
		ordering = ['-updated', '-timestamp']

	def get_absolute_url(self):  #get_absolute_url
		#return f'/restaurant/{self.slug}' #replace success URL, after submitting or use urlresolvers
		return reverse('items:detail', kwargs={'pk':self.pk})


	def get_contents(self):
		return self.contents.split(",")

	def get_excludes(self):
		return self.excludes.split(",")



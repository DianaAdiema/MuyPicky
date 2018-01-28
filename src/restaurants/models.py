from django.db import models
from django.db.models.signals import pre_save, post_save
from .util import unique_slug_generator
from .validators import validate_category
from django.conf import settings
from django.core.urlresolvers import reverse
# Create your models here.

User = settings.AUTH_USER_MODEL

class RestaurantLocation(models.Model):
	owner   	 = models.ForeignKey(User)
	name		 = models.CharField(max_length=120)
	category 	 = models.CharField(max_length=120, null=True, blank=True)#validators = [validate_category])
	location 	 = models.CharField(max_length=120, null=True, blank=True)
	timestamp 	 = models.DateField(auto_now_add=True)
	updated 	 = models.DateField(auto_now=True)
	slug		 = models.SlugField(null=True, blank=True)


	def __str__(self):
		return self.name


	def get_absolute_url(self):  #get_absolute_url
		#return f'/restaurant/{self.slug}' #replace success URL, after submitting or use urlresolvers
		return reverse('restaurant:detail', kwargs={'slug':self.slug})
	@property
	def title(self):
		return self.name



def rl_pre_save_receiver(sender, instance, *args, **kwargs):
	instance.category = instance.category.capitalize()  # make changes to field to capitalize and be displayed.
	
	if not instance.slug:
		instance.slug=unique_slug_generator (instance)


pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)

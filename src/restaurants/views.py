from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView
from .models import RestaurantLocation
from django.views.generic import ListView, DetailView, CreateView
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from django.contrib.auth.decorators import login_required


@login_required()
def restaurant_createview(request):
	form = RestaurantLocationCreateForm(request.POST, None)
	errors = None
	if form.is_valid():
		if request.user.is_authenticated():
			instance = form.save(commit = False)
			instance.owner = request.user
			instance.save()
			return HttpResponseRedirect('/restaurants/')  #link form entry to user and save.

		else:
			return HttpResponseRedirect('/login/')

	if form.errors:
		print(form.errors)


		
	template_name = 'restaurant/form.html'
	
	context= {"form":form, "errors":errors}
	return render(request,template_name, context)


def restaurant_listview(request):
	template_name = 'restaurant/restaurant_list.html'
	
	context= {"object_list":queryset}
	return render(request,template_name, context)




class RestaurantListview(ListView):

	template_name = 'restaurant/restaurantlocation_list.html'

	def get_queryset(self):
		queryset = RestaurantLocation.objects.all()
		slug = self.kwargs.get("slug")

		if slug:
			queryset = RestaurantLocation.objects.filter(Q(category__iexact = slug)|Q(category__icontains = slug))

		else:

			queryset = RestaurantLocation.objects.all()


		return queryset


class RestaurantDetailView(DetailView):

	template_name = 'restaurant/restaurantlocation_detail.html' 

	queryset = RestaurantLocation.objects.all()


class RestaurantCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantLocationCreateForm
	#login_url = '/login/'
	template_name = 'restaurant/form.html'
	#success_url = '/restaurants/'


	def form_valid(self, form): #class based foreign key linking and submitting form
		instance = form.save(commit = False)
		instance.owner = self.request.user
		return super(RestaurantCreateView,self).form_valid(form)

















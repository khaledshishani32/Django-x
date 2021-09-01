from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Car
from django.urls import reverse_lazy
# Create your views here.

class CarListView(ListView):
    template_name = 'car_list.html'
    context_object_name = "Cars"
    model  = Car


class CarDetailView(DetailView):
    template_name = 'car_detail.html'
    model = Car

class CarCreateView(CreateView):
    template_name= 'car_create.html'
    fields=['name' ,'purchaser' ,  'car_model' , 'description']
    model = Car
    success_url = reverse_lazy("car_list")

class CarUpdateView(UpdateView):
    template_name = 'car_update.html'
    fields=['name' ,'purchaser' , 'car_model' , 'description']
    model = Car
    success_url = reverse_lazy("car_list")


class CarDeleteView(DeleteView):
    template_name = "car_delete.html"
    model = Car
    success_url = reverse_lazy("car_list")

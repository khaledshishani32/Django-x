
from .views import *
from django.urls import path
from django.urls.resolvers import URLPattern

urlpatterns=[
    path('' ,CarListView.as_view() , name='crar_list'),
    path('<int:pk>/' ,CarDetailView.as_view() , name='car_detail'),
    path('create/' ,CarCreateView.as_view() , name='car_create'),
    path('<int:pk>/update/' ,CarUpdateView.as_view() , name='car_update'),
    path('<int:pk>/delete/' ,CarDeleteView.as_view() , name='car_delete'),

]

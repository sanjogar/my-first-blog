from django.urls import path
from . import views
#Here we're importing Django's function path and all of our views from the blog application. 

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('ciao', views.post_listciao, name='post_list_ciao'),
]

#name='post_list', is the name of the URL that will be used to identify the view. 
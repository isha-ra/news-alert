from django.urls import path
from .views import *
app_name="newsapp"
urlpatterns=[

path("",HomeView.as_view(),name="home"),
path("contact/",ContactView.as_view(),name="contact"),
path("about/",AboutView.as_view(),name="about"),

path("category/<int:pk>/detail",CategoryDetailView.as_view(),name="categorydetail"),
path("news/<int:pk>/newsdetail/",NewsDetailView.as_view(), name="newsdetail"),

path("subscriber/",SubscriberCreateView.as_view(),name="subscriber"),

path("message/",ContactCreateView.as_view(),name="message"),




]
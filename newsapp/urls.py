from django.urls import path
from .views import *
app_name="newsapp"
urlpatterns=[

path("signup/",SignupView.as_view(),name="signup"),
path("signin/",SigninView.as_view(),name="signin"),
path('signout/', SignoutView.as_view(), name='signout'),

path("username-checker/",UsernameCheckerView.as_view(),name="usernamechecker"),








path("",HomeView.as_view(),name="home"),
path("contact/",ContactView.as_view(),name="contact"),
path("about/",AboutView.as_view(),name="about"),
path("nepalinews/",NepaliNewsView.as_view(),name="nepalinews"),


path("category/<int:pk>/detail",CategoryDetailView.as_view(),name="categorydetail"),
path("news/<int:pk>/newsdetail/",NewsDetailView.as_view(), name="newsdetail"),

path("subscriber/",SubscriberCreateView.as_view(),name="subscriber"),

path("message/",ContactCreateView.as_view(),name="message"),


# for admin
path("adminhome/",AdminHomeView.as_view(),name="adminhome"),

# fornews category
path("admin/add/category",CategoryCreateView.as_view(),name="categorycreate"),
path("admin/<int:pk>/delete/category/",CategoryDeleteView.as_view(), name="categorydelete"),
path("admin/edit/category//<int:pk>",CategoryUpdateView.as_view(), name="categoryupdate"),








# for subscriber
path("subscriberlist/",AdminSubcriberListView.as_view(),name="subscriberlist"),
path('subscriber/<int:pk>/delete/',
          AdminSubscriberDeleteView.as_view(), name="subscriberdelete"),

# for mail
path("sendmaill/",AdminSendMailView.as_view(),name="sendmail"),
path("sendmaillist/",AdminSendMailListView.as_view(),name="sendmaillist"),

path("maillist/",AdminMailListView.as_view(),name="maillist"),
path("mail/<int:pk>/detail",AdminMailDetailView.as_view(),name="maildetail"),
path('mail/<int:pk>/delete/',
          AdminMailDeleteView.as_view(), name="maildelete"),


path("admin/add/news",NewsCreateView.as_view(),name="newscreate"),
path("news/<int:pk>/delete",AdminNewsDeleteView.as_view(),name="deletenews"),


path("organization/",OrganizationCreateView.as_view(),name="organizationcreate"),


]
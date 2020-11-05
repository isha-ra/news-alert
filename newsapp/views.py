from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from urllib.parse import urlparse, parse_qs
from datetime import datetime, date, timedelta
from django.urls import reverse_lazy
from django.views.generic import *
from .models import *
from .forms import *
import datetime
import requests
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# # Create your views here.








def error_404_view(request, exception):
    return render(request,'clienttemplate/404.html')


class BaseMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subsform"] = SubscriberForm
        context["currentdate"]=datetime.datetime.now()
        context["allcategory"] = Category.objects.order_by("id")
        context["allnews"]= News.objects.order_by('-id')
        context['organization']=Organization.objects.first()
        context['mainsponsored']=Sponsored.objects.first()
        context['allsponsored']=Sponsored.objects.all()

        response = requests.get(
            "https://ratopati.com/jsonapi/get_recent_posts/")
        results = eval(response.text)
        results = results['posts']
        context['allarticles'] = results




        return context


class HomeView(BaseMixin,TemplateView):
	template_name ="clienttemplate/home.html"
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)

		# context["allnews"]= News.objects.all()
		return context



class ContactView(BaseMixin,TemplateView):
	template_name ="clienttemplate/contact.html"


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["messageform"] = ContactForm
		return context


class NepaliNewsView(BaseMixin,TemplateView):
    template_name="clienttemplate/nepalinews.html"




class AboutView(BaseMixin,TemplateView):
	template_name ="clienttemplate/about.html"



class CategoryDetailView(BaseMixin, DetailView):
    template_name = "clienttemplate/categorydetail.html"
    model = Category
    context_object_name = "categoryobject"




class NewsDetailView(BaseMixin, DetailView):
    template_name = "clienttemplate/newsdetail.html"
    model = News
    context_object_name = "newsobject"



class SubscriberCreateView(BaseMixin, SuccessMessageMixin, CreateView):
    template_name = "clienttemplate/subscriber.html"
    form_class = SubscriberForm
    success_url = "/"

    def get_success_message(self, cleaned_data):

        return "Thankyou for subscribing us!!!"

    def form_valid(self, form):

        form_email = form.cleaned_data["email"]

        subject = 'Thanks for subscribing us'
        from_email = settings.EMAIL_HOST_USER
        contact_message = "Now ,You will be available to get notification for all latest news"
        send_mail(subject,
                  contact_message,
                  from_email,
                  [form_email],
                  fail_silently=False)

        return super().form_valid(form)



class ContactCreateView(BaseMixin, SuccessMessageMixin, CreateView):
    template_name = "clienttemplate/message.html"
    form_class = ContactForm
    success_url = reverse_lazy('newsapp:contact')

    def get_success_message(self, cleaned_data):

        return "Thankyou for the Message."

    def form_valid(self, form):

        form_email = form.cleaned_data["email"]

        subject = 'Thanks for the message'
        from_email = settings.EMAIL_HOST_USER
        contact_message = "Thankyou for contacting us, We will get back to you soon"
        send_mail(subject,
                  contact_message,
                  from_email,
                  [form_email],
                  fail_silently=False)
        return super().form_valid(form)




# for admin
class AdminBaseMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            pass
        else:
            return redirect("/signin/")

        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['organization']=Organization.objects.first()
        context['allmessage'] =Contact.objects.order_by('-id')
        context['countmail'] = Contact.objects.count()
        context['countsendmail'] = Mail.objects.count()

        context['countsub'] = Subscriber.objects.count()
        context['countcat'] = Category.objects.count()
        context['countnews'] = News.objects.count()


        context['allsub']=Subscriber.objects.order_by('-id')



        return context


# for admin
class AdminHomeView(AdminBaseMixin,TemplateView):
    template_name ="admintemplate/home.html"

# for admin category

class CategoryCreateView(AdminBaseMixin,SuccessMessageMixin,CreateView):
    template_name = "admintemplate/categorycreate.html"
    form_class = CategoryForm
    success_url = reverse_lazy('newsapp:categorycreate')
    
    def get_success_message(self, cleaned_data):

        return "New Category added"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat'] = CategoryForm
        category =Category.objects.order_by('-id').all()
        page = self.request.GET.get('page', 1)

        paginator = Paginator(category, 5)
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)
        context['allcategory'] = results
        return context
class CategoryDeleteView(AdminBaseMixin,SuccessMessageMixin,DeleteView):
    template_name="admintemplate/categorycreate.html"
    model=Category
    success_url=reverse_lazy('newsapp:categorycreate')
    def get_success_message(self, cleaned_data):

        return "category delete"

class CategoryUpdateView(AdminBaseMixin,UpdateView):
    template_name="admintemplate/categorycreate.html"
    form_class=CategoryForm
    model=Category
    success_url=reverse_lazy('newsapp:categorycreate')





class AdminNewsListView(AdminBaseMixin,TemplateView):
    template_name ="admintemplate/adminnewslist.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context["allnews"] = News.objects.order_by("id")       
        return context   

class AdminNewsCreateView(AdminBaseMixin, SuccessMessageMixin, CreateView):
    template_name = "admintemplate/adminaddnews.html"
    form_class = NewsForm
    success_url = "/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)



        context['newsform'] =NewsForm


        return context
class AdminNewsDeleteView(AdminBaseMixin,DeleteView):
    template_name="admintemplate/newsdelete.html"
    model=News
    success_url=reverse_lazy('newsapp:newscreate')




# for subscriber
class AdminSubcriberListView(AdminBaseMixin,TemplateView):
    template_name="admintemplate/adminsubcriberlist.html"


class AdminSubscriberDeleteView(AdminBaseMixin,DeleteView):
    template_name="admintemplate/adminsubcriberdelete.html"
    model = Subscriber
    success_url = reverse_lazy('newsapp:subscriberlist')

# for mail
class AdminSendMailView(AdminBaseMixin,CreateView):
    template_name ="admintemplate/adminsendmail.html"
    form_class = MailForm
    success_url = reverse_lazy('newsapp:sendmaillist')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)



        context['mail'] =MailForm


        return context
    def form_valid(self, form):

        form_email = form.cleaned_data["email"]

        subject = 'From News-alert'
        from_email = settings.EMAIL_HOST_USER
        message = form.cleaned_data["message"]
        send_mail(subject,
                  message,
                  from_email,
                  [form_email],
                  fail_silently=False)
        return super().form_valid(form)

class AdminSendMailListView(AdminBaseMixin,TemplateView):
    template_name="admintemplate/adminsendmaillist.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)



        context['allsendmail'] = Mail.objects.order_by('-id')


        return context

class AdminMailListView(AdminBaseMixin,TemplateView):
    template_name="admintemplate/adminmaillist.html"


class AdminMailDeleteView(AdminBaseMixin,DeleteView):
    template_name="admintemplate/adminmaildelete.html"
    model = Contact
    success_url = reverse_lazy('newsapp:sendmaillist')

class AdminMailDetailView(AdminBaseMixin,DetailView):
    template_name = "admintemplate/adminmaildetail.html"
    model = Contact
    context_object_name = "mailobject"






class NewsCreateView(AdminBaseMixin,CreateView):
    template_name = "admintemplate/newscreate.html"
    form_class = NewsForm
    success_url = reverse_lazy('newsapp:newscreate')
    def get_success_message(self, cleaned_data):

        return "Thankyou for subscribing us!!!"
    def form_valid(self, form):
        title = form.cleaned_data["title"]
        emails = Subscriber.objects.exclude(email='').values_list('email', flat=True)
        # reciever_list= ['mailme2isara@gmail.com', 'isharad014331@nec.edu.com','aanaishara@gmail.com']
        subject = 'From News-alert Check Our New News On'
        from_email = settings.EMAIL_HOST_USER
        datatuple = (
            (subject, title,from_email,emails)),
        send_mass_mail(datatuple)
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
   

        
        news =News.objects.order_by('-id').all()
        page = self.request.GET.get('page', 1)

        paginator = Paginator(news, 5)
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)
        context['allnews'] = results
        
      
        return context










class OrganizationCreateView(AdminBaseMixin,CreateView):
    template_name = "admintemplate/organizationcreate.html"
    form_class = OrganizationForm
    success_url = "/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['organizationcount']=Organization.objects.count()
        return context


class SignupView(AdminBaseMixin,FormView):
    template_name="admintemplate/register.html"
    form_class=SignupForm
    success_url="/"
    def form_valid(self,form):
        uname=form.cleaned_data["username"]
        email=form.cleaned_data["email"]
        pword=form.cleaned_data["password"]
        User.objects.create_user(uname,email,pword)

        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alluser']=User        
        return context



class SigninView(FormView):
    template_name = "admintemplate/adminlogin.html"
    form_class = SigninForm
    success_url = reverse_lazy('newsapp:adminhome')

    def form_valid(self, form):
        uname = form.cleaned_data["username"]
        pword = form.cleaned_data["password"]
        user = authenticate(username=uname, password=pword)
        if user is not None:
            login(self.request, user)
        else:
            return render(self.request, "admintemplate/adminlogin.html",
                          {"error": "Invalid Username or Password",
                           "form": form
                           })

        return super().form_valid(form)

class SignoutView(View):

    def get(self, request):
        logout(request)
        return redirect("/signin/")

class UsernameCheckerView(AdminBaseMixin,View):
    def get(self,request):
        un=request.GET["username"]
        
        if User.objects.filter(username=un).exists():
            message="yes"
        else:
            message="no"
        return JsonResponse({
            "output":message
            })

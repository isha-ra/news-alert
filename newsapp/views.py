from django.contrib.auth.models import User
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

# Create your views here.
def today(request):
    """Shows todays current time and date."""
    today = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    context = {'today': today}
    return render(request,'clienttemplate/base.html',{'today':today})

def showdate(request):
    datetime.datetime.now()
    """Shows todays current time and date."""
    # today = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    # context = {'today': today}
    return render(request,'clienttemplate/base.html')





def error_404_view(request, exception):
    return render(request,'clienttemplate/404.html')


class BaseMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subsform"] = SubscriberForm
        context["allcategory"] = Category.objects.order_by("id")
        context["allnews"]= News.objects.order_by('-id')
        context['organization']=Organization.objects.first()
        context['mainsponsored']=Sponsored.objects.first()

        return context


class HomeView(BaseMixin,TemplateView):
	template_name ="clienttemplate/home.html"
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['allsponsored']=Sponsored.objects.all()

		# context["allnews"]= News.objects.all()
		return context



class ContactView(BaseMixin,TemplateView):
	template_name ="clienttemplate/contact.html"
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["messageform"] = ContactForm
		return context

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
    success_url = "/"

    def get_success_message(self, cleaned_data):

        return "Thankyou for the Message!!!"

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
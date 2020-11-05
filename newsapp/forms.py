from django import forms
from .models import *
from django.contrib.auth.models import User





class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields=["title","image"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Category Title ...'
            }),
            'image':forms.ClearableFileInput(attrs={
            'class':'form-control'
            }),
            
        }



class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields=["title","category","image","content","content2","author"]
        widgets = {
         'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter newsTitle ...'
            }),
          'category': forms.Select(attrs={
                'class': 'form-control',
               
            }),
          'image':forms.ClearableFileInput(attrs={
            'class':'form-control'
            }),

        
            'content': forms.Textarea(attrs={
                'class': 'form-control',
             
            }),
            'content2': forms.Textarea(attrs={
                'class': 'form-control',
             
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Author name...'
            }),
            
            
        }


  
class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields="__all__"
        # fields=["name","logo","email","phone","address","slogan","about","mission_and_vision","website",]
        # widgets = {
        #  'name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter name ...'
        #     }),
       
        #   'logo':forms.ClearableFileInput(attrs={
        #     'class':'form-control'
        #     }),
        #   'email': forms.EmailInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter email...'
        #     }),
        #   'phone': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter phone ...'
        #     }),
         
        #   'address': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter address ...'
        #     }),
        #   'slogan': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter slogan ...'
        #     }),

        
        #     'about': forms.Textarea(attrs={
        #         'class': 'form-control',
             
        #     }),
        #     'mission_and_vision': forms.Textarea(attrs={
        #         'class': 'form-control',
             
        #     }),
  
        #     'website': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'placeholder': 'Enter Author website..'
        #     }),
         
            
        # }

  


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = "__all__"
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email...'
            }),
        }



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name...'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email...'
            }),
           
            'message': forms.Textarea(attrs={
                "class": 'form-control',
                'placeholder': 'Enter your message...'
            }),
        }


class MailForm(forms.ModelForm):
    class Meta:
        model=Mail
        fields="__all__"
        widgets = {
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address...'
            }),
            'image':forms.ClearableFileInput(attrs={
            'class':'form-control'
            }),
    
           
            'message': forms.Textarea(attrs={
                "class": 'form-control',
                'placeholder': 'Enter your message...'
            }),
        }




class SigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'ggg',
        'placeholder': 'Enter your username...'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'ggg',
        'placeholder': 'Enter your password...'
    }))


class SignupForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your username...'
    }))
    email=forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your username...'
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your username...'
    }))
    confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your username...'
    }))

    def clean_username(self):
        uname = self.cleaned_data["username"]
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError("username already exists")
        return uname
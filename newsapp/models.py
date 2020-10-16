from django.db import models
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
# Create your models here.
class Category(models.Model):
	title=models.CharField(max_length=200)
	image=models.ImageField(upload_to="category")
	
	def __str__(self):
		return self.title

		#manayto one relation in category and news
class News(models.Model):
	title=models.CharField(max_length=300)
	category=models.ForeignKey(Category,on_delete=models.CASCADE)
	image=models.ImageField(upload_to="news")
	content=models.TextField()
	content2=models.TextField(null=True,blank=True)
	author=models.CharField(max_length=100,null=True,blank=True)
	date=models.DateTimeField(auto_now_add=True)
	view_count=models.PositiveIntegerField(default=0)
	
	def __str__(self):
		return self.title


class Organization(TimeStamp):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="logo")
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    mobile = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200)
    slogan = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField()
    mission_and_vision = models.TextField()
    profile_image = models.ImageField(upload_to="profile")
    website = models.CharField(max_length=200)
    map_location = models.CharField(max_length=200)
    favicon = models.ImageField(upload_to="favicon", null=True, blank=True)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    youtube = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name



class Subscriber(TimeStamp):
    email = models.EmailField()

    def __str__(self):
        return self.email

class Contact(TimeStamp):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Sponsored(TimeStamp):
    
    title = models.CharField(max_length=200)
    image=models.ImageField(upload_to="Sponsored")
    message = models.TextField()
    end_date =models.DateTimeField()

    def __str__(self):
        return self.title


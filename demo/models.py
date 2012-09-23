from django.db import models
from django.contrib.auth.models import User
from django import forms
from goatnails.db.models import ImageWithThumbsField


class Character(models.Model):
    name = models.CharField(max_length=100)
    player = models.ForeignKey(User)
    server = models.CharField(max_length=100, blank=True)
    def __unicode__(self):
        return "{} ".format(self.name)

class Player(models.Model):
    user = models.OneToOneField(User)
    main = models.ForeignKey('Character', related_name='main_character')
    def __unicode__(self):
        return "{} ".format(self.user.username)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class NewUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    email = forms.CharField(max_length=100)
    character = forms.CharField(max_length=100)
    server = forms.CharField(max_length=100)

class AttendForm(forms.Form):
    char = forms.ModelChoiceField(Character.objects.all())

        
class Event(models.Model):
    name = models.CharField(max_length=100)
    begin = models.DateField()
    attendees = models.ManyToManyField('Character', blank=True,null=True)
    def __unicode__(self):
        return "{} {}".format( self.name, self.begin)
        
class EventForm(forms.Form):
    name = forms.CharField(max_length=100)
    begin_date = forms.CharField( ) 
    
class Rank(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    def __unicode__(self):
        return "{} ".format( self.name)

class Article(models.Model):
    title = models.CharField(max_length=100)
    text  = models.TextField()
    # img = models.ImageField(upload_to = "uploads")
    img = ImageWithThumbsField(upload_to = "uploads", 
                               sizes=((128,128), (200,200)))
    author = models.ForeignKey(User)
    approved = models.BooleanField(default=False)
    def __unicode__(self):
        return "{} by {}  {} ".format( self.title , self.author , self.approved )

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=100)
    text  = forms.CharField(widget=forms.Textarea)
    img = forms.ImageField()
    

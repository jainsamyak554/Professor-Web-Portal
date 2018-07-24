from django.contrib.auth.forms import User
from django import forms
from django.forms import ModelForm
from .models import Info,teaching, publication,project,recognition
from captcha.fields import CaptchaField

class detailform (ModelForm):
    class Meta:
        model=Info
        fields='__all__'

class userform(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput)
    captcha = CaptchaField()
    class Meta:
        model=User
        fields=['username', 'password']

class teachingform(forms.Form):
    course = forms.CharField(max_length=500)
    year = forms.CharField(max_length=10)
    odd = 'odd'
    even = 'even'
    SEMESTERS = (
        (odd, 'odd'),
        (even, 'even')
    )
    sem = forms.ChoiceField(
        choices=SEMESTERS
    )

class publicationform(forms.Form):
    publication_details = forms.CharField(max_length=1000)

class projectform (forms.Form):
    title = forms.CharField(max_length=100)
    pi = forms.CharField(max_length=10)
    agency = forms.CharField(max_length=10)
    startyear = forms.IntegerField()
    endyear = forms.IntegerField()

class recognitionform (forms.Form):
    recgonition_details = forms.CharField(max_length=1000)

from captcha.fields import CaptchaField


class CaptchaForm(forms.Form):
    captcha = CaptchaField()

class publicationform1(forms.Form):
    publication_details = forms.CharField(max_length=1000)
    captcha = CaptchaField()
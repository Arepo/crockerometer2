from django import forms
from .models import Vote, Metric

class VoteForm(forms.ModelForm):
  class Meta:
    model = Vote
    fields = ['email', 'rating']
    # When not using ModelForm, we had to do this:
    # name = forms.CharField(max_length = 255, label = 'Funky name')
    # number = forms.IntegerField(label = 'Important numbah')

class MetricForm(forms.ModelForm):
  class Meta:
    model = Metric
    fields = ['name']

class LoginForm(forms.Form):
  username = forms.CharField(label='User Name', max_length=64)
  password = forms.CharField(widget=forms.PasswordInput())

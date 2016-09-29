from django import forms
from .models import Woojit

class WoojitForm(forms.ModelForm):
  class Meta:
    model = Woojit
    fields = ['name', 'number']
  # name = forms.CharField(max_length = 255, label = 'Funky name')
  # number = forms.IntegerField(label = 'Important numbah')


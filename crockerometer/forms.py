from django import forms

class WoojitForm(forms.Form):
  name = forms.CharField(max_length = 255, label = 'Funky name')
  number = forms.IntegerField(label = 'Important numbah')

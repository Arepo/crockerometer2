from django.shortcuts import render

# Create your views here.
def index(request):
  value = 'look at mah value'
  context = { 'interpolation_test': value }

  return render(request, 'index.html', context)

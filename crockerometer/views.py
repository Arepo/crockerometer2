from django.shortcuts import render

# Create your views here.
def index(request):
  value = 'look at mah value'
  users = {'Bob the user', 'Quentin the other user'}
  context = { 'interpolation_test': value, 'users': users }

  return render(request, 'index.html', context)

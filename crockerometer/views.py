from django.shortcuts import render
from .models import User, Woojit
from .forms import WoojitForm
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
  users = User.objects.all()
  form = WoojitForm()
  context = { 'users': users, 'form': form }

  return render(request, 'index.html', context)

def detail(request, user_id):
  user = User.objects.get(id = user_id)

  return render(request, 'user.html', {'user': user})

def post_woojit(request):
  form = WoojitForm(request.POST)
  if form.is_valid():
    # woojit = Woojit(name   = form.cleaned_data['name'],
    #                 number = form.cleaned_data['number'])
    # woojit.save()
    form.save(commit = True)

  return HttpResponseRedirect('/')

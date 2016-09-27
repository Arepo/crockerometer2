from django.shortcuts import render
from models import User
# Create your views here.
def index(request):
  users = User.objects.all()
  context = { 'users': users }

  return render(request, 'index.html', context)

def detail(request, user_id):
  user = User.objects.get(id = user_id)

  return render(request, 'user.html', {'user': user})

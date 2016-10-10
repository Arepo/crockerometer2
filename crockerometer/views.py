from django.shortcuts import render
from .models import User, Rating
from .forms import MetricForm, VoteForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
  users = User.objects.all()
  form2 = MetricForm()
  form3 = VoteForm()
  context = { 'users': users, 'form2': form2, 'form3': form3 }

  return render(request, 'index.html', context)

def detail(request, user_id):
  user = User.objects.get(id = user_id)

  return render(request, 'user.html', {'user': user})

def login_view(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      user = form.cleaned_data['username']
      password = form.cleaned_data['password']
      user = authenticate(username = user, password = password)
      if user is not None:
        if user.is_active:
          login(request, user)
          return HttpResponseRedirect('/')
        else:
          print("The account has been disabled!")
      else:
        print("The username and password were incorrect.")

  else:
    form = LoginForm()
    return render(request, 'login.html', { 'form': form })

def profile(request, username):
  user = User.objects.get(username=username)
  ratings = Rating.objects.filter(user=user)
  return render(request, 'profile.html', { 'username': username, 'ratings': ratings })

def post_vote(request):
  form = VoteForm(request.POST)
  if form.is_valid():
    vote = form.save(commit = False)
    if request.user.email:
      vote.email = request.user.email
    vote.save()
    # vote.user = User.objects.first()
    # vote.metric = Metric.objects.first()
  return HttpResponseRedirect('/')

def post_metric(request):
  form = MetricForm(request.POST)
  if form.is_valid():
    form.save(commit = True)
  return HttpResponseRedirect('/')



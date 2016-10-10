from django.shortcuts import render
from .models import User, Rating
from .forms import MetricForm, VoteForm
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



# Crockerometer

## Crocker's Rules

> Declaring yourself to be operating by "Crocker's Rules" means that other people are allowed to optimize their messages for information, not for being nice to you.  Crocker's Rules means that you have accepted full responsibility for the operation of your own mind - if you're offended, it's your fault.  Anyone is allowed to call you a moron and claim to be doing you a favor.  (Which, in point of fact, they would be.  One of the big problems with this culture is that everyone's afraid to tell you you're wrong, or they think they have to dance around it.)  Two people using Crocker's Rules should be able to communicate all relevant information in the minimum amount of time, without paraphrasing or social formatting.  Obviously, don't declare yourself to be operating by Crocker's Rules unless you have that kind of mental discipline.

> Note that Crocker's Rules does not mean you can insult people; it means that other people don't have to worry about whether they are insulting you.  Crocker's Rules are a discipline, not a privilege.  Furthermore, taking advantage of Crocker's Rules does not imply reciprocity.  How could it?  Crocker's Rules are something you do for yourself, to maximize information received - not something you grit your teeth over and do as a favor.

> "Crocker's Rules" are named after Lee Daniel Crocker.

> http://sl4.org/crocker.html

Two issues confound actually implementing this philosophy: getting the word out, and persuading people that you really mean it. At the moment this is just a Django sandbox, but the goal is to develop it into a mini web service that lets people rate you on your crockerability (only if you sign up to invite them to), and provide a (hopefully dynamic) icon of your rating that you can use as an email signature.

## Setting up

Clone the project to your preferred environment, navigate to the root directory, set up the database with `python manage.py migrate` and run `python manage.py runserver`. 

I've been running the project with Python 3.5.1, so I recommend at least that version (and it probably won't work at all in Python 2.x)

The Crockerometer will be an instance of the 'Metric' model, so that thick-of-skin or recklessly optimistic users can create related (or possibly not) metrics on which others can rate them. You can create a Metric by first creating a super user (`python manage.py createsuperuser` from the command line), then navigating to localhost:8000/admin, logging in, and creating one from the admin panel


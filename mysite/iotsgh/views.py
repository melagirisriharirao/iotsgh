from django.shortcuts import render, render_to_response
from django.template import RequestContext

def index(requests):
	return render(requests, 'iotsgh/home.html')

def aboutproject(requests):
	return render(requests, 'iotsgh/aboutproject.html')

def teammembers(requests):
	return render(requests, 'iotsgh/teammembers.html')

def contactus(requests):
	return render(requests, 'iotsgh/contactus.html')

def thankyou(request):
  if request.method == "POST":
    screenname = request.POST.get("handle", None)  # handle is the name of the input in the question.
    # Here you can do anything with your screenname, like passing it to the function.
  return render_to_response('iotsgh/thankyou.html', {'name':[screenname]})
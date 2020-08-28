from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(request):
#    html = "<html><body>Hello world!</body></html>"
#    return HttpResponse(html)

def homepage(request):
    return render(request, 'habits/habits.html')
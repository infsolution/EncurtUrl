from django.shortcuts import render
from .models import *
def index(request):
    return render(request,'app/index.html')

def shorten(request):
	if request.GET.get('url'):
		short = Shortened(url=request.GET.get('url'))
		short.shorten()
		return render(request, 'app/index.html',{"url_short":short.url_shortened})

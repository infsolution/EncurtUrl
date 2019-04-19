from django.shortcuts import render, redirect
from .models import *
def index(request):
    return render(request,'app/index.html',{"title_page":"O melhor encurtador"})

def shorten(request):
	if request.GET.get('url'):
		short = Shortened(url=request.GET.get('url'))
		short.shorten()
		short.save()
		return render(request, 'app/index.html',{"url_short":short.url_shortened})
def shotened_report(request):
	shorteneds = Shortened.objects.all()
	return render(request, 'app/report.html',{"shorteneds":shorteneds})

def go_to_url(request, shortened):
	if request.method == 'GET':
		try:
			short = Shortened.objects.get(url_shortened=shortened)
		except Exception as e:
			return render(request,'app/urlnotfound.html', {"value":shortened,"error":e, "title_page":"Url Não encontrada"})
		return redirect(short.url)
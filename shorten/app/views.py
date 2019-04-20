from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from .models import *
from .forms import *
def index(request):
    return render(request,'app/index.html',{"title_page":"O melhor encurtador"})

def get_perfil_logado(request):
	return request.user.perfil

def shorten(request):
	if request.GET.get('url'):
		short = Shortened(url=request.GET.get('url'))
		short.shorten()
		short.save()
		return render(request, 'app/index.html',{"url_short":short.url_shortened})
	return render(request,'app/urlnotfound.html', {"value":"Nenhuma url foi informada", "title_page":"Url Não encontrada"})

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

def create_user(request):
	if request.method == 'POST':
		form = UserModelForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
			perfil = Perfil(user=user)
			perfil.save()
			return render(request, 'app/add.html', {'form':UserModelForm(), 'msg_confirm':'Parabéns você seu cadastro foi realizado.'})
		return render(request, 'app/add.html',{'form':UserModelForm(request.POST), 'msg_confirm':'Ocorreu um erro ao realizar o cadastro.'})
	form = UserModelForm()
	return render(request, 'app/add.html', {"form":form})

def do_login(request):
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password =  request.POST['password'])
		if user is not None:
			login(request,user)
			#return redirect('/app/'+str(user.id), user)
			return redirect('index')
		return render(request,'app/login.html' ,{"error_msg":"Usuário ou senha Invalidos"})	
	return render(request, 'app/login.html')

def do_logout(request):
	logout(request)
	return redirect('/login/')	
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.shortcuts import render, redirect
from .models import *
from .forms import *
def index(request):
	perfil_logado = get_perfil_logado(request)
	return render(request,'app/index.html',{"title_page":"O melhor encurtador","perfil_logado":perfil_logado})

def get_perfil_logado(request):
	try:
		perfil = Perfil.objects.get(user=request.user)
	except Exception as e:
		return None
	return perfil

def shorten(request):
	if request.GET.get('url'):
		short = Shortened(perfil=get_perfil_logado(request), url=request.GET.get('url'))
		short.shorten()
		if request.GET.getlist('private'):
			short.get_private_code()
		short.save()
		return render(request, 'app/index.html',{"url_short":short.url_shortened,"perfil_logado":get_perfil_logado(request)})
	return render(request,'app/urlnotfound.html', {"value":"Nenhuma url foi informada", 
	"title_page":"Url Não encontrada","perfil_logado":get_perfil_logado(request)})
@login_required
def shotened_report(request):
	perfil_logado = get_perfil_logado(request)
	shorteneds = Shortened.objects.filter(perfil=perfil_logado)
	return render(request, 'app/report.html',{"shorteneds":shorteneds,"perfil_logado":perfil_logado})

def go_to_url(request, shortened):
	if request.method == 'GET':
		try:
			short = Shortened.objects.get(url_shortened=shortened)
		except Exception as e:
			return render(request,'app/urlnotfound.html', {"value":shortened,"error":e, "title_page":"Url Não encontrada"})
		if short.private_code != None:
			return render(request, 'app/private_access.html',{"short":short})
		return redirect(short.url)

def create_user(request):
	if request.method == 'POST':
		form = UserModelForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
			perfil = Perfil(name=user.username, user=user)
			perfil.save()
			return render(request, 'app/add.html', {'form':UserModelForm(), 'msg_confirm':'Parabéns seu cadastro foi realizado.'})
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

def access_private(request):
	if request.method == 'POST':
		short = Shortened.objects.get(url_shortened=request.POST['url_shortened'])
		if request.POST.get('private_code') == short.private_code:
			return redirect(short.url)
		return render(request, 'app/private_access.html',{"short":short, "error_msg":"Código inválido"})
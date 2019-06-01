from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.core.paginator import Paginator, InvalidPage
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
		if request.GET.getlist('preview'):
			short.preview=True
			short.preview_message = request.GET.get('preview_msg')
		short.save()
		return render(request, 'app/showurl.html',{"url_short":short.url_shortened,"perfil_logado":get_perfil_logado(request),
			"title_page":"TShort: Sua url encurtada"})
	return render(request,'app/urlnotfound.html', {"value":"Nenhuma url foi informada", 
	"title_page":"Url Não encontrada","perfil_logado":get_perfil_logado(request)})
@login_required
def shotened_report(request):
	ITEMS_PER_PAGE = 5
	perfil_logado = get_perfil_logado(request)
	shorteneds = Shortened.objects.filter(perfil=perfil_logado)
	paginator = Paginator(shorteneds, ITEMS_PER_PAGE)
	page = request.GET.get('page',1)
	try:
		short_page = paginator.get_page(page)
	except InvalidPage:
		short_page = paginator.get_page(1)
	return render(request, 'app/report.html',{"shorteneds":short_page,"perfil_logado":perfil_logado})
@login_required
def detail(request, shortened_id):
	shorten = Shortened.objects.get(id=shortened_id)
	return render(request, 'app/report_detail.html', {'shorten':shorten, 'perfil_logado':get_perfil_logado(request)})

def go_to_url(request, shortened):
	if request.method == 'GET':
		try:
			short = Shortened.objects.get(url_shortened=shortened)
			get_click(request,short)
		except Exception as e:
			return render(request,'app/urlnotfound.html', {"value":shortened,"error":e, "title_page":"Url Não encontrada"})
		if short.private_code != None:
			return render(request, 'app/private_access.html',{"short":short})
		if short.preview:
			return render(request, 'app/preview.html',{'short':short, 'perfil_logado':get_perfil_logado(request)})
		return redirect(short.url)

def create_user(request):
	if request.method == 'POST':
		form = UserModelForm(request.POST)
		if form.is_valid():
			if request.POST['last-password'] == request.POST['password']:
				user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['last-password'])#validar se as senhas são igauis
				perfil = Perfil(name=user.username, user=user)
				perfil.save()
				return render(request, 'app/add.html', {'form':UserModelForm(), 'alert_type':'success', 'msg_confirm':'Parabéns seu cadastro foi realizado.'})
			else:
				return render(request, 'app/add.html', {'form':UserModelForm(),'alert_type':'danger' , 'msg_confirm':'As senhas não são iguais'})
		return render(request, 'app/add.html',{'form':UserModelForm(request.POST), 'alert_type':'danger','msg_confirm':'Ocorreu um erro ao realizar o cadastro.'})
	form = UserModelForm()
	return render(request, 'app/add.html', {"form":form})

'''def do_login(request):
	if request.method == 'POST':
		user = authenticate(username = request.POST['username'], password =  request.POST['password'])
		if user is not None:
			login(request,user)
			#return redirect('/app/'+str(user.id), user)
			return redirect('index')
		return render(request,'app/login.html' ,{"error_msg":"Usuário ou senha Invalidos"})	
	return render(request, 'app/login.html')'''

def do_logout(request):
	logout(request)
	return redirect('/login/')	

def access_private(request):
	if request.method == 'POST':
		short = Shortened.objects.get(url_shortened=request.POST['url_shortened'])
		if request.POST.get('private_code') == short.private_code:
			return redirect(short.url)
		return render(request, 'app/private_access.html',{"short":short, "error_msg":"Código inválido"})



@login_required
def get_contatos(request):
	return render(request, 'app/contatos.html', {"perfil_logado":get_perfil_logado(request)})

def request_access(request, codeurl):
	if request.method == 'POST':
		short = Shortened.objects.get(url_shortened=codeurl)
		if send_message(short):
			return render(request,'app/request_access.html',{"code":codeurl,"msg":"Sua solicitação foi enviada. Aquarde contato."})
	return render(request,'app/request_access.html',{"code":codeurl})


def send_message(short):
	return True

def get_click(request, shortened):
	shor = Click(shortened=shortened)
	print(shor.save())


def about(request):
	context = {}
	if get_perfil_logado(request):
		context = {"perfil_logado":get_perfil_logado(request)}
	return render(request, 'app/about.html',context)

def help(request):
	context = {}
	if get_perfil_logado(request):
		context = {"perfil_logado":get_perfil_logado(request)}
	return render(request, 'app/help.html',context)
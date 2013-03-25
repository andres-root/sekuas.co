from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.www.models import News
from apps.home.forms import ContactForm,LoginForm
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect

def index_view(request):
	news = News.objects.filter(visible=True) 
	news = News.objects.order_by('-id') 
	ctx = {'news':news}
	return render_to_response('home/index.html',ctx,context_instance=RequestContext(request))

def contact_view(request):
	info_enviado = False
	email = ""
	titulo = ""
	texto = ""
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			info_enviado = True
			email = form.cleaned_data['Email']
			titulo = form.cleaned_data['Titulo']
			texto = form.cleaned_data['Texto']
			
			to_admin = 'chost7531@hotmail.com'
			html_content = "Informacion recibida <br><br><br>***Mensaje***<br><br>%s"%(texto)
			msg = EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html')
			msg.send()
	else:
		form = ContactForm()
	ctx = {'form':form,'email':email,'titulo':titulo,'texto':texto,'info_enviado':info_enviado}
	return render_to_response('home/contact.html',ctx,context_instance=RequestContext(request))

def login_view(request):
	msg = "" 
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			form = LoginForm(request.POST)
			if form.is_valid():
				username = form.cleaned_data['username']				
				password = form.cleaned_data['password']
				user = authenticate(username=username,password=password)
				
				if user is not None and user.is_active:
					login(request,user)
					return HttpResponseRedirect('/')
				else:
					msg = "Usuario o Password incorrectos"
				
		form = LoginForm()
		ctx = {'form':form,'mensaje':msg}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request)) 
			
def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')	

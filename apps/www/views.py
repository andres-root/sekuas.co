# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from apps.www.forms import newPostForm,SUCreateForm
from apps.www.models import News,Song 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def add_post_view(request):
	if request.method == "POST":
		form = newPostForm(request.POST)
		info = "Inicializando"
		if form.is_valid():
			title = form.cleaned_data['title']	
			content = form.cleaned_data['content']	
			p = News()
			p.title = title
			p.content = content
			p.visible = True
			p.save()
			info = "Se guardo"
		else:
			info = "Datos incorrectos"
		form = newPostForm()
		ctx = {'form':form, 'info':info}
		return render_to_response('manager/wall.html',ctx,context_instance=RequestContext(request))
	else:
		form = newPostForm()
		ctx = {'form':form} 
		return render_to_response('manager/wall.html',ctx,context_instance=RequestContext(request))

def signup(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	if request.method == 'POST':
		form = SUCreateForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
		else:
			msg = "Error: Debe ingresar correctamente la información del formulario de registro."
		ctx = {'form':form,'message':msg}
		form = SUCreateForm()
		return render_to_response('manager/signup.html',ctx,context_instance=RequestContext(request))
	else:
		form = SUCreateForm()
		ctx = {'form':form}
		return render_to_response('manager/signup.html',ctx,context_instance=RequestContext(request))
	

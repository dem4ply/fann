from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
	template = loader.get_template('base/base.html')
	return HttpResponse( template.render() )

def user_sign_up(request):
	template = loader.get_template('user/sign_up.html')
	return HttpResponse( template.render() )

# Create your views here.

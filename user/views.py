from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core import serializers
from user.models import User
from django.db import IntegrityError
import json

def user_api( request ):
	if request.method == 'GET':
		return get_all_users( request )
	elif request.method == 'POST':
		return new_user( request )
	return HttpResponse( request.method )

def get_all_users( request ):
	result = serializers.serialize( "json", User.objects.all() )
	return HttpResponse( result )

def new_user( request ):
	user = User();
	post = list( request.POST );
	post = json.loads( post[0] )

	try:
		user = User( **post )
		user.username = user.email
		user.save()
	except IntegrityError:
		error = { 'msg': "Usuario ya registrado", }
		return HttpResponse( json.dumps( error ), status = 409 )
	
	return HttpResponse( json.dumps( { 'msg': "Registro correcto"} ), status = 201 )

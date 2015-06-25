from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from user.managers import User_manager

class User( AbstractBaseUser, PermissionsMixin ):
	alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$',
		message = "Only alphanumeric characters are allowed." )

	### redefine los campos del modelo user
	username =    models.CharField( unique=True, max_length=64,
							validators=[ alphanumeric ] )
	email =       models.EmailField( verbose_name='email address', unique=True,
							max_length=255 )
	first_name =  models.CharField( max_length=128, null=True, blank=True )
	last_name =   models.CharField( max_length=128, null=True, blank=True )
	date_joined = models.DateTimeField( auto_now_add=True )
	is_active =   models.BooleanField( default=True, null=False )
	is_staff =    models.BooleanField( default=False, null=False )

	objects = User_manager()
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = [ 'username' ]

	def get_full_name( self ):
		fullname = self.first_name + " " + self.last_name
		return fullname

	def get_short_name( self ):
		return self.username

	def __unicode__( self ):
		return str( self )

	def __str__( self ):
		return self.email

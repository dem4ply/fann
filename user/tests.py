from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import serializers
from user.models import User

class User_manager_test( TestCase ):

	def test_create_user( self ):
		user = User.objects.create_user( username='test_1', email='test_1@test_1.test_1' )
		self.assertEqual( user.email, "test_1@test_1.test_1", "El correo no es el registrado" )
		self.assertEqual( user.username, "test_1", "el username no es el correcto" )

	def test_get_all_user( self ):
		client = Client()

		#registro de un usuario
		user = User.objects.create_user( username='test_2', email='test_2@test_2.test_2' )

		response = client.get(	reverse( 'user_api' ) )
		self.assertEqual( response.status_code, 200, "codigo de error incorecto" )

# Create your tests here.

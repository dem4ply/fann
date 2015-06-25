from django.test import TestCase
from user.models import User
from user.managers import User_manager

class User_manager_test( TestCase ):
	def test_create_user( self ):
		user = User.objects.create_user( username='test_1', email='test_1@test_1.test_1' )
		self.assertEqual( user.email, "test_1@test_1.test_1" )
		self.assertEqual( user.username, "test_1" )

# Create your tests here.

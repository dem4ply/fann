from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class User_manager( BaseUserManager ):
	def create_user( self, username, email, password=None ):
		if not email:
			raise ValueError( 'Users must have an email address ' )
		if not username:
			raise ValueError( 'Users must have a username' )

		user = self.model( username=username, email=self.normalize_email( email ), )
		user.is_active = True
		user.set_password( password )
		user.save( using=self._db )
		return user

	def create_superuser( self, username, email, password ):
		user = self.create_user( username=username, email=email, password=password )
		user.is_staff = True
		user.is_superuser = True
		user.save( using=self._db )
		return user

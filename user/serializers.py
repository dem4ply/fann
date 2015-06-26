from .models import User
from rest_framework.serializers import ModelSerializer

class User_serializer( ModelSerializer ):
	class Meta:
		model = User
		fields = ( 'id', 'username', 'first_name', 'last_name', 'email' )

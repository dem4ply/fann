from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^user/sign_up$', views.user_sign_up, name='user_sign_up'),
]

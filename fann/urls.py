from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
   # Examples:
   # url(r'^$', 'fann.views.home', name='home'),
   # url(r'^blog/', include('blog.urls')),
	url(r'^', include( 'website.urls' ) ),
	url(r'^admin/', include( admin.site.urls ) ),
	url(r'^api_auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^api/v1/user', include( 'user.urls') ),
]

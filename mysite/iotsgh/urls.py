from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about-project/$', views.aboutproject, name='aboutproject'),
	url(r'^team-members/$', views.teammembers, name='teammembers'),
	url(r'^contact-us/$', views.contactus, name='contactus'),
	url(r'^thank-you/$', views.thankyou, name='thankyou'),	
]

from django.conf.urls import url

from ussdmenus import views

urlpatterns = [
	url(r'run$', views.run, name="run"),
	url(r'$', views.ussd_setup, name="ussd_setup"),
]
from django.conf.urls import urls

from ussdmenus import views

urlpatterns = [
	url(r'run', views.run, name="run"),
];
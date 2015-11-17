from django.shortcuts import render
from django.http import HttpResponse
import xmlrpclib

def run(request):
	params = {}
	params['msisdn'] = request.POST['msisdn']
	params['sessionId'] = request.POST['sessionId']
	params['imsi'] = request.POST['imsi']
	params['ussdRequestString'] = request.POST['ussdRequestString']
	proxy = xmlrpclib.ServerProxy("http://127.0.0.1:15290/")
	response = proxy.handleRequest(params)
	response_text = '<pre>'+response['ussdResponseString']+'</pre>'
	return HttpResponse(response_text)

def ussd_setup(request):
	return HttpResponse("")
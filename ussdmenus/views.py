from django.shortcuts import render
from django.http import HttpResponse
import xmlrpclib
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie, csrf_protect, requires_csrf_token

#@csrf_exempt
#@ensure_csrf_cookie
#@csrf_protect
#@requires_csrf_token
def run(request):
	params = {}
	# params['msisdn'] = request.GET['msisdn']
	# params['sessionId'] = request.GET['sessionId']
	# params['imsi'] = request.GET['imsi']
	# params['ussdRequestString'] = request.GET['ussdRequestString']
	#host_port = 
	params['msisdn'] = "2343243424"
	params['sessionId'] = "23432342"
	params['imsi'] = "23423423"
	params['ussdRequestString'] = "2"
	proxy = xmlrpclib.ServerProxy("http://127.0.0.1:15290")
	response = proxy.handleRequest(params)
	response_text = '<pre>'+response['ussdResponseString']+'</pre>'
	return HttpResponse(response_text)
	#r = request.POST
	#return HttpResponse(r)

def ussd_setup(request):
	return render(request, 'ussdmenus/index.html', {})
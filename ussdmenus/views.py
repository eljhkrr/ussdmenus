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
	# params['msisdn'] = request.POST['msisdn']
	# params['sessionId'] = request.POST['sessionId']
	# params['imsi'] = request.POST['imsi']
	# params['ussdRequestString'] = request.POST['query_string']
	# host_port = 
	params['msisdn'] = request.GET["msisdn"]
	params['sessionId'] = request.GET["session_id"]
	params['imsi'] = request.GET["imsi"]
	params['ussdRequestString'] = request.GET["query_string"]
	proxy = xmlrpclib.ServerProxy(str(request.GET["server"]))
	response = proxy.handleRequest(params)
	response_text = response['ussdResponseString']
	#response_text = dict(request.body)
	# response_text = type(request.body)
	# response_text = request.GET["query_string"]
	# response_text = request.GET["server"]
	#response_text = dict(request)
	#response_text = request.get("server", default="No Server")
	# if request.GET:
	# 	response_text = "Theres GET data"
	# else:
	# 	response_text = "No GET data"

	return HttpResponse(response_text)
	#r = request.POST
	#return HttpResponse(r)

def ussd_setup(request):
	return render(request, 'ussdmenus/index.html', {})
from django.shortcuts import render
from django.http import HttpResponse
import json
def index(request):
	dict = {}
#	info = 'Json success'
#	if request.method == 'POST':
#		req = simplejson.loads(request.raw_post_data)
#		username = request.GET.get('username') 
	#	info = request.raw_post_data
	dict["username"] = "username"
	dict["password"] = "password"
	m_json = json.dumps(dict)
	return HttpResponse(m_json)

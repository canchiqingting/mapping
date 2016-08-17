from django.shortcuts import render
from django.http import HttpResponse
import json
def index(request):
	dict = {}
#	info = 'Json success'
#	if request.method == 'POST':
#		req = simplejson.loads(request.raw_post_data)
#		username = request.GET.getet('username') 
	#	info = request.raw_post_data
	fruit = Person.object.create()
	fruit.username = "qfgao"
	fruit.password = "qw1990"
	fruit.save()
	dict["username"] = "qfgao"
	dict["password"] = fruit.object.filter(username = 'qfgao').password
	m_json = json.dumps(dict)
	return HttpResponse(m_json)

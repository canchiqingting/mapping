from django.shortcuts import render
from django.http import HttpResponse
from models import Person
import json
def index(request):
	dict = {}
	fruit = Person(username = "qfgao",password = "qw1990")
#	fruit.username = "qfgao"
#	fruit.password = "qw1990"
	fruit.save()
	dict["username"] = "qfgao"
	p = Person.objects.filter(username = "qfgao")
	dict["password"] = p.password
	m_json = json.dumps(dict)
	return HttpResponse(m_json)

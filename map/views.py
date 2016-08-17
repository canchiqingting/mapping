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
	dict["password"] = Person.objects.get(pk=1).password
	m_json = json.dumps(dict)
	return HttpResponse(m_json)

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
	return render(request, "html/wp-blog-header.php")

from django.shortcuts import render
from django.http import HttpResponse
from .models import SalesReport
# Create your views here.

def index(request):
	print('##########In the index of sales**************')
	
	sales = SalesReport.objects.all()
	
	return render(request, 'index.html', {'sales':sales});

def upload(request):
	return render(request, 'upload.html')
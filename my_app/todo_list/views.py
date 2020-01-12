from django.shortcuts import render
from .models import datas

def home(request):

	data = datas.objects.all()
	return render(request, 'home.html', {'data' : data})
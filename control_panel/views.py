from django.shortcuts import render
from control_panel.models import Machine
from django.utils import timezone

# Create your views here.
def dashboard(request):
	context = {'m': Machine.objects.get(id=1)}
	# context = {'status': render(request, 'control_panel/status.html', ), 'controls': render(request, 'control_panel/new_sample.html')}
	return render(request, 'control_panel/dashboard.html', context)

# def new_study(request):
# 	return render(request, 'control_panel/dashboard.html', context)

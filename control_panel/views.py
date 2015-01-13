from django.shortcuts import render
from control_panel.models import Machine

# Create your views here.
def dashboard(request, machine_id=1):
	context = {'m': Machine.objects.get(id=machine_id)}
	return render(request, 'control_panel/new_sample.html', context)
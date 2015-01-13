from django.contrib import admin
from control_panel.models import Machine

# Register your models here.
class MachineAdmin(admin.ModelAdmin):
	fields = ['status', 'current_sample']

admin.site.register(Machine)
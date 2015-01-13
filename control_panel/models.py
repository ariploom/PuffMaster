from django.db import models

class Machine(models.Model):
	name = models.CharField(max_length=50)
	current_sample = models.IntegerField()
	status = models.IntegerField()

	def __str__(self):
		return self.name

from django.db import models

class Machine(models.Model):
	name = models.CharField(max_length=50)
	current_sample = models.IntegerField()
	status = models.IntegerField()
	# time_remaining = models.IntegerField()
	# puffa_remaining = models.IntegerField()

	def __str__(self):
		return self.name

# class Study(models.Model):
# 	date = models.DateTimeField('date')
# 	npuffs = models.IntegerField()
# 	volume = models.IntegerField()
# 	duration = models.IntegerField()
# 	interval = models.IntegerField()
from django.db import models
from model_utils.models import TimeStampedModel

class Todo(TimeStampedModel):
	title = models.CharField(max_length=1000)
	# notes = models.CharField(max_length=5000)

	due = models.DateTimeField(auto_now=True)
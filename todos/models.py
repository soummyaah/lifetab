from django.db import models
from model_utils.models import TimeStampedModel
from datetime import datetime

class Todo(TimeStampedModel):
	title = models.CharField(max_length=1000)
	# notes = models.CharField(max_length=5000)

	due = models.DateField(default=datetime.now)
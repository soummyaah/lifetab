from django.db import models
from model_utils.models import TimeStampedModel

class Entry(TimeStampedModel):
	FEELING_CHOICES = (
		('HAPP', "happy"),
		('SADD', "sad"),
		('NOST', "nostalgic"),
		('CURI', "curious"),
		('WOND', "wonderful"),
	)

	is_protected = models.BooleanField(default=False)
	title = models.CharField(max_length=2000)
	content = models.TextField(max_length=100000)
	
	feeling = models.CharField(max_length=4,
								choices=FEELING_CHOICES,
								default='HAPP')
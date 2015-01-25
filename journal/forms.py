from django import forms
from models import Entry

class AddEntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['feeling', 'title', 'content', 'is_protected',]
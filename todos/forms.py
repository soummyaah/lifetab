from django import forms
from models import Todo

class AddTodoForm(forms.Form):
	title = forms.CharField()
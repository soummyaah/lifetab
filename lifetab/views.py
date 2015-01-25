from django.shortcuts import render_to_response
from django.template.context import RequestContext

from todos.forms import AddTodoForm
from journal.forms import AddEntryForm

def home(request):

	todo_form = AddTodoForm()
	journal_form = AddEntryForm()

	context = RequestContext(request, {'request': request, 'user': request.user, 'todo_form': todo_form, 'journal_form': journal_form})

	return render_to_response('lifetab/home.html',
                             context_instance=context)
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View, ListView, DetailView
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse, reverse_lazy
from models import Todo
from forms import AddTodoForm
import json

class AjaxableResponseMixin(object):

	"""
	Mixin to add AJAX support to a form.
	Must be used with an object-based FormView (e.g. CreateView)
	"""
	ajaxerror = {
		'error': 'Not fetched from ajax or using post',
	}
	def form_invalid(self, form):
		response = super(AjaxableResponseMixin, self).form_invalid(form)
		if self.request.is_ajax() and self.request.method == 'POST':
			return JsonResponse(form.errors, status=400)
		else:
			return JsonResponse(ajaxerror)

	def form_valid(self, form):
		response = super(AjaxableResponseMixin, self).form_valid(form)
		if self.request.is_ajax() and self.request.method == 'POST':
			data = build_return_data()
			return JsonResponse(response)
		else:
			return JsonResponse(ajaxerror)

	def build_return_data(self):
		pass

class TodoCreate(View):
	def post(self, request):
		if request.is_ajax():
			form = AddTodoForm(request.POST)
			if form.is_valid():
				# print request.POST['title']
				# from datetime import datetime
				# td = Todo.objects.create(title=request.POST['title'])
				td = form.save()
				# td.save()
				response_data = {'status': 'success',
									'data':	{
											'id': td.id,
											'title': td.title,
											'due': td.due,
											},
								}
			else:
				response_data = {'status': 'error', 'errors': form.errors}
			return JsonResponse(response_data)
		else:
			data = {
				'errors': 'AJAX not used',
			}
			return JsonResponse(data)

class TodoUpdate(View):
	def post(self, request, todo_id):
		try:
			todo = Todo.objects.get(pk=todo_id)
		except Todo.DoesNotExist:
			return JsonResponse({'status': 'error', 'errors': 'Todo does not exist'})


		if request.is_ajax():
			form = AddTodoForm(request.POST, instance=todo)
			if form.is_valid():
				from datetime import datetime
				id = form.cleaned_data['id']
				todo = Todo.objects.get(pk=id)
				todo.title = form.cleaned_data['title']
				todo.save()
				response_data = {'status': 'success',
									'data':{'id': todo.pk,
											'title': todo.title,
											}
								}
			else:
				response_data = {'status': 'error', 'errors': form.errors}
			return JsonResponse(form.errors)
		else:
			data = {
				'errors': 'AJAX not used',
			}
			return HttpResponse(JsonResponse(data))

class TodoListToday(View):

	def get(self, request):
		if request.is_ajax():
			import datetime
			today = datetime.date.today() + datetime.timedelta(days=1)
			todo_objs = Todo.objects.filter(due__lte=today).order_by('-modified')
			response_data = {'status': 'success'}
			todos = []
			for todo_obj in todo_objs:
				todo_data = {'title': todo_obj.title, 'id': todo_obj.pk}
				todos.append(todo_data)
			response_data['data'] = todos
			return JsonResponse(response_data)
		else:
			data = {
				'errors': 'AJAX not used',
			}
			return HttpResponse(JsonResponse(data))

class TodoListFuture(View):

	def get(self, request):
		if request.is_ajax():
			import datetime
			today = datetime.date.today() + datetime.timedelta(days=1)
			todo_objs = Todo.objects.filter(due__gt=today).order_by('-modified')
			response_data = {'status': 'success'}
			todos = []
			for todo_obj in todo_objs:
				todo_data = {'title': todo_obj.title, 'id': todo_obj.pk}
				todos.append(todo_data)
			response_data['data'] = todos
			return JsonResponse(response_data)
		else:
			response_data = { 'status': 'success', 'errors': 'AJAX not used', }
			return JsonResponse(response_data)

class TodoDone(View):
	def post(self, request):
		if request.is_ajax():
			try:
				pk = request.POST['id']
				todo = Todo.objects.get(pk=pk)
				todo.delete()
				response_data = {'status': 'success', 'id': pk}
			except Todo.DoesNotExist:
				response_data = {'status': 'error', 'errors' : 'That todo does not exist',}
			return JsonResponse(response_data)
		else:
			return JsonResponse({'error': 'Not fetched by AJAX'})
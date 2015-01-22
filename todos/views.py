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
				print request.POST['title']
				# from datetime import datetime
				td = Todo.objects.create(title=request.POST['title'])
				td.save()
				data = {'message': 'Saved Successfully','id': td.id, 'title': td.title}
				HttpResponse(json.dumps(data), content_type="application/json")
			else:
				return JsonResponse(form.errors)
		else:
			data = {
				'errors': 'AJAX not used',
			}
			return HttpResponse(JsonResponse(data))

class TodoUpdate(View):
	def post(self, request):
		if request.is_ajax():
			form = AddTodoForm(request.POST)
			if form.is_valid():
				from datetime import datetime
				id = form.cleaned_data['id']
				todo = Todo.objects.get(pk=id)
				todo.title, todo.notes = form.cleaned_data['title'], form.cleaned_data['notes']
				todo.save()
				data = {'message': 'Saved Successfully','id': todo.pk, 'title': todo.title, 'notes': todo.notes}
				HttpResponse(json.dumps(data), content_type="application/json")
			else:
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
			yesterday = datetime.date.today() - datetime.timedelta(days=1)
			todo_objs = Todo.objects.filter(due__gt=yesterday).order_by('-modified')
			response = {'message': 'Today\'s Stuff'}
			response_data = []
			for todo_obj in todo_objs:
				todo_data = {'title': todo_obj.title, 'notes': todo_obj.notes, 'id': todo_obj.pk}
				response_data.append(todo_data)
			response['data'] = response_data
			return JsonResponse(response)
		else:
			data = {
				'errors': 'AJAX not used',
			}
			return HttpResponse(JsonResponse(data))

class TodoListFuture(View):

	def get(self, request):
		if request.is_ajax():
			import datetime
			today = datetime.date.today()
			todo_objs = Todo.objects.filter(due__gte=today).order_by('-modified')
			response = {'message': 'Today\'s Stuff'}
			response_data = []
			for todo_obj in todo_objs:
				todo_data = {'title': todo_obj.title, 'notes': todo_obj.notes, 'id': todo_obj.pk}
				response_data.append(todo_data)
			response['data'] = response_data
			return JsonResponse(response)
		else:
			data = {
				'errors': 'AJAX not used',
			}
			return HttpResponse(JsonResponse(data))

class TodoDone(View):
	def post(self, request):
		if request.is_ajax():
			try:
				pk = request.POST['id']
				todo = Todo.objects.get(pk=pk)
				todo.delete()
				data = {'message': 'Done',}
				return JsonResponse(data)
			except Todo.DoesNotExist:
				error = { 'error': 'That todo does not exist',}
				return JsonResponse(error)
		else:
			return JsonResponse({'error': 'Not fetched by AJAX'})
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View, ListView, DetailView
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse, reverse_lazy
from models import Todo
from forms import AddTodoForm

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
	def get(self, request):
		return HttpResponse('Fetched via get')
	def post(self, request):
		if request.is_ajax():
			form = AddTodoForm(request.POST)
			if form.is_valid():
				from datetime import datetime
				todo = Todo(title=form.cleaned_data['title'], notes=form.cleaned_data['notes'])
				todo.save()
				data = {'message': 'Saved Successfully','id': todo.pk, 'title': todo.title, 'notes': todo.notes}
				return JsonResponse(data)
			else:
				return JsonResponse(form.errors)
		else:
			data = {
				'errors': 'AJAX not used',
			}
			return HttpResponse(JsonResponse(data))

class TodoUpdate(AjaxableResponseMixin, UpdateView):
	model = Todo
	form_class = 'AddTodoForm'
	template_name = 'nothing.html'

	def build_return_data(self):
		todo = self.object
		data = {}
		data['id'] = todo.pk
		data['title'] = todo.title
		data['notes'] = todo.notes
		data['done'] = todo.done
		data['due'] = todo.due
		data['message'] = 'Saved Successfully'
		return data


class TodoDelete(AjaxableResponseMixin, DeleteView):
	model = Todo
	template_name = 'nothing.html'

	def build_return_data(self):
		todo = self.object
		data = {'message': 'Deleted Successfully'}

		return data

class TodoList(AjaxableResponseMixin, ListView):
	model = Todo
	template_name = 'nothing.html'

class TodoListToday(View):

	def get(self, request):
		if request.is_ajax():
			import datetime
			yesterday = datetime.date.today() - datetime.timedelta(days=1)
			todo_objs = Todo.objects.filter(due__gt=yesterday)
			response = {'message': 'Today\'s Stuff'}
			response_data = {}
			for todo_obj in todo_objs:
				todo_data = {'title': todo_obj.title, 'notes': todo_obj.notes}
				response_data.append(todo_data)
			response['data'] = response_data
			return JsonResponse(response)
		else:
			data = {
				'errors': 'AJAX not used',
			}
			return HttpResponse(JsonResponse(data))

class TodoListFuture(AjaxableResponseMixin, ListView):
	model = Todo
	template_name = 'nothing.html'

	def get_queryset(self):
		import datetime
		today = datetime.date.today()
		return Todo.objects.filter(due__gte=today)


class TodoDetail(AjaxableResponseMixin, DetailView):
	model = Todo
	template_name = 'nothing.html'


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
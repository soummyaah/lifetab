from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.core.urlresolvers import reverse, reverse_lazy
from models import Entry

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
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax() and self.request.method == 'POST':
            data = {
                'pk': self.object.pk,
            }
            return JsonResponse(response)
        else:
            return JsonResponse(ajaxerror)

class TodoCreate(AjaxableResponseMixin, CreateView):
	model = Todo

class TodoUpdate(AjaxableResponseMixin, UpdateView):
	model = Todo

class TodoDelete(AjaxableResponseMixin, DeleteView):
	model = Todo


class TodoList(AjaxableResponseMixin, ListView):
	model = Todo

class TodoListToday(AjaxableResponseMixin, ListView):
	model = Todo
	def get_queryset(self):
		import datetime
		yesterday = datetime.date.today() - datetime.timedelta(days=1)
		return Todo.objects.filter(due__gt=yesterday)

class TodoListFuture(AjaxableResponseMixin, ListView):
	model = Todo
	def get_queryset(self):
		import datetime
		today = datetime.date.today()
		return Todo.objects.filter(due__gte=today)


class TodoDetail(AjaxableResponseMixin, DetailView):
	model = Todo
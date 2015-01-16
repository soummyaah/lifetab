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


class EntryCreate(AjaxableResponseMixin, CreateView):
	model = Entry

class EntryUpdate(AjaxableResponseMixin, UpdateView):
	model = Entry

class EntryDelete(AjaxableResponseMixin, DeleteView):
	model = Entry


class EntryList(AjaxableResponseMixin, ListView):
	model = Entry

class EntryDetail(AjaxableResponseMixin, DetailView):
	model = Entry
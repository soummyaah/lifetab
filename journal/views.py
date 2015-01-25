from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.core.urlresolvers import reverse, reverse_lazy

from models import Entry

# Main class based methods to be used
class EntryCreate(AjaxableResponseMixin, CreateView):
	model = Entry
	template_name = 'nothing.html'

	def build_return_data(self):
		entry = self.object
		data = {}
		data['id'] = entry.pk
		data['title'] = entry.title
		data['content'] = entry.content
		data['feeling'] = entry.feeling
		data['message'] = 'Created Successfully'
		return data

class EntryUpdate(AjaxableResponseMixin, UpdateView):
	model = Entry
	template_name = 'nothing.html'

	def build_return_data(self):
		entry = self.object
		data = {}
		data['id'] = entry.pk
		data['title'] = entry.title
		data['content'] = entry.content
		data['feeling'] = entry.feeling
		data['message'] = 'Saved Successfully'
		return data

class EntryDelete(AjaxableResponseMixin, DeleteView):
	model = Entry
	template_name = 'nothing.html'

	def build_return_data(self):
		entry = self.object
		data = {'message': 'Deleted Successfully'}

		return data

class EntryList(AjaxableResponseMixin, ListView):
	model = Entry
	template_name = 'nothing.html'

class EntryDetail(AjaxableResponseMixin, DetailView):
	model = Entry
	template_name = 'nothing.html'




# method stubs to be used for testing of ajax

def EntryCreate(request):
	return JsonResponse({'status': success})

def EntryUpdate(request):
	return JsonResponse({'status': success})

def EntryDelete(request):
	return JsonResponse({'status': success})

def EntryList(request):
	return JsonResponse({'status': success})

def EntryDetail(request):
	return JsonResponse({'status': success})
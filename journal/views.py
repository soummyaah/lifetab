from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.core.urlresolvers import reverse, reverse_lazy

from models import Entry

# Main class based methods to be used
class EntryCreate(View):
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

class EntryUpdate(View):
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

class EntryDelete(View):
	model = Entry
	template_name = 'nothing.html'

	def build_return_data(self):
		entry = self.object
		data = {'message': 'Deleted Successfully'}

		return data

class EntryList(View):
	model = Entry
	template_name = 'nothing.html'

class EntryDetail(View):
	model = Entry
	template_name = 'nothing.html'




# method stubs to be used for testing of ajax

def entryCreate(request):
	return JsonResponse({'status': success})

def entryUpdate(request):
	return JsonResponse({'status': success})

def entryDelete(request):
	return JsonResponse({'status': success})

def entryList(request):
	data = [
		{
			'id': 12,
			'title': 'this is a test',
			'content': 'This is supposed to be a long thing that is concatenated to be as short as possible...',
			'feeling': 'Happy',
			'is_protected': False,
		},
		{
			'id': 21,
			'title': 'a protected text',
			'content': 'Contents Hidden. Click to enter password',
			'feeling': 'Sad',
			'is_protected': True,
		},
	]
	return JsonResponse({'status': success, 'data':data})

def entryDetail(request):
	return JsonResponse({'status': success})
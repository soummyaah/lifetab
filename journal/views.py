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
	data = {
			'title': request.POST['title'],
			'content': request.POST['content'],
			'feeling': request.POST['feeling'],
		}
	if 'is_protected' in  request.POST:
		data['is_protected'] = True
	else:
		data['is_protected'] = False

	return JsonResponse({'status': 'success', 'data': data})

def entryUpdate(request):
	passcode = request.POST['passcode']
	data = {
			'id': request.POST['id'],
			'title': request.POST['title'],
			'content': request.POST['content'],
			'feeling': request.POST['feeling'],
			'is_protected': request.POST['is_protected'],
		}
	return JsonResponse({'status': 'success', 'data':data})

def entryDelete(request):
	title = "This is a title"
	return JsonResponse({'status': 'success', 'title': title})

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
	return JsonResponse({'status': 'success', 'data':data})

def entryDetail(request):
	data = {
			'id':	request.POST['id'],
			'title':	request.POST['title'],
			'content':	request.POST['content'],
			'feeling':	request.POST['feeling'],
			'is_protected': request.POST['is_protected'],
		}
	return JsonResponse({'status': 'success', 'data': data})
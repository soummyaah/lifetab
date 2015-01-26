from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View, ListView, DetailView
from django.http import HttpResponse, JsonResponse
from django.core.urlresolvers import reverse, reverse_lazy
from models import Entry
from forms import AddEntryForm
import json

# Main class based methods to be used
class EntryCreate(View):
	def post(self, request):
		if request.is_ajax():
			form = AddEntryForm(request.POST)
			if form.is_valid():
				# print request.POST['title']
				# from datetime import datetime
				# td = Todo.objects.create(title=request.POST['title'])
				en = form.save()
				# td.save()
				response_data = {'status': 'success',
									'data':	{
											'title': en.title,
											},
								}
			else:
				response_data = {'status': 'error', 'errors': form.errors}
			return JsonResponse(response_data)
		else:
			response_data = {
				'status': 'error',
				'errors': 'AJAX not used'}
			return JsonResponse(response_data)

class EntryUpdate(View):
	def post(self, request):
		entry_id = request.POST['id'].strip();	

		if entry_id:
			try:

				entry = Entry.objects.get(pk=int(entry_id))
			except Entry.DoesNotExist:
				return JsonResponse({'status': 'error', 'errors': 'Entry does not exist'})
		else:
			entry = Entry()

		if request.is_ajax():
			form = AddEntryForm(request.POST, instance=entry)
			if form.is_valid():
				#from datetime import datetime
				entry = form.save()
				response_data = {'status': 'success',
									'data':{'id': entry.id,
											'title': entry.title,
											'content': entry.content,
											'feeling': entry.get_feeling_display(),
											'is_protected': entry.is_protected,
											}
								}
			else:
				response_data = {'status': 'error', 'errors': form.errors}
			return JsonResponse(response_data)
		else:
			data = {'status': 'error',
				'errors': 'AJAX not used',
			}
			return HttpResponse(JsonResponse(data))


class EntryDelete(View):
	def post(self, request):
		if request.is_ajax():
			try:
				pk = request.POST['id']
				# title = request.POST['title']
				# content = request.POST['content']
				# feeling = request.POST['feeling']
				# is_protected = request.POST['is_protected']
				entry = Entry.objects.get(pk=pk)
				entry.delete()
				response_data = {'status': 'success', 'data':{
												# 'id': pk,
												'title': entry.title,
												# 'content': content,
												# 'feeling': feeling,
												# 'is_protected': is_protected
												}
								}
			except Entry.DoesNotExist:
				response_data = {'status': 'error', 'errors' : 'That entry does not exist',}
			return JsonResponse(response_data)
		else:
			return JsonResponse({'status': 'error', 'errors': 'Not fetched by AJAX'})

class EntryList(View):
	def get(self, request):
		if request.is_ajax():
			#import datetime
			#yesterday = datetime.date.today() - datetime.timedelta(days=1)
			entry_objs = Entry.objects.all().order_by('-modified')
			response_data = {'status': 'success'}
			entry = []
			for entry_obj in entry_objs:
				entry_data = {'id': entry_obj.id, 'title': entry_obj.title, 'content': entry_obj.content, 'feeling': entry_obj.get_feeling_display(), 'is_protected': entry_obj.is_protected}
				entry.append(entry_data)
			response_data['data'] = entry
			return JsonResponse(response_data)
		else:
			# data = {
			# 	'errors': 'AJAX not used'
			# }	
			return HttpResponse(JsonResponse({'status':'error', 'errors': 'Not fetched by AJAX'}))

class EntryDetail(View):
	def post(self, request):
		if request.is_ajax():
			try:
				pk = request.POST['id']
				entry = Entry.objects.get(pk=pk)
				# title = request.POST['title']
				# content = request.POST['content']
				# feeling = request.POST['feeling']
				# is_protected = request.POST['is_protected']
				response_data = {'status': 'success', 'data':
											{'id': pk,
											'title': entry.title,
											'content': entry.content,
											'feeling': entry.get_feeling_display(),
											'is_protected': entry.is_protected
											}}
			except Todo.DoesNotExist:
				response_data = {'status': 'error', 'errors' : 'That todo does not exist',}
			return JsonResponse(response_data)
		else:
			response_data = {'status': 'error', 'errors' : 'Not fetched by AJAX',}
			return JsonResponse(response_data)

# method stubs to be used for testing of ajax

# def entryCreate(request):
# 	data = {
# 			'title': request.POST['title'],
# 			'content': request.POST['content'],
# 			'feeling': request.POST['feeling'],
# 		}
# 	if 'is_protected' in  request.POST:
# 		data['is_protected'] = True
# 	else:
# 		data['is_protected'] = False
# 	return JsonResponse({'status': 'success', 'data': data})

# def entryUpdate(request):
# 	passcode = request.POST['passcode']
# 	data = {
# 			'id': request.POST['id'],
# 			'title': request.POST['title'],
# 			'content': request.POST['content'],
# 			'feeling': request.POST['feeling'],
# 			'is_protected': request.POST['is_protected'],
# 		}
# 	return JsonResponse({'status': 'success', 'data':data})

# def entryDelete(request):
# 	title = "This is a title"
# 	return JsonResponse({'status': 'success', 'title': title})

# def entryList(request):
# 	data = [
# 		{
# 			'id': 12,
# 			'title': 'this is a test',
# 			'content': 'This is supposed to be a long thing that is concatenated to be as short as possible...',
# 			'feeling': 'Happy',
# 			'is_protected': False,
# 		},
# 		{
# 			'id': 21,
# 			'title': 'a protected text',
# 			'content': 'Contents Hidden. Click to enter password',
# 			'feeling': 'Sad',
# 			'is_protected': True,
# 		},
# 	]
# 	return JsonResponse({'status': 'success', 'data':data})

# def entryDetail(request):
# 	data = {
# 			'id':	request.POST['id'],
# 			'title':	request.POST['title'],
# 			'content':	request.POST['content'],
# 			'feeling':	request.POST['feeling'],
# 			'is_protected': request.POST['is_protected'],
# 		}
# 	return JsonResponse({'status': 'success', 'data': data})
#	return JsonResponse({'status': 'success', 'id': request.POST['id']})

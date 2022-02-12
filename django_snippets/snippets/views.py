from django.http import HttpResponse

def top(request):
    return HttpResponse(b'Hello World')

def snippets_list(request):
    return HttpResponse('all snippets list')

def snippet_new(request):
    return HttpResponse('new snippet')

def snippet_detail(request, snippet_id):
    return HttpResponse('detail snippet')

def snippet_edit(request, snippet_id):
    return HttpResponse('edit snippet')

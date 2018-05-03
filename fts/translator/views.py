from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from django.urls import reverse
from django.http import JsonResponse

def index(request):
#    all_clients = Client.objects.all()
#    template = loader.get_template('registration/index.html')
#    context = {
#        'name': name,
#    }
#    response_body = template.render(context)
    return HttpResponse("404")
#render(request, 'registration/index.html', locals())

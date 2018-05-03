from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader, RequestContext
from django.urls import reverse
from django.http import JsonResponse
import datetime
from .models import Client

def index(request):
    all_clients = Client.objects.all()
#    template = loader.get_template('registration/index.html')
#    context = {
#        'name': name,
#    }
#    response_body = template.render(context)
    return render(request, 'registration/index.html', locals())

def edit(request, cl_id):
    try:
        client = Client.objects.get(pk=cl_id)
    except Client.DoesNotExist as Exc:
        raise Http404('Товар не найден') from Exc
    return render(request, 'registration/edit.html', locals())

def save(request, cl_id):
    if request.method.upper() != 'POST':
        raise Http404('Неврный метод запроса')
    client = get_object_or_404(Client, pk = cl_id)
    client.c_id = request.POST['cid']
    client.name = request.POST['name']
    client.surname = request.POST['surname']
    client.email = request.POST['email']
    client.phone = request.POST['phone']
    client.reg_date = request.POST['reg_date']
    client.save()
    return HttpResponseRedirect(reverse('registration:index'))

# Registration new User
def new(request):
    if 'name' in request.POST and 'surname' in request.POST and 'email' in request.POST and 'phone' in request.POST:
        if Client.objects.filter(phone=request.POST['phone']).exists():
            return JsonResponse({"response":"record_ex"})
        client = Client()
        client.name = request.POST['name']
        client.surname = request.POST['surname']
        client.email = request.POST['email']
        client.phone = request.POST['phone']
        client.c_id = client.surname[0]+client.name[0]+client.phone
        client.reg_date = datetime.date.today().strftime("%d.%m.%Y")
        client.save()
        return JsonResponse({"response":client.c_id})
    else:
        return JsonResponse({"response":"field_er"})

# Authentication
def authentication(request):
    if 'phone' in request.POST:
#        if Client.objects.filter(phone=request.POST['phone']).exists():
        try:
            client = Client.objects.get(phone=request.POST['phone'])
        except Client.DoesNotExist as Exc:
            return JsonResponse({"response":"denied"}) 
        return JsonResponse({"response":client.c_id})
#        else:
#            return JsonResponse({"response":"denied"})
    else:
        return JsonResponse({"response":"error"})


def delete(request, cl_id):
    client = get_object_or_404(Client, pk=cl_id)
    client.delete()
    return HttpResponseRedirect(reverse('registration:index'))

from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Order
from .models import Files
from registration.models import Client
from .utils.Utils import *


# index
def index(request):
    all_orders = Order.objects.all()
    return render(request, 'orders/index.html', locals())


#new
def new(request):
    if 'language' in request.POST and 'pages' in request.POST:
        order = Order()
#        token = request.POST['token']
        order.o_id = generate_id()
        order.lang = request.POST.get('language', "unknown")
        order.pages = request.POST.get('pages',"unknown")
        order.urgency = request.POST.get('urgency', "unknown")
        try:
            client = Client.objects.get(c_id=request.POST.get('myid', "unknown"))
        except Client.DoesNotExist as Exc:
            return JsonResponse({"response":"unknown_cl", "id":"none"})
        order.customer = client.c_id
        order.date = datetime.date.today().strftime("%d.%m.%Y")
        order.file_path = 'orders_files/' + order.o_id + '/'
        files = request.FILES.getlist('files', [])
        for f in files:
            new_file = Files()
            new_file.ord_id = order.o_id
            new_file.ord_file = f
            new_file.save()
        order.save()
        return JsonResponse({"response": "ord_added", "id": order.o_id})
    else:
        return JsonResponse({"response": "ferror"})


#test
def test(request):
    if 'language' in request.POST and 'pages' in request.POST:
        return JsonResponse({"response":"taked", "id":"iiiiidddd"})
    else:
        return JsonResponse({"response":"ferror"})


def delete(request, or_id):
    pass
#    order = get_object_or_404(Order, pk=or_id)
#    order.delete()
#    return HttpResponseRedirect(reverse('orders:index'))


def deleteall(request):
    Order.objects.all().delete()

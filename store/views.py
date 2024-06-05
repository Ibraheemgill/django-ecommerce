from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse

from store.models import Product,OrderItem


def index(request):
    queryset= Product.objects.filter(id__in= OrderItem.objects.values('product_id').distinct()).order_by('title')
    # query_set=OrderItem.objects.filter(unit_price=20)
    return render(request,'index.html',{'product':queryset}) 
    # try:

    #    product =Product.objects.get(pk=1)
    #    # return HttpResponse('heloooooo')
    #    return  render(request,'index.html')
    # except ObjectDoesNotExist :
    #   pass

# Create your views here.

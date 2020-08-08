from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm

# Create your views here.

def index (request): 
    item_list= Item.objects.all()
    template= loader.get_template('myapp/index.html')
    context= {
        'item_list' : item_list,
    }
    return render(request,'myapp/index.html',context)

def detail(request,item_id):
    item= Item.objects.get(pk=item_id)
    context= {
        'item' : item,
    }
    return render(request,'myapp/detail.html',context)

def create_item (request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('myapp:index')

    return render(request,'myapp/item-form.html',{'form':form})



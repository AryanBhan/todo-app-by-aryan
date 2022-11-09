
from django.contrib import messages

from .models import Todo
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import Listform
# Create your views here.
def index(request):
    if request.method=='POST':
        form=Listform(request.POST or None)
        if form.is_valid():
            form.save()
            all_item=Todo.objects.all()

            messages.success(request,("Item Has Been Added"))
            return render(request,"index.html",{'all_item':all_item})
    else:
        all_item=Todo.objects.all()
        return render(request,"index.html",{'all_item':all_item})
def about(request):
    return render(request,"about.html")

def delete(request,list_id):
    item=Todo.objects.get(pk=list_id)
    item.delete()
    messages.success(request,("Item Deleted Successfull"))
    return redirect("/")
def edit(request,list_id):
    if request.method=='POST':
        item=Todo.objects.get(pk=list_id)
        form=Listform(request.POST or None,instance=item)
        if form.is_valid():
            form.save()
            
            messages.success(request,("Item Has Been Edited"))
            return redirect("/")
    else:
        item=Todo.objects.get(pk=list_id)
        print(item)
        return render(request,"edit.html",{"item":item})
def cross(request,list_id):
    item=Todo.objects.get(pk=list_id)
    item.status=True
    item.save()
    return redirect("/")
def uncross(request,list_id):
    item=Todo.objects.get(pk=list_id)
    item.status=False
    item.save()
    return redirect("/")


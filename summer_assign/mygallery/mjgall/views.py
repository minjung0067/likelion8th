from django.shortcuts import render, get_object_or_404 ,redirect
from .models import photo
from django.urls import reverse
from .forms import createForm
import os

# Create your views here.

def main(request):
    photo_obj = photo.objects
    return render(request, 'main.html', {"photo_key":photo_obj})

def update(request,update_id):
    update_obj = get_object_or_404(photo,pk=update_id)
    form = createForm()
    if request.method == "POST":
        update_obj.name = request.POST['name']
        update_obj.about = request.POST['about']
        update_obj.pic = request.FILES['pic']
        update_obj.save()
        return redirect(reverse('main'))
    else:
        pass
    return render(request, 'update.html', {"update_key":update_obj,"form":form})

def create(request):
    form = createForm()
    if request.method == "POST":
        photo_val = photo()
        photo_val.name = request.POST['name']
        photo_val.about = request.POST['about']
        photo_val.pic = request.FILES['pic']
        photo_val.save()
        return redirect(reverse('main'))
    else:
        pass
    return render(request, 'create.html',{'form':form})

def delete(request, delete_id):
    delete_obj = get_object_or_404(photo, pk= delete_id)
    delete_obj.delete()
    return redirect('main')
from django.http import HttpResponse
from django.shortcuts import render, redirect
from carapp.forms import Carform
from carapp.models import Car
app_name = 'carapp'

def index(request):
    car = Car.objects.all()
    context = {
                'car_list': car }
    return render(request,'index.html',context)
def detail(request,car_id):
    car = Car.objects.get(id=car_id)
    return render(request,'detail.html',{'cars':car})
def add_car(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        car = Car(name=name,desc=desc,year=year,img=img)
        car.save()
    return render(request,'add.html')
def update(request,id):
    car = Car.objects.get(id=id)
    form = Carform(request.POST or None, request.FILES, instance=car)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'car':car})
def delete(request,id):
    if request.method == 'POST':
        car = Car.objects.get(id=id)
        car.delete()
        return redirect('/')
    return render(request,'delete.html')


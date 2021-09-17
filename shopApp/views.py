from django.shortcuts import redirect,render
from .models import vegetables
from .forms import vegForm
from django.contrib import messages
# Create your views here.

def vegIndex(request):
    return render(request,'index.html')

def vegHome(request):
    vegetable = vegetables.objects.all()
    return render(request,'Home.html',{'veggie':vegetable})

def vegDetails(request,v_id):
    veggie = vegetables.objects.get(id=v_id)
    return render(request,'Details.html',{'items':veggie})

def addVeg(request):
    if request.method =='POST':
        Vname = request.POST.get('name')
        Vqty = request.POST.get('quantity')
        Vimage = request.FILES['image']
        Vprice = request.POST.get('price')

        obj = vegetables(Name=Vname, Quantity=Vqty, Image=Vimage, Price=Vprice)
        obj.save()
    
        
    return render(request,'AddItem.html')

def updateVeg(request,v_id):
    obj = vegetables.objects.get(id=v_id)
    form = vegForm(request.POST or None,request.FILES,instance=obj)
   
    if form.is_valid():
        form.save()
        print('Updated')
    return render(request,'Update.html',{'form':form, 'value':obj})

def deleteVeg(request,v_id):
    if request.method == 'POST':
        obj_del = vegetables.objects.get(id=v_id)
        obj_del.delete()
        return redirect('/')
    return render(request, 'Delete.html')
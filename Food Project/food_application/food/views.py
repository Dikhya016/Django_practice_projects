from django.shortcuts import render,redirect,get_object_or_404
from .models import Item,Profile
from .forms import ItemForm,RegisterForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login,logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            Profile.objects.create(user=user)
            return redirect('login')
    form=RegisterForm()
    return render(request,'food/signup.html',{'form':form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'food/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required
def index(request):
    profile = Profile.objects.get(user=request.user)
    items=Item.objects.filter(profile=profile)
    return render(request,'food/index.html',{'items':items})

@login_required
def details(request,id):
    profile = Profile.objects.get(user=request.user)
    item=get_object_or_404(Item,id=id,profile=profile)
    return render(request,'food/details.html',{'item':item})

@login_required
def createitem(request):
    form=ItemForm(request.POST)
    if form.is_valid():
        item=form.save()
        item.profile = Profile.objects.get(user=request.user)
        item.save()
        return redirect('index')
    return render(request,'food/create_update.html',{'form':form})

@login_required
def updateitem(request,id):
    profile = Profile.objects.get(user=request.user)
    item = get_object_or_404(Item, id=id, profile=profile)
    form=ItemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('index')
    
    return render(request,'food/create_update.html',{'form':form,'item':item})

@login_required
def deleteitem(request,id):
    profile = Profile.objects.get(user=request.user)
    item = get_object_or_404(Item, id=id, profile=profile)

    if request.method=='POST':
        item.delete()
        return redirect('index')
    
    return render(request,'food/delete.html',{'item':item})
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
from .forms import CreateUserForm

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect('dashboardView')
    else:
        if request.method == 'POST':
            username = request.POST.get('username') 
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboardView')
            else:
                messages.info(request,'Check your username and password again!') 
    return render(request, 'login.html') 



def registerView(request):
    if request.user.is_authenticated:
        return redirect('dashboardView')
    else:
        form = CreateUserForm() 
        if request.method == 'POST': 
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save()   
                #adding to the nurse group 
                user = form.cleaned_data.get('username') 
                messages.success(request, 'Thank you '+user+' for registering. Please login now to explore our app.  ')
                return redirect('loginView')
    context = { 
        'form': form, 
         
    }
    return render(request,'register.html',context) 
     

def logoutView(request):
    logout(request)
    return redirect('loginView') 


 
from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get("username")
        email = request.POST.get('email')
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        if pass1 != pass2 :
            messages.info(request,'Password is not matching')
        try:
            if User.objects.get(username=username):
                messages.warning(request,'Username is Alredy Taken')  
                return redirect ('/signup')
        except Exception as identifier:
            pass    

        user = User.objects.create_user(username,email,pass1)
        user.save()
        print(user)
        messages.success(request," Signin Successfuly!! ")
        return redirect('/') 

    return render(request,'signup.html')    

def handalelogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get('pass1')
        print(username,pass1)
        user = authenticate(request, username=username, password=pass1)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successfull !!')
            return redirect('/')
        else:
            messages.error(request,"Invalid Creadentials")
            return redirect('/login')
    return render (request,'login.html')    


















def topicsPage(request):
    return render(request,'base/topics.html')
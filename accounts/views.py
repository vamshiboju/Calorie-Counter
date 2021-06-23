from django.shortcuts import render ,redirect
from  .models import Breakfast, Lunch , Dinner
from .models import Calc
from django.contrib.auth.models import User,auth
from django.contrib import messages
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            print(user)
            auth.login(request,user)
            return redirect("/")
        else :
            messages.info(request,'Ivalid Username/Password')
            return redirect('login')
    else :
        return render(request,'login.html')    
def register(request):
    if request.method == 'POST' :
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 == password2 :
            if User.objects.filter(username=username).exists(): 
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else : 
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name, last_name=last_name)
                user.save();
                messages.info(request,'Account Succesfully Created')
                return redirect('login')

        else :
            messages.info(request,'Password Not Matches')
            return redirect('register')
    else :     
        return render(request,"register.html")
# Create your views here.
def BMICALC(request):
    u=None            
    if request.method == 'POST':
        username=request.POST["username"]
        age=int(request.POST["age"])
        weight=int(request.POST["weight"])
        height=float(request.POST["height"])
        if request.user.is_authenticated  :
            u=request.user.username   
        if u == username :
            if age >= 18 and age <= 65 :
                res = "{:.1f}".format(weight/(height*height))
                c = Calc.objects.all()
                for i in c :
                    if i.username == username :
                        i.delete()
                        count=1
                        break
                    else :
                        pass       
                ins=Calc(username=username,age=age,weight=weight,height=height,res=res)
                ins.save();
                if float(res) > 25.0 :
                    messages.info(request,' It indicates that your OVERWEIGHT ')
                elif float(res) >= 18.5 and float(res) <= 24.9 :
                    messages.info(request,' It indicates that your HEALTHY ')
                else :
                    messages.info(request,' It indicates that your UNDERWEIGHT')
                return render(request,'BMI.html',{'result' : res })
            else :
                messages.info(request,'BMI only applies to people of age 18-65')
                return redirect('BMICALC')
        else :
            messages.info(request,'       Enter  Your  User  Name CORRECTLY   ')
            return redirect('BMICALC')
    else :  
        global r 
        r=0
        c = Calc.objects.all()
        current_user=request.user
        for i in c :
            if current_user.username == i.username :
                r=i.res
                break
        if float(r) >= 25.0 :
            messages.info(request,' it indicates that your OVERWEIGHT ')
        elif float(r) >= 18.5 and float(r) <= 24.9 :
            messages.info(request,' it indicates that your HEALTHY ')
        elif float(r) == 0.0 :
            messages.info(request,' No previous records ')
        else :
            messages.info(request,' it indicates that your UNDERWEIGHT')
        return render(request,'BMI.html',{'result' : r })  
def calorie(request) :
    global p,q,s
    p=0
    q=0
    s=0
    b=Breakfast.objects.all()
    l=Lunch.objects.all()
    d=Dinner.objects.all()
    c = Calc.objects.all()
    #print(U.username)
    current_user=request.user
    print(current_user.username)
    for i in c:
        if current_user.username == i.username :
            p=i.weight
            q=i.age
            break;
        else :
            pass
    s=p*q*0.9        
    return render(request,'calorie.html',{ 'value' : s,'breakfast' : b,'dinner' : d ,'lunch' : l }) 

def diet(request) :
    global r,count1,count2,count3
    r=0
    count1=None
    count2=None
    count3=None
    current_user=request.user
    c = Calc.objects.all()
    print(current_user.username)
    for i in c:
        if current_user.username == i.username :
            r=i.res
            break;
        else :
            pass   
    if float(r) >= 25.0 :
        count1=1
    elif float(r) >= 18.5 and float(r) <= 24.9 :
        count2=1
    elif float(r) == 0 :
        pass        
    else :
        count3=1
    return render(request,'diet.html',{'count1' : count1,'count2' : count2,'count3' : count3})
def workout(request) :
    global r,count1,count2,count3
    r=0
    count1=None
    count2=None
    count3=None
    current_user=request.user
    c = Calc.objects.all()
    print(current_user.username)
    for i in c:
        if current_user.username == i.username :
            r=i.res
            break;
        else :
            pass   
    if float(r) >= 25.0 :
        count1=1
    elif float(r) >= 18.5 and float(r) <= 24.9 :
        count2=1  
    elif float(r) == 0 :
        pass         
    else :
        count3=1
    return render(request,'workout.html',{'count1' : count1,'count2' : count2,'count3' : count3})

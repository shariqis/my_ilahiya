from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader 
from Home.form import EmpForm,StudForm,EmployeeForm
from Home.functions.functions import upload_file
from myproject import settings
from django.core.mail import send_mail

# Create your views here.


def hello(request):
    return HttpResponse('<h1>hello world</h1>')

def myHtml(request):
    temp=loader.get_template("day1.html")
    name=input('enter ur name  : ')
    details={'fname':name}
    return HttpResponse(temp.render(details))


def reg_emp(request):
    if request.method=="POST":
        frm=EmpForm(request.POST)
        
        if frm.is_valid():
            try:
                print('//////////')
                return redirect("/")
            except:
                print('====================')
                return HttpResponse("error")
        
        # return HttpResponse("ihoiiiiiiiiiiiii")
    else:    
        print('////////////////')
        emp=EmpForm()
        return render(request,'emp_reg.html',{'form':emp})
    

def stud_reg(request):
    s=StudForm()
    return render(request,'stu_reg.html',{'frm':s}) 


def about(request):
    return render(request,'aboutus.html')



def em_up(request):    
    if request.method=="POST":
        em=EmployeeForm(request.POST,request.FILES)
        if em.is_valid():
            upload_file(request.FILES['file'])
            return HttpResponse("success")
        else:
            return HttpResponse("error")
    else:    
        e=EmployeeForm()
        return render(request,'emp_up.html',{'frm':e}) 
    
def mysession(request):
    return render(request,'mypage.html')     

def setsession(request):
    request.session["name"] ="ANU"
    request.session['email']='anu@gmail.com'
    return HttpResponse('session set')


def viewsesiion(request):
    if "name" in request.session:
        sname= request.session["name"] 
        semail= request.session['email']
        return HttpResponse(sname + "  " + semail)
    else:
        return HttpResponse("plz login first")
    
def delsession(request):
    if "name" in request.session:
        del request.session["name"]
        del request.session['email']
        return HttpResponse("sucessfully logouted")
    else:
        return HttpResponse("plz login first")
    
    

def set_c(request):
    res=HttpResponse('cookies set')
    res.set_cookie('name','anu')  
    return res  


def get_c(request):
    ename=request.COOKIES['name']
    return HttpResponse('my name is '+ename)


def mail(request):
    subject="welcome"
    msg="hai djnago"
    to= 'tomailId'
    res=send_mail(subject,msg,settings.EMAIL_HOST_USER,[to])
    if res==1:
        m="success"
    else:
        m='failed'
    return HttpResponse(m)        
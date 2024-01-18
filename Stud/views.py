from django.shortcuts import render,redirect
from django.http import HttpResponse
from Stud.form import StudentForm
from django.contrib.auth import authenticate,login,logout
from Stud.models import Student,User,Stud_user

from django.contrib.auth.decorators import login_required


# Create your views here.


def hi(request):
    return HttpResponse('<h1>hello student</h1>')

def stud_add(request):
    if request.method=="POST":
        stufrm=StudentForm(request.POST)
        if stufrm.is_valid():
            stufrm.save()
            # return redirect('/view/')
            return HttpResponse("<script>window.alert('Successfully  Added!!');window.location.href='/view'</script>")
            # return HttpResponse('<h1>success</h1>')
        else:
            return HttpResponse('<h1>error</h1>')
    else:    
        stu=StudentForm()
        return render(request,'stu/stu_reg.html',{'form':stu})
    
    
def view_stud(request):
    details=Student.objects.all()
    print(details)
    return render(request,'stu/view_stud.html',{'data':details})  


def det_stud(request,sid):
    print('--------------------------',sid)
    
    stu=Student.objects.get(id=sid)
    stu.delete()
    
    return HttpResponse("<script>window.alert('Successfully  deleted!!');window.location.href='/view'</script>")

def edit_stud(request,sid):
    print('--------------------------',sid)
    stu=Student.objects.get(id=sid)
    return render(request,'stu/edit_stud.html',{'data':stu})  


def update_stud(request,sid):
    
    st=Student.objects.get(id=sid)
    form=StudentForm(request.POST,instance=st )
    if form.is_valid():
        form.save()    
        return HttpResponse("<script>window.alert('Successfully  updtaed!!');window.location.href='/view'</script>")
    else:    
        return HttpResponse("<script>window.alert('Error Occured!!');window.location.href='/view'</script>")
    
    
def my_orm(request):    
    # s=Student.objects.create(first_name='appu',last_name='thomas',age=12,phone=43434,email="appu@gmail.com")    
    # s.save()
    
    # s=Student.objects.filter(first_name='appu')
    
    # s=Student.objects.exclude(first_name__startswith='ap')
    
    
    # s=Student.objects.filter(first_name__startswith='k')| Student.objects.filter(first_name__startswith='a')
    
    # s=Student.objects.filter(first_name__startswith='k')& Student.objects.filter(first_name__startswith='a')
    
    # s=Student.objects.all().count()
    
    
    # s=Student.objects.all()[:2]
    
    s=Student.objects.all().order_by('-age')
    
    print(s)
    return HttpResponse("<script>window.alert('Successfully  saved!!')</script>")


def stud_signUp(request):
    if request.method=="POST":
        user = request.POST.get('uname')
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        ph = request.POST['ph']
        passw = request.POST['passs']   
        print('...................',user , email)
        
        user_details= User.objects.create_user(first_name=fname, last_name=lname,phone=ph,is_active=0,
email= email, username=user,password=passw,usertype='student')
        user_details.save()
        
        pm = request.POST['pm']
        dpt = request.POST['dpt']
        
        details=Stud_user.objects.create(department=dpt,plus_mark=pm,user_id=user_details)
        details.save()
        
        return HttpResponse("<script>window.alert('Successfully  saved!!')</script>")
    else:
        return render(request,'stu/signUp.html')
    
    
def sign_in(request) :
    if request.method=="POST":
        uname = request.POST.get('uname')
        passw = request.POST.get('passs')
        print(uname,passw)
        user = authenticate(request,username=uname,password=passw)
        
        # user = authenticate(request,username='anu',password='anu')
        print(user)
        
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect("admin_home")
            elif user.usertype == "student":
                request.session['stud_id']=user.id                 
                return redirect("stud_home")
                
            return HttpResponse("<script>window.alert('Successfully  Loged In!!')</script>")
        else:
            return HttpResponse("<script>window.alert('Invalid username and password!!')</script>")
    else:
        return render(request,'stu/singnIn.html')
    
@login_required    
def admin_home(request):
    return render(request,'stu/admin_home.html')

@login_required    
def stud_home(request):
    return render(request,'stu/stud_home.html')    

@login_required
def stud_edit_profile(request):
    
    if request.method=="GET":
    
        sid=request.session['stud_id']
        # print(sid)
        data=User.objects.get(id=sid)
        data1=Stud_user.objects.select_related('user_id').get(user_id=sid)        
        data2=Stud_user.objects.select_related('user_id')          
        
        return render(request,'stu/edit_profile.html',{'details':data,'details1':data1,'details2':data2})
    else:
        user = request.POST.get('uname')
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        ph = request.POST['ph']  
        pm = request.POST['pm']
        dpt = request.POST['dpt'] 

@login_required    
def logouts(request):
    logout(request)
    return redirect(sign_in)

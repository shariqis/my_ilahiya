from django.urls import path
from Home import views


urlpatterns=[
    path("b/",views.hello),
    path("my/",views.myHtml),
    path("emp/",views.reg_emp),
    path("stu/",views.stud_reg),
    path("a/",views.about),
    path("up/",views.em_up),
    
    path("ms/",views.mysession),
    path("ss/",views.setsession, name='uu'),
    path("gs/",views.viewsesiion),
    path("ds/",views.delsession),
    
    
    path("sc/",views.set_c),
    path("gc/",views.get_c),
    path("m/",views.mail),
    
    
]
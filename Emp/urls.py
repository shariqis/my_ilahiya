from django.urls import path
from Emp.views import *


urlpatterns=[
    path('create/', EmpCreateView.as_view(), name='emp_user_create'),
    path('view/', EmpListView.as_view(), name='emp_user_list'),
    path('del/<int:pk>/', EmpDelete.as_view(), name='emp_user_del'),
    # path('<int:pk>/', EmpDeatils.as_view(), name='emp_user_details'),
    path('<int:pk>/update/', EmpUpdate.as_view(), name='emp_user_update'),
    path('books/', BookView.as_view(), name='book_detail'),
]
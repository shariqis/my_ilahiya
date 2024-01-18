from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from Emp.models import Employee,Book
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.
from django.views import View
from Emp.form import BookForm



class EmpCreateView(CreateView):
    model = Employee
    template_name = 'emp_reg.html'
    fields="__all__"
    success_url = reverse_lazy('emp_user_list')
    # fields = ['user_id', 'department', 'plus_mark']
    
    
class EmpListView(ListView):
    model = Employee
    template_name = 'emp_list.html'
    context_object_name = 'oo'
    
    
class EmpDelete(DeleteView,SuccessMessageMixin):
    model=  Employee 
    template_name = "employee_confirm_delete.html"
    success_url=reverse_lazy('emp_user_list')
    success_message = "deleted successfully"
  
    
# class EmpDeatils(DetailView):
#     model=Employee
#     template_name = 'emp_reg.html'
#     context_object_name = 'emp'


class EmpUpdate(UpdateView):
    model=Employee
    template_name = 'emp_reg.html'
    fields="__all__"
    success_url=reverse_lazy('emp_user_list')
    
    

class BookView(View):
    template_name = 'book_detail.html'
    def get(self, request):
        print('......')
        # form = BookForm()
        # return render(request, 'bookform.html', {'form': form})
        return 'success'
    
    def post(self, request):
        print('/////////////////////////')
        return 'success'
        # book = get_object_or_404(Book, pk=pk)
        # form = BookForm(request.POST )  #or None, instance=book
        # if form.is_valid():
        #     form.save()
            
        #     return redirect('book_detail', pk=pk)
        # return render(request, 'bookform.html')
    # , {'book': book, 'form': form}



from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from django.views.generic.edit import DeleteView,UpdateView,CreateView
from django.urls import reverse_lazy
from .models import NhanVien
# Create your views here.
class nhanvien_list(ListView):
    model = NhanVien

class nhanvien_view(DetailView):
    model = NhanVien

class nhanvien_create(CreateView):
    model = NhanVien
    fields = ['name','adrress','email','chucvu','tuoi',]
    success_url = reverse_lazy('nhanvien_list')

class nhanvien_update(UpdateView):
    model = NhanVien
    fields = ['name','adrress','email','chucvu','tuoi',]
    success_url = reverse_lazy('nhanvien_list')

class nhanvien_delete(DeleteView):
    model = NhanVien
    success_url = reverse_lazy('nhanvien_list')
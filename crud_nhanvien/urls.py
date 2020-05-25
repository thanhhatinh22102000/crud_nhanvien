from django.urls import path
from . import views
urlpatterns = [
    path('',views.nhanvien_list.as_view(),name='nhanvien_list'),
    path('view/<int:pk>',views.nhanvien_view.as_view(),name='nhanvien_view'),
    path('create/',views.nhanvien_create.as_view(),name='nhanvien_create'),
    path('view/<int:pk>',views.nhanvien_view.as_view(),name='nhanvien_view'),
    path('edit/<int:pk>',views.nhanvien_update.as_view(),name='nhanvien_update'),
    path('delete/<int:pk>',views.nhanvien_delete.as_view() ,name='nhanvien_delete'),
]
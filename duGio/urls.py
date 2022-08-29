from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),

    path('dugio/', views.duGio, name='duGio'),
    path('dugio/add/', views.add, name='add'),
    path('dugio/add/addrecord/', views.addrecord, name='addrecord'),
    path('dugio/update/<int:id>', views.update, name='update'),
    path('dugio/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('dugio/delete/<int:id>', views.delete, name='delete'),
    path('dugio/sort1/', views.sorting1, name='sorting1'),
    path('dugio/sort2/', views.sorting2, name='sorting2'),
    path('dugio/sort3/', views.sorting3, name='sorting3'),
    path('dugio/sort4/', views.sorting4, name='sorting4'),

    path('khdgtg/', views.KHDGTG, name='KHDGTG'),
    path('khdgtg/addKHDGTG/', views.addKHDGTG, name='addKHDGTG'),
    path('khdgtg/addKHDGTG/addrecordKHDHTG/', views.addrecordKHDGTG, name='addrecordKHDGTG'),
    path('khdgtg/updateKHDGTG/<int:id>', views.updateKHDGTG, name='updateKHDGTG'),
    path('khdgtg/updateKHDGTG/updaterecordKHDGTG/<int:id>', views.updaterecordKHDGTG, name='updaterecordKHDGTG'),
    path('khdgtg/deleteKHDGTG/<int:id>', views.deleteKHDGTG, name='deleteKHDGTG'),


]
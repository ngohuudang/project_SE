from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('baocaomon/', views.baoCaoMon, name='baoCaoMon'),
    path('baocaomon/new/', views.taoBaoCaoMon, name='taoBaoCaoMon'),
    path('baocaohocky/', views.baoCaoHocKy, name='baoCaoHocKy'),
    path('baocaohocky/new/', views.taoBaoCaoHocKy, name='taoBaoCaoHocKy'),

]
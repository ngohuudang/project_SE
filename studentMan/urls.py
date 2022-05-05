from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path("home/", views.admin_home, name='admin_home'),
    path("tiepnhan/", views.tiepNhan, name='tiepNhan'),
    path("danhsachlop/", views.dsLop, name='dsLop'),

    path("tracuu/", views.traCuu, name='traCuu'),

    path("bangdiem/", views.bangDiem, name='bangDiem'),
    path("baocaomonhoc/", views.baoCaoMH, name='baoCaoMonHoc'),
    path("baocaohocki/", views.baoCaoHK, name='baoCaoHocKi'),

]
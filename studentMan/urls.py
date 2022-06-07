from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path("home/", views.admin_home, name='admin_home'),
    path("tiepnhanhocsinh/", views.tiepNhanHS, name='tiepNhanHS'),
    path("danhsachlop/", views.dsLop, name='dsLop'),
    path("lapdanhsachlop/", views.lapDSLop, name='lapDSLop'),

    path("tracuu/", views.traCuu, name='traCuu'),

    path("bangdiem/", views.bangDiem, name='bangDiem'),
    path("bangdiem/capnhat/<int:mark_id>", views.capNhatDiem, name='capNhatDiem'),

    path("baocaomonhoc/", views.baoCaoMH, name='baoCaoMonHoc'),
    path("baocaohocki/", views.baoCaoHK, name='baoCaoHocKi'),
    path("quanlituoi/", views.quanLiTuoi, name='quanLiTuoi'),
    path("quanlilop/", views.quanLiLop, name='quanLiLop'),
    path("quanlimon/", views.quanLiMon, name='quanLiMon'),
    path("quanlimon/capnhat/<int:subject_id>", views.capNhatMon, name='capNhatMon'),
    path("subject/delete/<int:subject_id>",views.xoaMon, name='xoaMon'),
    path("subject/add", views.themMon, name='themMon'),
    path("themtaikhoangv/",views.themTaiKhoanGV,name='themTaiKhoanGV'),
    path("themtaikhoangv/",views.themTaiKhoanGV,name='themTaiKhoanGV'),
]

from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [

    path("home/", views.admin_home, name='admin_home'),
    path("tiepnhanhocsinh/", views.tiepNhanHS, name='tiepNhanHS'),
    path("danhsachlop/", views.dsLop, name='dsLop'),
    path("danhsachlop/<str:pk_test>/", views.dsLopFilter, name='dsLopFilter'),
    path("lapdanhsachlop/", views.lapDSLop, name='lapDSLop'),

    path("tracuu/", views.traCuu, name='traCuu'),

    path("bangdiem/", views.bangDiem, name='bangDiem'),
    path("baocaomonhoc/", views.baoCaoMH, name='baoCaoMonHoc'),
    path("baocaohocki/", views.baoCaoHK, name='baoCaoHocKi'),
    path("quanlituoi/", views.quanLiTuoi, name='quanLiTuoi'),
    path("quanlilop/", views.quanLiLop, name='quanLiLop'),
    path("quanlimon/", views.quanLiMon, name='quanLiMon'),
    path("quanlimon/capnhat/<int:subject_id>", views.capNhatMon, name='capNhatMon'),
    path("subject/delete/<int:subject_id>",views.xoaMon, name='xoaMon'),
    path("subject/add", views.themMon, name='themMon'),
    path("quanlilop/capnhat/<int:class_id>", views.capNhatLop, name='capNhatLop'),
    path("Class/delete/<int:class_id>", views.xoaLop, name='xoaLop'),
    path("Class/add", views.themLop, name='themLop'),
    path("quanlilop/<str:pk_test>/", views.quanLiLopFilter, name='quanLiLopFilter'),

    path("logout/", views.logoutUser, name='logout'),
]
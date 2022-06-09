from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('reset_password/',
         auth_views.PasswordResetView.as_view(),
         name='reset_password'),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    path('capnhattaikhoan/', views.capNhatTaiKhoan, name='capNhatTaiKhoan'),
    path('doimatkhau/', views.doiMatKhau.as_view(), name='doiMatKhau'),
    path("home/", views.admin_home, name='admin_home'),

    path("themAdmin/", views.themAdmin, name='themAdmin'),
    path("themGV/", views.themGV, name='themGV'),
    path("themHS/", views.tiepNhanHS, name='tiepNhanHS'),

    path("danhsachtaikhoan/", views.dsTaiKhoan, name='dsTaiKhoan'),
    path("danhsachlop/", views.dsLop, name='dsLop'),
    path("danhsachlop/nienkhoa", views.chonNienKhoaLop, name='chonNienKhoaLop'),
    path("lapdanhsachlop/nienkhoa_<int:age_id>", views.lapDSLop, name='lapDSLop'),

    path("tracuu/nienkhoa", views.chonNienKhoaTraCuu, name='chonNienKhoaTraCuu'),
    path("tracuu/nienkhoa/nienkhoa_<int:age_id>", views.traCuu, name='traCuu'),

    path("bangdiem/", views.bangDiem, name='bangDiem'),
    path("bangdiem/capnhat/<int:mark_id>", views.capNhatDiem, name='capNhatDiem'),

    path("baocaomonhoc/", views.baoCaoMH, name='baoCaoMonHoc'),
    path("baocaohocki/", views.baoCaoHK, name='baoCaoHocKi'),
    path("baocaohocki/<str:lop>/<str:hocKy>/<str:nienKhoa>/", views.baoCaoHocKy, name='baoCaoHK'),

    path("quanlituoi/", views.quanLiTuoi, name='quanLiTuoi'),
    path("quanlituoi/capnhat/<int:age_id>", views.capNhatTuoi, name='capNhatTuoi'),
    path("quanlituoi/delete/<int:age_id>", views.xoaTuoi, name='xoaTuoi'),
    path("age/add", views.themTuoi, name='themTuoi'),

    path("quanlilop/", views.quanLiLop, name='quanLiLop'),
    path("quanlilop/capnhat/<int:class_id>", views.capNhatLop, name='capNhatLop'),
    path("class/delete/<int:class_id>", views.xoaLop, name='xoaLop'),
    path("class/add", views.themLop, name='themLop'),

    path("quanlimon/", views.quanLiMon, name='quanLiMon'),
    path("quanlimon/capnhat/<int:subject_id>", views.capNhatMon, name='capNhatMon'),
    path("subject/delete/<int:subject_id>", views.xoaMon, name='xoaMon'),
    path("subject/add", views.themMon, name='themMon'),
]

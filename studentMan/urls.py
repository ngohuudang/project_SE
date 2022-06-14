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
    path("taotkhocsinh/",views.taoTKHocSinh,name='taoTKHocSinh')
    
    path('reset_password/',
            auth_views.PasswordResetView.as_view(template_name='admin_template/reset_password_form.html'),
            name='reset_password'),
    path('reset_password_sent/',
            auth_views.PasswordResetDoneView.as_view(template_name='admin_template/thongBaoResetMatKhau.html'),
            name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
            auth_views.PasswordResetConfirmView.as_view(template_name='admin_template/capNhatMatKhau.html'),
            name='password_reset_confirm'),
    path('reset_password_complete/',
            auth_views.PasswordResetCompleteView.as_view(template_name='admin_template/thongBaoResetMatKhauThanhCong.html'),
            name='password_reset_complete'),
]

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

    path("home/", views.admin_home, name='admin_home'),
    path("tiepnhanhocsinh/", views.tiepNhanHS, name='tiepNhanHS'),
    path("danhsachlop/", views.dsLop, name='dsLop'),
    path("lapdanhsachlop/", views.lapDSLop, name='lapDSLop'),

    path("tracuu/", views.traCuu, name='traCuu'),

    path("bangdiem/", views.bangDiem, name='bangDiem'),
    path("baocaomonhoc/", views.baoCaoMH, name='baoCaoMonHoc'),
    path("baocaohocki/", views.baoCaoHK, name='baoCaoHocKi'),
    path("baocaohocki/<str:lop>/<int:hocKy>/<str:nienKhoa>/", views.baoCaoHocKy, name='baoCaoHK'),
    path("quanlituoi/", views.quanLiTuoi, name='quanLiTuoi'),
    path("quanlilop/", views.quanLiLop, name='quanLiLop'),
    path("quanlimon/", views.quanLiMon, name='quanLiMon'),

]

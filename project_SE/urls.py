from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('transcript', include('transcript.urls')),
#     path('baocao/', include("baocao.urls")),
#     path('dangkylophoc', include("dangkylophoc.urls")),
#     path('Tracuuhocsinh', include("Tracuuhocsinh.urls")),
#     path('tiepnhan', include("tiepNhanHocSinh.urls")),
    
# ]

# urlpatterns = [
#     path("", include('main_app.urls')),
#     path("accounts/", include("django.contrib.auth.urls")),
#     path('admin/', admin.site.urls),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studentMan.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
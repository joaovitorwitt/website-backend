from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from system.views import ping

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('articles.urls')),
    path('api/v1/', include('projects.urls')),
    # add endpoint to make periodic requests
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
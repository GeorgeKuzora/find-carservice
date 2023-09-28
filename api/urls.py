from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from api.v1 import urls as v1_urls


app_name = 'api'

urlpatterns = [
    path('v1/', include(v1_urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

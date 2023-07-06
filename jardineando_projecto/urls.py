from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from api import views




router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('staff/', include('staff.urls', namespace='staff')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
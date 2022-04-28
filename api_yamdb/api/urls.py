from django.urls import include, path
from rest_framework.routers import DefaultRouter

"""from .views import ..."""

app_name = 'api'

router_v1 = DefaultRouter()
"""router_v1.register(...)"""

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router_v1.urls)),
]

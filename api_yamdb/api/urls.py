from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .users.views import UsersViewSet, api_gettoken, api_signup

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'users', UsersViewSet)


urlpatterns = [
    path('v1/auth/signup/', api_signup),
    path('v1/auth/token/', api_gettoken),
    path('v1/', include(router_v1.urls)),
]

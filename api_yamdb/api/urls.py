from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .users.views import UsersViewSet, api_gettoken, api_signup
from .views import CategoryViewSet, GenreViewSet, TitleViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'users', UsersViewSet)
router_v1.register(r'categories', CategoryViewSet, basename='categories')
router_v1.register(r'genres', GenreViewSet, basename='genres')
router_v1.register(r'titles', TitleViewSet, basename='titles')


urlpatterns = [
    path('v1/auth/signup/', api_signup),
    path('v1/auth/token/', api_gettoken),
    path('v1/', include(router_v1.urls)),
]

from rest_framework.routers import SimpleRouter

from django.urls import include, path

from api.views import PostViewSet


router = SimpleRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

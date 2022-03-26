from rest_framework.routers import SimpleRouter
from django.urls import include, path

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


router = SimpleRouter()
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet)


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

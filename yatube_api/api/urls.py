from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = SimpleRouter()
router_v1.register('posts', PostViewSet)
router_v1.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='posts')
router_v1.register('groups', GroupViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # Артем, привет! Не знаю как написать тебе в slack.
    # Может быть еще что-то добавим, на развитие?
    # Можно жесткое :) , ведь целая неделя впереди.
    path('v1/', include('djoser.urls.jwt')),
]

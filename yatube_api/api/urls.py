from django.urls import path, include
from rest_framework import routers

from .views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet

router_v1 = routers.DefaultRouter()
router_v1.register('posts', viewset=PostViewSet)
router_v1.register('groups', viewset=GroupViewSet)
router_v1.register(
    'posts/(?P<post_pk>\\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('v1/', include('djoser.urls.jwt')),
]

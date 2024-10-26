from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views  import TokenObtainPairView, TokenRefreshView
from .views import PostViewSet, TagViewSet

urlpatterns = [
    path("", views.index, name='home'),
    path('about123', views.about, name='about'),
]

router = DefaultRouter()

router.register(r'tags', TagViewSet, basename='tags')
router.register(r'posts', views.PostViewSet, basename='posts')
# router.register(r'topic', views.TopicViewSet, basename='topic')

api_urlpatterns = router.urls + [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]



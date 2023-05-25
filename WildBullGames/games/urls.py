from django.urls import path, include
from rest_framework import routers
from .views import GameViewSet, ReviewViewSet, SubmissionViewSet, TagViewSet, ScreenshotViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'games', GameViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'submissions', SubmissionViewSet)
router.register(r'tags', TagViewSet)
router.register(r'screenshots', ScreenshotViewSet)
router.register(r'categories', CategoryViewSet)

app_name = 'games'

urlpatterns = [
    path('', include(router.urls)),
]

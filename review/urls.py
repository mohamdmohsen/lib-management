from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet ,FavoriteViewSet

router = DefaultRouter()
router.register('reviews', ReviewViewSet, basename='review')
router.register('favorites', FavoriteViewSet, basename='favorite')

urlpatterns = router.urls
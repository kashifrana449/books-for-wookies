from rest_framework.routers import DefaultRouter

from .views import BookViewSet

router = DefaultRouter()
router.register('books', BookViewSet, 'book-crud-api')

urlpatterns = router.urls

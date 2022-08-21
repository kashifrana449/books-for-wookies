from rest_framework.routers import DefaultRouter

from .views import UserCreateView

router = DefaultRouter()
router.register('create-user', UserCreateView, 'create-user-api')

urlpatterns = router.urls

"""API routes for the BusinessEnglish app, mounted under ``/api/`` by the
project URLconf. A DRF ``DefaultRouter`` gives us the browsable API root plus
list/detail routes for each viewset.
"""

from rest_framework.routers import DefaultRouter

from .views import LessonViewSet, ExpressionViewSet

router = DefaultRouter()
router.register(r"lessons", LessonViewSet, basename="lesson")
router.register(r"expressions", ExpressionViewSet, basename="expression")

urlpatterns = router.urls

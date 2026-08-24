"""Read-only DRF viewsets for the lesson API.

Everything here is read-only (``ReadOnlyModelViewSet`` → list + retrieve only);
the corpus is authored in ``raw_data/`` and loaded via ``import_lessons``.
"""

from django.db.models import Count
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Lesson, Expression
from .serializers import (
    LessonListSerializer,
    LessonDetailSerializer,
    ExpressionSerializer,
)


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    """`/api/lessons/` (list) and `/api/lessons/{day_number}/` (detail)."""

    # URLs read /api/lessons/1/ rather than exposing the auto PK.
    lookup_field = "day_number"

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["dialogue_topic", "focus_theme", "title"]
    ordering_fields = ["day_number", "date"]
    ordering = ["day_number"]

    def get_queryset(self):
        queryset = Lesson.objects.all()
        if self.action == "list":
            # Cheap list: just annotate the child count.
            return queryset.annotate(expression_count=Count("expressions"))
        # Detail: pull children in bulk to avoid N+1 on the nested serializer.
        return queryset.prefetch_related("expressions__examples", "upgrades")

    def get_serializer_class(self):
        if self.action == "list":
            return LessonListSerializer
        return LessonDetailSerializer

    @action(detail=True, methods=["get"])
    def expressions(self, request, day_number=None):
        """`/api/lessons/{day_number}/expressions/` — this lesson's expressions."""
        lesson = self.get_object()
        queryset = lesson.expressions.prefetch_related("examples")
        kind = request.query_params.get("kind")
        if kind:
            queryset = queryset.filter(kind=kind)
        serializer = ExpressionSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)


class ExpressionViewSet(viewsets.ReadOnlyModelViewSet):
    """`/api/expressions/` — browse/search expressions across all lessons.

    Filter by kind with `?kind=idiom|phrasal_verb|vocabulary`; free-text
    `?search=` covers name/meaning/collocations; `?ordering=` on name/order.
    """

    serializer_class = ExpressionSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "meaning", "collocations"]
    ordering_fields = ["name", "order", "lesson__day_number"]
    ordering = ["lesson__day_number", "kind", "order"]

    def get_queryset(self):
        queryset = Expression.objects.select_related("lesson").prefetch_related("examples")
        kind = self.request.query_params.get("kind")
        if kind:
            queryset = queryset.filter(kind=kind)
        return queryset

from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema

from .models import Apartment
from .serializers import ApartmentSerializer, ApartmentCreateSerializer
from .filters import ApartmentFilter


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user


class ApartmentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


@extend_schema(tags=["apartments"])
class ApartmentViewSet(viewsets.ModelViewSet):
    queryset = Apartment.objects.all()
    lookup_field = 'slug'
    pagination_class = ApartmentPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = ApartmentFilter

    def get_serializer_class(self):
        if self.action == 'create':
            return ApartmentCreateSerializer
        return ApartmentSerializer

    def get_permissions(self):
        if self.action in ['create']:
            permission_classes = [permissions.IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [
                permissions.IsAuthenticated, 
                IsOwnerOrReadOnly
            ]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

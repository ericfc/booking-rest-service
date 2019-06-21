from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets

from bookings.models import Booking
from bookings.serializers import BookingSerializer


class CreateListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    A base viewset that provides create and list actions for a model.
    """
    pass


class BookingViewSet(CreateListViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
    filterset_fields = ('booking_type',)

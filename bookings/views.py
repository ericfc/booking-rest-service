from rest_framework import mixins, viewsets

from bookings.models import Booking
from bookings.serializers import BookingSerializer


class CreateListRetrieveViewSet(
	mixins.CreateModelMixin,
	mixins.ListModelMixin,
	mixins.RetrieveModelMixin,
	viewsets.GenericViewSet,
):
	"""
	A base viewset that provides retrieve, create, and list actions for a
	model.
	"""
	pass


class BookingViewSet(CreateListRetrieveViewSet):
	serializer_class = BookingSerializer
	queryset = Booking.objects.all()

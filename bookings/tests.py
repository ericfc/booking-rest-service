from datetime import date, time, timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from bookings.models import Booking


class BookingAPITestCase(APITestCase):
    def setUp(self):
        Booking.objects.bulk_create([
            Booking(
                name='Jennifer Walters',
                email='jen@greenlaw.com',
                address='621 S Congress Ave Austin, TX 78701',
                booking_type=Booking.HOUSEKEEPING,
                booking_date=date(2019, 6, 24),
                booking_time=time(1, 2)
            ),
            Booking(
                name='Jane Foster',
                email='jane@midgard.com',
                address='622 N Lamar Blvd Austin, TX 78751',
                booking_type=Booking.DOG_WALK,
                booking_date=date(2019, 6, 29),
                booking_time=time(3, 9)
            ),
            Booking(
                name='Kamala K.',
                email='khan@bigm.com',
                address='226 Burnet Rd Austin, TX 78759',
                booking_type=Booking.DOG_WALK,
                booking_date=date(2019, 7, 15),
                booking_time=time(15, 39)
            ),
        ])

    def test_create_booking(self):
        """
        Test creating Booking via POST.
        """
        url = reverse('booking-list')
        data = {
            'email': 'storm@xmansion.com',
            'name': 'Ororo Munroe',
            'address': '364 S 1st St Austin, TX 78704',
            'booking_type': 'housekeeping',
            'booking_date': str(date.today() + timedelta(days=1)),
            'booking_time': '01:02:00'
        }
        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response.data.pop('id')
        self.assertDictEqual(response.data, data)

    def test_create_invalid_booking(self):
        """
        Test creating Booking with invalid booking_type via POST.
        """
        url = reverse('booking-list')
        data = {
            'email': 'storm@xmansion.com',
            'name': 'Ororo Munroe',
            'address': '364 S 1st St Austin, TX 78704',
            'booking_type': 'invalid_booking_type',
            'booking_date': str(date.today() + timedelta(days=1)),
            'booking_time': '01:02:00'
        }
        response = self.client.post(url, data=data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_bookings(self):
        """
        Test get list of Bookings.
        """
        url = reverse('booking-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 3)
        self.assertListEqual(
            response.data['results'],
            [
                {
                    'id': 1,
                    'email': 'jen@greenlaw.com',
                    'name': 'Jennifer Walters',
                    'address': '621 S Congress Ave Austin, TX 78701',
                    'booking_type': 'housekeeping',
                    'booking_date': '2019-06-24',
                    'booking_time': '01:02:00'
                },
                {
                    'id': 2,
                    'email': 'jane@midgard.com',
                    'name': 'Jane Foster',
                    'address': '622 N Lamar Blvd Austin, TX 78751',
                    'booking_type': 'dog_walk',
                    'booking_date': '2019-06-29',
                    'booking_time': '03:09:00'
                },
                {
                    'id': 3,
                    'email': 'khan@bigm.com',
                    'name': 'Kamala K.',
                    'address': '226 Burnet Rd Austin, TX 78759',
                    'booking_type': 'dog_walk',
                    'booking_date': '2019-07-15',
                    'booking_time': '15:39:00'
                }
            ]
        )

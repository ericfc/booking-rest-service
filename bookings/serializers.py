from datetime import datetime

from rest_framework import serializers

from bookings.models import Booking


class BookingSerializer(serializers.ModelSerializer):
    def validate(self, data):
        """
        Validate that the provided booking date and time are in the future.
        """
        validated_data = super().validate(data)
        now_datetime = datetime.now()
        today = now_datetime.date()
        booking_date = validated_data['booking_date']
        error_message = (
            'booking_date and booking_time must be in the future. The current '
            'time is %s' % now_datetime
        )

        if booking_date > today:
            return validated_data
        elif booking_date < today:
            raise serializers.ValidationError(error_message)

        # booking_date is today, now check booking_time
        now_time = now_datetime.time()
        if validated_data['booking_time'] < now_time:
            raise serializers.ValidationError(error_message)

        return validated_data

    class Meta:
        model = Booking
        fields = '__all__'

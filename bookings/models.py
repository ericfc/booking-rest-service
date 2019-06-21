from django.db import models


class Booking(models.Model):
    HOUSEKEEPING = 'housekeeping'
    DOG_WALK = 'dog_walk'
    BOOKING_TYPE_CHOICES = (
        (DOG_WALK, 'Dog Walk'), 
        (HOUSEKEEPING, 'Housekeeping'),
    )

    email = models.EmailField()
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    booking_type = models.CharField(
        max_length=30,
        choices=BOOKING_TYPE_CHOICES,
    )
    booking_date = models.DateField(db_index=True)
    booking_time = models.TimeField(db_index=True)

    def __str__(self):
        return '{} for {}'.format(self.booking_type, self.name)

    class Meta:
        ordering = ['booking_date', 'booking_time']

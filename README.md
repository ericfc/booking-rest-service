# Booking REST API
REST Service to create and retrieve service bookings.
This is a REST API service implemented using Django and Python 3. It provides
endpoints to retrieve paginated service bookings, and to create new bookings.

## Running the application with Docker
After installing Docker you may run
`docker-compose up`
from the base directory.
It will download the necessary dependencies and start the service.
The app will be running on `localhost:8000`

At this point you may run unit tests in a different window:
`docker-compose exec service python manage.py test`

`docker-compose down` will bring down the service.


## API
### Get Bookings
In order to retrieve all bookings perform a `GET` request to the endpoint
`api/bookings/`
It will return the first 20 booking records. They are ordered by booking date
and time.

```
{
    "count": 101,
    "next": "http://localhost:8000/api/bookings/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "email": "fakeemail@exampledomain.com",
            "name": "Bob Smith",
            "address": "103 Main Ave Austin Texas 78704",
            "booking_type": "housekeeping",
            "booking_date": "2019-06-22",
            "booking_time": "18:02:35"
        },
        ...
        {
            "id": 60,
            "email": "nimaclea@comcast.net",
            "name": "Ivan Reilly",
            "address": "235 Deerfield St. Fairburn, GA 30213",
            "booking_type": "housekeeping",
            "booking_date": "2019-07-26",
            "booking_time": "08:09:00"
        }
    ]
}
```

The API implements page number pagination. In order to return the next 20
records use the `next` URL. When you have reached the end of pagination the
`next` value will be `null`.

This endpoint also supports filtering records by `booking_type`. In order to
filter the returned records by `booking_type`, pass the endpoint a query
parameter `booking_type` with either `housekeeping` or `dog_walk`.

For example `api/bookings/?booking_type=housekeeping` will return the first 20
houseekeeping bookings.

### Create Bookings
In order to create a new booking perform a `POST` request to `api/bookings/`
providing all required fields as follows:

```
{
    "email": "exampleemail@yahoo.com",
    "name": "Person Surname",
    "address": "372 N Capital of Tx Hwy Austin TX 78759",
    "booking_type": "housekeeping",
    "booking_date": "2019-07-26",
    "booking_time": "08:09:00"
}
```

Validation will be applied to email, booking_type, booking_date, and
booking_time. The endpoint will return a `400` response with the appropriate
error message when validation fails.

Additionally, the booking_date and booking_time use UTC timezone. New bookings
must take place in the future. Otherwise it will not pass validation and return
a `400` response.

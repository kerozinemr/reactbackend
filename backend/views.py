from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Trip
from .utils import get_ors_route
from django.utils import timezone

@api_view(['POST'])
def create_trip(request):
    data = request.data
    start = data.get('start')  # expected: {'lat': float, 'lng': float}
    pickup = data.get('pickup')
    dropoff = data.get('dropoff')

    coords = [
        [start['lng'], start['lat']],
        [pickup['lng'], pickup['lat']],
        [dropoff['lng'], dropoff['lat']]
    ]

    ors_route = get_ors_route(coords)
    if ors_route is None:
        return Response({"error": "Failed to get route from ORS"}, status=500)

    trip = Trip.objects.create(
        user=request.user,
        start_location=start,
        pickup_location=pickup,
        dropoff_location=dropoff,
        start_time=timezone.now(),
        status='active',
        ors_route=ors_route
    )

    return Response({
        "trip_id": trip.id,
        "route": ors_route,
        "start_time": trip.start_time
    })

        
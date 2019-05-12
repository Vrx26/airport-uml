from django.db import models


class Airport(models.Model):
    airport_id = models.CharField(max_length=4)
    airport_name = models.CharField(max_length=60)
    city = models.CharField(max_length=60)


class Flight(models.Model):
    flight_id = models.CharField(max_length=8, unique=True)
    departure_place = models.ForeignKey(Airport, related_name='departure', on_delete=models.CASCADE)
    arrival_place = models.ForeignKey(Airport, related_name='arrival', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    plane_model = models.CharField(max_length=60)


class Place(models.Model):
    place_id = models.AutoField(primary_key=True)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    place_type = models.IntegerField()  # 0 - economical, 1 - business
    free_places = models.IntegerField()
    price = models.IntegerField()
    luggage_price = models.IntegerField()
    child_place_price = models.IntegerField()


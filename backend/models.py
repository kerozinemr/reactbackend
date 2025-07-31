from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_location = models.JSONField()
    pickup_location = models.JSONField()
    dropoff_location = models.JSONField()
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='active')
    ors_route = models.JSONField(null=True, blank=True)
    
   
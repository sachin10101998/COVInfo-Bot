from __future__ import unicode_literals
from django.db import models


# Create your models here.

class State(models.Model):
    state_name= models.CharField(max_length=200)
    confirmed_cases = models.IntegerField(default=0)
    active_cases = models.IntegerField(default=0)
    dead_cases = models.IntegerField(default=0)
    recovered_cases = models.IntegerField(default=0)

    #Returns name of State
    def __str__(self):
        return self.state_name

    #Returns if state is a hotspot
    def is_a_hotspot(self):
        return ((self.recovered_cases)*2<self.confirmed_cases)

class District(models.Model):
    district_name = models.CharField(max_length=200)
    confirmed_cases = models.IntegerField(default=0)
    active_cases = models.IntegerField(default=0)
    dead_cases = models.IntegerField(default=0)
    recovered_cases = models.IntegerField(default=0)
    
    #Returns district name 
    def __str__(self):
        return self.district_name
    
    #Returns true if district is a hotspot
    def is_a_hotspot(self):
        return ((self.recovered_cases)*2<self.confirmed_cases)


from django.db import models

# Create your models here.
from django.db import models

'''
#   create table flight(destion   text,source text,duration integer)
#   insert into flight values('ahm','bom',2323)
   class flight
       destion = models.textfield()
       source=models.textfield()
       duration = models.Integerfield()

    fl1=flight(destion='ahm',source='bom',duration=2323)    
    fl1.save()   

    flight.objects.all() 

        makemigrations 
        migrate

'''


class airport(models.Model):
    city = models.CharField(max_length=56)
    code = models.CharField(max_length=45)

    def __str__(self):
        return f"Airport({self.city}({self.code}))"


# Create your models here.
class flight(models.Model):
    source = models.ForeignKey(airport, on_delete=models.CASCADE, related_name="departure")
    destion = models.ForeignKey(airport, on_delete=models.CASCADE, related_name="arrival")
    duration = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"flight({self.source} to {self.destion})"

    def is_flight_valid(self):
        return self.source != self.destion or self.duration > 0


class passengers(models.Model):
    first_name = models.CharField(max_length=34)
    last_name = models.CharField(max_length=34)
    flights = models.ManyToManyField(flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"Passenger({self.first_name},{self.last_name})"


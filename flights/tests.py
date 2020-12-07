#from django.test import TestCase,Client

# Create your tests here.
from django.test import TestCase,Client
from .models import airport,flight

# Create your tests here.
class FlightTestCases(TestCase):

    def setUp(self):

        #create airport objectr̥
        a1 = airport.objects.create(city="ahmedabad",code="ahm")
        a2 = airport.objects.create(city="baroda", code="bob")
        a3 = airport.objects.create(city="surat",code="sur")

        #flight object
        fl1=flight.objects.create(source=a1,destion=a2,duration=100,price=1222)
        fl2 = flight.objects.create(source=a1, destion=a1, duration=-150, price=222)
        fl3 = flight.objects.create(source=a1, destion=a3, duration=100, price=1222)


    def test_departure_count(self):
        a1=airport.objects.get(code='ahm')
        self.assertEqual(a1.departure.count(),3)

    def test_arrival_count(self):
        a1=airport.objects.get(code='sur')
        self.assertEqual(a1.arrival.count(),1)

    def test_valid_flight(self):
        a1=airport.objects.get(code='ahm')
        a3=airport.objects.get(code='sur')
        fl=flight.objects.get(source=a1,destion=a3)
        self.assertTrue(fl.is_flight_valid())

    def test_invalid_flight_durations(self):
        fl=flight.objects.get(duration=-150)
        self.assertFalse(fl.is_flight_valid())

    def test_invalid_flight_durations(self):
        a1=airport.objects.get(code="ahm")
        fl=flight.objects.get(source=a1,destion=a1)
        self.assertFalse(fl.is_flight_valid())

    def test_home(self):
        cl=Client()
        response=cl.get("/flights/home")
        self.assertEqual(response.status_code,200)

    def test_no_of_flight_home(self):
        cl = Client()
        response = cl.get("/flights/home")
        self.assertEqual(response.context["flights"].count(), 2)

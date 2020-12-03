from django.urls import path
from . import views
urlpatterns =[

    path("counter",views.showcounter,name="counter"),
    path("home",views.home,name="airline-home"),
    path("flights/<int:flight_id>",views.flight_details,name="flightdetails"),
    path("books/<int:flight_id>",views.book,name="book")
]
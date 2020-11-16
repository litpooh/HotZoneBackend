from django.urls import path
from locations import views

urlpatterns = [
    path('locations/',
         views.LocationView.as_view(),
         name='locations-information'),
#     path('retrieve/',
#          views.RetrieveView.as_view(),
#          name='retrieve_location'),
#     path('addlocation/',
#          views.AddLocationView,
#          name="add_location")
]
from django.urls import path
from api import views

urlpatterns = [
    path('api/puntodeinteres/', views.puntodeinteres_list),
    path('api/puntodeinteres/<pk>', views.puntodeinteres_detail),
    path('api/puntodeinteres/beacons/', views.puntodeinteres_beacons_list),
    path('api/puntodeinteres/beacons/<pk>', views.puntodeinteres_beacons_detail)
]
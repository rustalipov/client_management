from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, CreateClientView, UpdateClientByRegistrationNumber

router = DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('clients/create/', CreateClientView.as_view(), name='create_client'),
    path('clients/update/<str:registration_number>/', UpdateClientByRegistrationNumber.as_view(), name='update_client_by_registration_number'),
]

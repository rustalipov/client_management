from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from clients.views import MyTokenObtainPairView, CreateClientView, UpdateClientByRegistrationNumber

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clients.urls')),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/clients/create/', CreateClientView.as_view(), name='create_client'),
    path('api/clients/update/<str:registration_number>/', UpdateClientByRegistrationNumber.as_view(), name='update_client_by_registration_number'),
]

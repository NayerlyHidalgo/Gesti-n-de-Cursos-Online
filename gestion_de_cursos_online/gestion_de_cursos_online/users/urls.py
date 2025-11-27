# billing_api/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),   # <-- todo lo de usuarios/auth/admin
    # En Parte 2 y 3 añadiremos:
    # path('api/', include('catalog.urls'))
    # path('api/', include('invoices.urls'))
]
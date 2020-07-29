"""RESERVATION_SYS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


from wake_sys.views.views import HomeView, RegisterView, ReservationCreateView, ProfileView, \
    ReservationsView, ReservationUpdateView, ReservationDeleteView, AvailabilityView, AdminReservationView, \
    AdminReservations
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='sys-home'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='sys-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='sys-logout'),
    path('register/', RegisterView.as_view(), name='sys-register'),
    path('reservation/', ReservationCreateView.as_view(), name='sys-reservation'),
    path('profile/', ProfileView.as_view(), name='sys-profile'),
    path('bookings/', ReservationsView.as_view(), name='sys-bookings'),
    path('reservation_update/<int:reservation_id>/', ReservationUpdateView.as_view(), name='sys-reservation-update'),
    path('reservation_delete/<int:pk>/', ReservationDeleteView.as_view(), name='sys-reservation-delete'),
    path('reservation_table/', AvailabilityView.as_view(), name='sys-availability'),
    path('admin/reservation/', AdminReservations.as_view(), name='admin-reservations'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
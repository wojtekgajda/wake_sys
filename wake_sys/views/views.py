from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DeleteView
import datetime
from wake_sys.models import Reservation
from wake_sys.forms.forms import UserRegisterForm, ReservationForm, ProfileUpdateForm, UserUpdateForm, AvailabilityForm
from django.contrib.auth.models import User
from wake_sys.models import HOURS


class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class RegisterView(View):
    def get(self, request):
        register_form = UserRegisterForm()
        return render(request, 'register.html', {'form': register_form})

    def post(self, request):
        register_form = UserRegisterForm(request.POST)
        if not register_form.is_valid():
            return render(request, 'register.html', {'form': register_form})
        register_form.save()
        username = register_form.cleaned_data.get('username')
        messages.success(request, f'User {username} created')
        return redirect('sys-login')


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        update_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        ctx = {
            'update_form': update_form,
            'profile_form': profile_form,
        }
        return render(request, 'profile.html', ctx)

    def post(self, request):
        update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if update_form.is_valid() and profile_form.is_valid():
            update_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('sys-profile')


class ReservationCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = ReservationForm()
        return render(request, 'reservation.html', {'form': form})

    def post(self, request):
        form = ReservationForm(request.POST)
        if form.is_valid():
            now = datetime.datetime.now().time()
            now = int(now.strftime('%H')) + 2
            print(now)
            reservation = Reservation.objects.filter(user=request.user,
                                                     day=form.cleaned_data['day'],
                                                     hour=form.cleaned_data['hour'],
                                                     )
            if reservation:
                messages.error(request, f'Please pick different date or hour')
                return redirect('sys-reservation')
            elif form.cleaned_data['hour'] < now:
                messages.error(request, f"You can't make reservation in the past")
                return redirect('sys-reservation')
            instance = form.save(commit=False)
            instance.user = User.objects.get(id=request.user.id)
            instance.save()
            return redirect('sys-reservation')
        return render(request, 'reservation.html', {'form': form})


class ReservationsView(LoginRequiredMixin, View):
    def get(self, request, ):
        bookings = Reservation.objects.filter(user=request.user)
        return render(request, 'booking.html', {'bookings': bookings})


class ReservationUpdateView(LoginRequiredMixin, View):
    def get(self, request, reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        form = ReservationForm(instance=reservation)
        return render(request, 'reservation.html', {'form': form})

    def post(self, request, reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your reservation has been updated!')
            return redirect('sys-bookings')

        messages.error(request, f'Fill up the form correctly')
        form = ReservationForm(instance=reservation)
        return render(request, 'reservation.html', {'form': form})


class ReservationDeleteView(DeleteView, LoginRequiredMixin):
    model = Reservation
    template_name = 'delete.html'
    success_url = reverse_lazy('sys-bookings')


class AvailabilityView(View):
    def get(self, request):
        today = datetime.datetime.now().date()
        reservations = Reservation.objects.filter(day=today)
        form = AvailabilityForm()
        hours = HOURS



        return render(request, 'availability.html', {'form': form,
                                                     'today': today,
                                                     'hours': hours})


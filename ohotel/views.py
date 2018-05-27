from django.shortcuts import render

# Create your views here.

# =============================
# Added by developer after this
# =============================

import datetime

from .models import Booking
def index(request):
    """View function for index page."""

    template = 'ohotel/index.html'
    context = {}

    return render(request, template, context)

def staff_home(request):
    """View function for staff page."""

    template = 'ohotel/staff_home.html'

    today_check_in_list = Booking.objects.all().filter(
        start_date=datetime.date.today()
    )
    today_check_out_list = Booking.objects.all().filter(
        end_date=datetime.date.today()
    )
    #today_booking_list = Booking.objects.all()

    context = {
        'today_check_in_list': today_check_in_list,
        'today_check_out_list': today_check_out_list,
    }

    return render(request, template, context)

def staff_room(request):
    """View function for staff room page."""

    template = 'ohotel/staff_room.html'

    today_check_in_list = Booking.objects.all().filter(
        start_date=datetime.date.today()
    )
    today_check_out_list = Booking.objects.all().filter(
        end_date=datetime.date.today()
    )
    #today_booking_list = Booking.objects.all()

    context = {
        'today_check_in_list': today_check_in_list,
        'today_check_out_list': today_check_out_list,
    }

    return render(request, template, context)

def check_room_availability(start_date, end_date):
    """Non-view function for checking room availability."""

    room_list = Room.object.all()
    booking_list = Booking.object.all().filter(
        start_date__lte=start_date
    ).filter(
        end_date__gt=start_date
    )
    for room in room_list:
        # if room not in bookin_list
        # return True
        pass

    return false

def make_booking(request):
    """View function for make booking."""

    template = 'ohotel/staff_make_booking.html'

    if request.method == 'POST':
        if form.is_valid():
            # start_date = form.cleaned_data['start_date']
            # end_date = form.cleaned_data['end_date']
            # customer = form.cleaned_data['customer']
            # room = get_room(start_date, end_date)
            # if room is not 'NA':
                # booking = Booking(start_date, end_date, customer, booking_status)
                # return render(request, template, context)
            #
            #
            # 1. Get start_date, end_date, customer, number_of_people from
            #    the form.  
            # 2. Check if room is available in that date
            # 3. Create a booking object if room available
            # 4. Save the booking object to database
            #
            #
            pass
    else:
        form = BookingFormStaff();

    context = {
        'form': form,
    }

    return render(request, template, context)


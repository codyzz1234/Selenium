import time
from booking.booking import Booking
from booking.constants import BASE_URL


with Booking() as bot:
    bot.land_first_page();
    print('Exiting...')
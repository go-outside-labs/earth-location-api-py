# -*- encoding: utf-8 -*-
# api/methods.py

import pytz
import datetime
import timezonefinder
from geopy.geocoders import Nominatim


def _find_timezone_name(lat, lon) -> str:

    tf = timezonefinder.TimezoneFinder()
    timezone = tf.certain_timezone_at(lat=lat, lng=lon)

    if not timezone:
        timezone = 'America/New_York'
        print(f'Could not find timezone for {lat}-{lon}. Setting {timezone}')

    return timezone


def _find_timezone(lat, lon) -> int:

    tzone = _find_timezone_name(lat, lon)
    timezone_delta = datetime.datetime.now(pytz.timezone(tzone)).strftime('%z')

    return int(timezone_delta[:-2])


def get_location(city) -> dict:

    geolocator = Nominatim(user_agent="go-outside")
    location = geolocator.geocode(city)

    data = {
        'latitude': location.latitude,
        'longitude': location.longitude,
        'timezone': _find_timezone(float(location.latitude),
                                            float(location.longitude))
    }

    return data

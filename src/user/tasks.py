import requests
from celery import shared_task
from django.db import IntegrityError

from config.secrets import ABSTRACT_API_API_KEY

from .models import UserGeolocation


@shared_task
def fetch_ip_geolocation_data(ip_address):
    try:
        response = requests.get(
            f"https://ipgeolocation.abstractapi.com/v1/?api_key={ABSTRACT_API_API_KEY}&ip_address={ip_address}"
        )
        data = response.json()

        # Perform any necessary data validation on the response
        if "ip_address" not in data:
            raise ValueError("Invalid response: missing 'ip_address' field")

        # Create a UserGeolocation instance and populate the fields
        geolocation = UserGeolocation()
        geolocation.ip_address = data["ip_address"]
        geolocation.city = data["city"]
        geolocation.country_code = data["country_code"]
        geolocation.city_geoname_id = data["city_geoname_id"]
        # Populate other fields as needed

        # Save the UserGeolocation instance
        geolocation.save()

        # If everything goes well, call fetch_holiday_data() async to save data into holiday_data_model
        # fetch_holiday_data.delay(country_code, year, month, day)

        # Add another task to async store holiday data
    except (
        requests.RequestException,
        ValueError,
        IntegrityError,
    ) as e:
        # Should schedule for a retry here into a specific queue for retries that gets dequeued  multiple times a day
        print(
            f"An error occurred while fetching or saving geolocation data: {str(e)}"
        )


@shared_task
def fetch_holiday_data(country_code, year, month, day):
    pass
    # response = requests.get(
    #     f"https://holidays.abstractapi.com/v1/?api_key=77ccca00b3e94b1db5daa5dfa4caa714&country={country_code}&year={year}&month={month}&day={day}"
    # )

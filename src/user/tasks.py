from celery import shared_task


@shared_task
def fetch_ip_geolocation_data(ip_address):
    pass

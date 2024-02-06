import schedule
import time
import requests
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Keep the backend alive by sending periodic requests'

    def handle(self, *args, **options):
        # Define the endpoint to send periodic requests to
        endpoint_url = 'https://portfolio-backend-fdxe.onrender.com'

        # Define the interval for sending requests (in seconds)
        interval_seconds = 300  # 5 minutes

        # Define the function to send the request
        def send_keep_alive_request():
            try:
                response = requests.get(endpoint_url)
                response.raise_for_status()
                print(f"Keep-alive request sent successfully: {response.status_code}")
            except Exception as e:
                print(f"Error sending keep-alive request: {e}")

        # Schedule the periodic request
        schedule.every(interval_seconds).seconds.do(send_keep_alive_request)

        # Run the scheduler
        while True:
            schedule.run_pending()
            time.sleep(1)

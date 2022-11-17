from datetime import date


from requests import get
from requests import Response


class OnThisDayAPIWrap:
    """
    This class encapsulate interaction to 'on this day'
    wikimedia api use https://byabbe.se/on-this-day/
    REST-API
    """

    def __init__(self):
        self.url = 'https://byabbe.se/on-this-day'

    def get_fact_about_day(self, month: int, day: int) -> Response:
        """
        Returns response of 'on this day' service, that
        contains json-object with events list corresponding
        required month and day
        :param int month: required month
        :param int day: required day
        :return requests.Response: answer of service
        """
        return get(url=f'{self.url}/{month}/{day}/events.json')

    def get_fact_about_today_day(self) -> Response:
        """
        Returns response of 'on this day' service, that
        contains json-object with events list corresponding
        required current day
        :return requests.Response: answer of service
        """
        current_day = date.today()
        return self.get_fact_about_day(month=current_day.month, day=current_day.day)

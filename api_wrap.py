from datetime import date


from requests import get

from models import WikipediaOnThisDay
from marshmallow_schemas import WikipediaOnThisDaySchema


class OnThisDayAPIWrap:
    """
    This class encapsulate interaction to 'on this day'
    wikimedia api use https://byabbe.se/on-this-day/
    REST-API
    """

    def __init__(self):
        self.url = 'https://byabbe.se/on-this-day'

    def get_fact_about_day(self, month: int, day: int) -> WikipediaOnThisDay:
        """
        Returns the model represents of 'on this day' service, by
        required month and day
        :param int month: required month
        :param int day: required day
        :return models.WikipediaOnThisDay on_this_day_model: answer of service
        """
        response = get(url=f'{self.url}/{month}/{day}/events.json')
        on_this_day_model = WikipediaOnThisDaySchema().load(response.json())
        return on_this_day_model

    def get_fact_about_today_day(self) -> WikipediaOnThisDay:
        """
        Returns the model represents of 'on this day' service, by
        required current day
        :return models.WikipediaOnThisDay: answer of service
        """
        current_day = date.today()
        return self.get_fact_about_day(month=current_day.month, day=current_day.day)

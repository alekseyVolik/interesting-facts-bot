from datetime import date


from requests import get

from models import WikipediaOnThisDay
from marshmallow_schemas import WikipediaOnThisDaySchema


class OnThisDayAPIWrap:
    """
    This class encapsulate interaction to 'on this day'
    wikimedia api use https://api.wikimedia.org/wiki/API_reference/Feed/On_this_day
    REST-API
    """

    def __init__(self):
        self.url = 'https://api.wikimedia.org'

    def get_fact_about_day(self, month: int, day: int) -> WikipediaOnThisDay:
        """
        Returns the model represents of 'on this day' events, by
        required month and day. Day and month will be padded to
        required parameter
        :param int month: required month
        :param int day: required day
        :return models.WikipediaOnThisDay on_this_day_model: answer of service
        """
        _lang, _type = 'ru', 'events'
        month, day = f'{month:0>2d}', f'{day:0>2d}'
        response = get(url=f'{self.url}/feed/v1/wikipedia/{_lang}/onthisday/{_type}/{month}/{day}')
        on_this_day_model = WikipediaOnThisDaySchema().load(response.json())
        return on_this_day_model

    def get_fact_about_today_day(self) -> WikipediaOnThisDay:
        """
        Returns the model represents of 'on this day' events, by
        required current day
        :return models.WikipediaOnThisDay: answer of service
        """
        current_day = date.today()
        return self.get_fact_about_day(month=current_day.month, day=current_day.day)

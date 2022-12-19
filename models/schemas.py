from marshmallow import Schema, fields, post_load, EXCLUDE

from models.models import (
    WikipediaOnThisDay, WikipediaEvents
)


class WikipediaOnThisDaySchema(Schema):
    events = fields.List(fields.Nested('WikipediaEventSchema'))

    @post_load
    def make_wikipedia_on_this_day(self, data, **kwargs) -> WikipediaOnThisDay:
        return WikipediaOnThisDay(**data)

    class Meta:
        unknown = EXCLUDE


class WikipediaEventSchema(Schema):
    text = fields.Str()
    year = fields.Int()

    @post_load
    def make_wikipedia_event(self, data, **kwargs) -> WikipediaEvents:
        return WikipediaEvents(**data)

    class Meta:
        unknown = EXCLUDE

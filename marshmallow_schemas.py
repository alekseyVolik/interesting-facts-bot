from marshmallow import Schema, fields, post_load


from models import (
    WikipediaOnThisDay, WikipediaEvent, WikipediaLink
)


class WikipediaOnThisDaySchema(Schema):
    date = fields.Str()
    wikipedia = fields.Str()
    events = fields.List(fields.Nested('WikipediaEventSchema'))

    @post_load
    def make_wikipedia_on_this_day(self, data, **kwargs) -> WikipediaOnThisDay:
        return WikipediaOnThisDay(**data)


class WikipediaEventSchema(Schema):
    year = fields.Str()
    description = fields.Str()
    wikipedia = fields.List(fields.Nested('WikipediaLinkSchema'))

    @post_load
    def make_wikipedia_event(self, data, **kwargs) -> WikipediaEvent:
        return WikipediaEvent(**data)


class WikipediaLinkSchema(Schema):
    title = fields.Str()
    wikipedia = fields.Str()

    @post_load
    def make_wikipedia_link(self, data, **kwargs) -> WikipediaLink:
        return WikipediaLink(**data)

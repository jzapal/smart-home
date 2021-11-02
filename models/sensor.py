import mongoengine as me


class Sensor(me.Document):
    name = me.StringField(required=True)

import mongoengine as me

from models.sensor import Sensor


class Measurement(me.Document):
    value = me.FloatField()
    sensor = me.ReferenceField(Sensor, reverse_delete_rule=me.CASCADE)

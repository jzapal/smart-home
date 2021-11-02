import factory

import models


class SensorFactory(factory.mongoengine.MongoEngineFactory):
    class Meta:
        model = models.Sensor

    name = factory.Faker('name')

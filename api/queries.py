import typing

import strawberry

import models
from api import types


@strawberry.type
class Query:
    @strawberry.field
    def sensors(self) -> typing.List[types.Sensor]:
        return models.Sensor.objects.all()

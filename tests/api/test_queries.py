from api import schema
from tests.factories.sensor import SensorFactory


def test_query(database_mock):
    SensorFactory.create_batch(2)
    query = """
        query Sensors {
            sensors {
                name
            }
        }
    """

    result = schema.execute_sync(
        query
    )

    assert result.errors is None
    assert len(result.data["sensors"]) == 2

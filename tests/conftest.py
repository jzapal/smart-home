import pytest
from mongoengine import connect
from mongoengine import disconnect


@pytest.fixture(scope='function')
def database_mock():
    db_name = 'sh_test'
    disconnect()
    connection = connect(db_name, host='mongomock://localhost')
    yield connection
    connection.drop_database(db_name)

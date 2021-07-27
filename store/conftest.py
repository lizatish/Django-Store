import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import NullPool

from store import db, create_app


@pytest.fixture()
def engine(postgresql):
    connection = f'postgresql+psycopg2://postgres:@{postgresql.info.host}:{postgresql.info.port}/{postgresql.info.dbname}'
    return create_engine(connection, echo=False, poolclass=NullPool)


@pytest.fixture()
def tables(engine):
    db.Model.metadata.create_all(engine)
    yield
    db.Model.metadata.drop_all(engine)


@pytest.fixture
def dbsession(engine, tables):
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)

    yield session

    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()


@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()

    # Commit the changes for the users
    db.session.commit()

    yield db  # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope='function')
def test_client(postgresql):
    connection = f'postgresql+psycopg2://postgres:@{postgresql.info.host}:{postgresql.info.port}/{postgresql.info.dbname}'
    engine = create_engine(connection, echo=False, poolclass=NullPool)
    db.Model.metadata.create_all(engine)

    class TestC(object):
        TESTING = True
        SQLALCHEMY_DATABASE_URI = connection
        SQLALCHEMY_TRACK_MODIFICATIONS = False

    flask_app = create_app(TestC)
    # Flask provides a way to test your appli ation by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()

    # Establish an application context before running the tests.
    ctx = flask_app.app_context()

    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()
    db.Model.metadata.drop_all(engine)

#
# @pytest.fixture
# def app():
#     yield flask_app


# @pytest.fixture
# def client(app):
#     return app.test_client()

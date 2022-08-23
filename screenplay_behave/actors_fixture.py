from behave import fixture
from .actors import Actors


@fixture
def actors_fixture(context):
    context.actors = Actors()
    type(context).they = property(lambda self: self.actors.active)
    yield context.actors
    context.actors.clean_up()

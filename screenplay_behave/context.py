from .actors import Actors


def add_screenplay_objects_to(context):
    context.actors = Actors()
    type(context).they = property(lambda self: self.actors.active)

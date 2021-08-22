from screenplay_behave import Actors, add_screenplay_objects_to
from screenplay import Actor

from .stub_abilities import StubAbility


class Context:
    pass


def test_An_Actors_object_is_added_to_a_context():
    context = Context()

    add_screenplay_objects_to(context)

    assert isinstance(context.actors, Actors)


def test_The_they_Actor_object_is_added_to_a_context():
    context = Context()

    add_screenplay_objects_to(context)

    context.actors.add_person_called('Simon')
    context.actors.switch_active('Simon')

    assert isinstance(context.they, Actor)


def test_Ability_objects_can_be_added_to_Actors_easily():
    context = Context()

    add_screenplay_objects_to(context)

    context.actors.add_person_called('Simon').who_can(StubAbility())


def test_The_Ability_objects_of_all_Actor_objects_are_cleaned_up_when_the_Actors_object_is_cleaned():
    context = Context()

    add_screenplay_objects_to(context)

    ability1 = StubAbility()
    ability2 = StubAbility()

    context.actors.add_person_called('Simon').who_can(ability1)
    context.actors.add_person_called('Jeremy').who_can(ability2)

    context.actors.clean_up()

    assert ability1.clean_up_run, 'Ability was not cleaned up when the Actors object was cleaned up'
    assert ability2.clean_up_run, 'Ability was not cleaned up when the Actors object was cleaned up'

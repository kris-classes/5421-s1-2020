"""
ISCG5421 S1 2020 Practical Test Solutions for Questions B & C
    by Kris Pritchard / @krisrp

Learning Outcomes covered by this test:
1. Implement the designs by writing well-structured programs that follow
      enforced programming language conventions and programming standards.
2. Identify the fundamental data requirements of an intermediate-level program.
3. Apply the logic structures of the language.
4. Select and use intermediate-level data structures

This is a module docstring for pylint.
Run tests with pytest -v contact_tracer.py
"""

# Disabling a few of pylint's pedantic settings for this test.
# pylint: disable=unnecessary-pass,protected-access,line-too-long
import datetime
import pytest  # Uses unittest or pytest module  [1 mark]


# Question B - Implementation [20 marks]
class InvalidLocation(Exception):  # Correct InvalidLocation exception: [2 marks]
    """Custom exception"""
    pass


class Person:
    """Person class for contact tracer"""

    def __init__(self, email):  # Correct __init__ method: [3 marks]
        # We can represent private fields with an _ prefix.
        self._email = email

        # We want to store the date/time a person last visited a location.
        self.last_visit_at = datetime.datetime.now()

        # We want to keep track of locations, so we use a set.
        self.locations = set()


    def visit(self, location_id):  # Correct visit method: [4 marks]
        """Adds location id to the set of visited locations"""

        if location_id < 0:
            raise InvalidLocation('Invalid Location')

        self.locations.add(location_id)
        self.last_visit_at = datetime.datetime.now()


    def has_contact(self, other_person):  # Correct has_contact method: [6 marks]
        """
        Compares the visited location of each person.
        Returns True if they've visited the same location.

        NOTE: Ilya had a cool 1-line solution for this:
            return bool(self.locations & other_person.locations)
        """
        # This is why choosing the right data structure is extremely important.
        # It just needs 1 line of code if using a set.
        if self.locations.intersection(other_person.locations):
            return True
        return False


    def _notify(self):  # Correct notify method: [1 mark]
        """Notify a user when this method is called."""
        return f'Notifying user {self._email.upper()}'


    def num_locations_visited(self):  # Correct num_locations_visited method: [1 mark]
        """Returns the number of visited locations"""
        return len(self.locations)


# Passes pylint conventions with 10/10: [3 marks]


# Question C - Tests [15 marks]
# Run these with pytest -v contact_tracer.py
def test_visit_adds_location_id_to_locations():  # Correct visit test #1: [2 marks]
    """Test that visit adds a location id to locations"""
    person = Person('person@gmail.com')
    person.visit(1)
    assert 1 in person.locations


def test_visit_raises_invalidlocation_if_location_id_lt_zero():  # Correct visit test #2: [2 marks]
    """Test that visiting invalid location id raises exception"""
    person = Person('person@gmail.com')
    with pytest.raises(InvalidLocation):
        person.visit(-1)


def test_no_visits_has_num_locations_of_zero():  # Correct num_locations_visited test #1: [2 marks]
    """Tests if a person makes no visits then their visit count is 0"""
    person = Person('person@gmail.com')
    assert person.num_locations_visited() == 0


def test_one_visit_has_num_locations_of_one():  # Correct num_locations_visited test #2: [2 marks]
    """Test if a person visits a location then that visit is counted"""
    person = Person('person@gmail.com')
    person.visit(123)
    assert person.num_locations_visited() == 1


def test_has_contact_for_contacted_users_returns_true():  # Correct has_contact test #1: [2 marks]
    """Tests if two people who visited the same locations had contact"""
    person1 = Person('person1@gmail.com')
    person2 = Person('person2@gmail.com')
    person1.visit(1)
    person1.visit(2)
    person2.visit(4)
    person2.visit(2)
    assert person1.has_contact(person2)  # Equivalent to person1.has_contact(person2) == True


def test_contact_for_two_people_without_contact_returns_false():  # Correct has_contact test #2: [2 marks]
    """Tests if two people who visited different locations have had contact"""
    person1 = Person('person1@gmail.com')
    person2 = Person('person2@gmail.com')
    person1.visit(1)
    person1.visit(2)
    person2.visit(4)
    person2.visit(5)
    assert not person1.has_contact(person2)  # Equivalent to person1.has_contact(person2) == False


def test_notify_person_returns_persons_email_address_in_uppercase():  # Correct notify test: [2 marks]
    """Tests if _notify returns uppercase email address"""
    person = Person('person@gmail.com')
    assert person._notify() == 'Notifying user PERSON@GMAIL.COM'

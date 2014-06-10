"""

Sample Business Objects
-----------------------

We want to show how things can  be organized with `Resto`. That's why we
have this separate module which  represents your business objects.  They
can access database  layer directly or rely on other  objects. That's up
to you decide about  your system design. What needs to  be clear is that
`Resto` should work really just as a bridge.

"""

import datetime


class Teacher(object):
    """Represents and manipulates a teacher object."""

    @classmethod
    def delete(cls, id):
        """Removes an object from store."""
        pass

    @classmethod
    def load(cls, id):
        """Loads teacher object from store."""
        new_obj = Teacher()
        new_obj.id = id
        new_obj.name = 'Rafael Pivato'
        new_obj.birthdate = datetime.datetime.now()
        return new_obj

    def save():
        """Saves a teacher object to the store."""
        new_obj.id = 1

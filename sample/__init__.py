"""

Sample Resto Application
------------------------

This sample  application is  what will  motivate initial  development of
Resto library. Intention here is  to understand pratical aplicability of
concepts implemented  so far.  More than that,  it serves  as guidelines
about how features will be implemented.

"""

import resto

import business


class Teacher(resto.Resource):
    """A teacher from our school."""

    id = resto.IntegerField('identifier for teacher')
    name = resto.StringField('name for the teacher')
    birthdate = resto.StringField('date of birth')

    def get(self, id):
        """Gets information about a given teacher."""
        loaded = business.Teacher.load(id)
        if not loaded:
            raise resto.NotFoundError()
        else:
            self.id = loaded.id
            self.name = loaded.name
            self.birthdate = loaded.birthdate

    def put(self, id):
        """Stores information about a given teacher."""
        loaded = business.Teacher.load(id)
        if not loaded:
            raise resto.NotFoundError()
        else:
            loaded.name = self.name
            loaded.birthdate = loaded.birthdate
            loaded.save()

    def post(self):
        """Adds new teacher to the collection."""
        created = business.Teacher()
        created.name = self.name
        created.birthdate = self.birthdate
        create.save()

    def delete(self, id):
        """Deltes a teacher from the collection."""
        business.Teacher.delete(id)

from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # instantiate the form with empty name
        # simulating user not filling out the name
        form = ItemForm({'name': ''})

        # test that form is not valid
        self.assertFalse(form.is_valid())

        # error occurred on the name field
        self.assertIn('name', form.errors.keys())

        # display error message
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    # assert that if item model (forms.py) is changed in the future,
    # the form won't display other fields rather than name and done
    def test_fields_are_explicit_in_form_metaclass(self):
        # instantiate empty form
        form = ItemForm()
        # assert that only name and done are displayed
        self.assertEqual(form.Meta.fields, ['name', 'done'])


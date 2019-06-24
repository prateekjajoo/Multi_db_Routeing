from django.forms import ModelForm
from .models import UserRole, Product
from django import forms

Database_choices = (
    ('database1', 'Database1'),
    ('database2', 'Database2'),
    ('database3', 'Database3'),
    ('database4', 'Database4'),
    ('database5', 'Database5'),
)


class UserRoleForm(ModelForm):
    """ User form overwite password field for password input and db_assign for list of database """
    password = forms.CharField(widget=forms.PasswordInput)
    db_assign = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=Database_choices,)

    class Meta:
        model = UserRole
        fields = ['first_name', 'last_name', 'username', 'password', 'db_assign']


class ProductForm(ModelForm):
    """ Product Form """
    class Meta:
        model = Product
        exclude = ['user']

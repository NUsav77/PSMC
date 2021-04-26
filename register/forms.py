from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
import SavBlock.models
from SavBlock.models import *

''' Form for users to register '''


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        initial='',
        required=True,
        help_text='Please enter a valid email address'
    )

    '''
    rank = forms.ChoiceField(
        label='Are you a PSMC member?',
        choices=SavBlock.models.User.rank,
        initial=False,
        required=True,
        help_text='Member accounts will be validated with your HC.',
    )
    '''

    class Meta:
        model = User
        # username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password1', 'password2']  # 'rank',

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        # User.ranking = self.cleaned_data['rank']
        if commit:
            user.save()
        return user


'''
class AnakRegisterForm(UserCreationForm):
    tribe = forms.ChoiceField(
        label='What tribe are you from, Uce?',
        choices=SavBlock.models.Anak.tribe,
        initial=False,
        required=True,
        help_text='Member accounts will be validated with your HC.'
    )

    class Meta:
        model = Anak
        fields = ['tribe']

    def save(self, commit=True):
        user = super(AnakRegisterForm, self).save(commit=False)
        user.tribe = self.cleaned_data['tribe']
        if commit:
            user.save()
        return user

class UsoRegisterForm(AuthenticationForm):
    pass


class ChiefRegisterForm(AuthenticationForm):
    pass
'''

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, AnakRegisterForm, UsoRegisterForm, ChiefRegisterForm
from formtools.wizard.views import SessionWizardView


# Create your views here.
def register(response):
    context = {}
    temp_key = {}
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            if form.cleaned_data.get('rank') == 'Anak':
                temp_key[form.cleaned_data.get('username')] = form.cleaned_data
                return redirect('anak_register')
                # anak_register(form.cleaned_data)

            messages.success(response, 'Registration successful. Please login.')
            return redirect('login')
        else:
            context['register'] = form
    else:
        form = RegisterForm()
        context['register'] = form

    return render(request=response, template_name='register/register.html', context={'form': form})


def coming_soon(coming_soon):
    return render(coming_soon, 'coming-soon.html')


def anak_register(response):
    context = {}
    if response.method == 'POST':
        anak_form = AnakRegisterForm(response.POST)
        if anak_form.is_valid():
            # TODO: The form obtains the tribe information from the user. Now we must save this information into the
            #  users account.


            """
            anak_form = RegisterForm.save(register)
            return anak_form
            """
        else:
            context['register'] = anak_form

        render(request=response, template_name='register/register.html', context={'form': anak_form})

    else:
        anak_form = AnakRegisterForm(response.POST)
        context['anak_register'] = anak_form
        # messages.error(request, 'Unsuccessful registration. Invalid information.')

    return render(request=response, template_name='register/anak_register.html', context={'form': anak_form})

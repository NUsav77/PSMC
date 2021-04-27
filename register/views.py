from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm  # AnakRegisterForm, UsoRegisterForm, ChiefRegisterForm
from formtools.wizard.views import SessionWizardView

# Create your views here.
def register(response):
    context = {}
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            '''
            rank = form.cleaned_data.get('rank')
            if rank == 'Anak':
                anak_register(response.POST)
                # anak_register(form.cleaned_data)
                '''

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




'''
def anak_register(anak_response):
    context = {}
    if anak_response.method == 'POST':
        anak_form = AnakRegisterForm(anak_response)
        if anak_form.request.is_valid():
            anak_form.save()
            messages.success(anak_response, 'Registration successful. Please login.')
            return redirect('login')
        else:
            context['register'] = anak_form

    render(request=anak_response, template_name='register/register.html', context={'form': anak_form})

    else:
        form = AnakRegisterForm()
        context['register'] = form
        # messages.error(request, 'Unsuccessful registration. Invalid information.')

    form = RegisterForm

    return render(request=anak_response, template_name='register/register.html', context={'form': form})
'''

from django.shortcuts import render
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
from common import utils
from .forms import SignupForm
from .forms import ConfirmForm


def signup(request):
    if request.method != 'POST':
        form = SignupForm()
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            # get new secret
            secret = utils.get_secret()
            request.session['user_id'] = form.cleaned_data['user_id']
            request.session['password'] = form.cleaned_data['password']
            request.session['secret'] = secret
            # get QR-code image
            request.session['img'] = utils.get_image_b64(utils.get_auth_url(form.cleaned_data['user_id'], secret))
            return redirect('confirm_token')

    return render(request, 'input.html', {'form': form})


def confirm_token(request):
    if request.method != 'POST':
        form = ConfirmForm()
    else:
        form = ConfirmForm(request.POST)
        form.secret = request.session['secret']
        if form.is_valid():
            return redirect('signup_success')

    return render(request, 'confirm_token.html', {'form': form})


def success(request):
    return render(request, 'signup_success.html')

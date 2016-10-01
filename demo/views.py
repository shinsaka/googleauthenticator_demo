from django.shortcuts import render
from . import utils


def index(request):
    user_id = 'GoogleAuthenticateDemo@example.com'
    secret = utils.get_secret()
    request.session['secret'] = secret
    request.session['img'] = utils.get_image_b64(utils.get_auth_url(user_id, secret))

    return render(request, 'index.html')


def get_otpcode(request):
    return render(request, 'get_otpcode.html', {'token': utils.get_token(request.session['secret'])})

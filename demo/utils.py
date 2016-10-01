import string
import base64
from io import BytesIO
from django.utils.crypto import get_random_string
import qrcode
import onetimepass as otp


def get_secret(length=10):
    """
    generate new secret
    """
    return base64.b32encode(
        get_random_string(
            length=length,
            allowed_chars=string.ascii_letters + string.digits
        ).encode()
    ).decode()


def get_auth_url(user_id, secret, issuer='DemoSite'):
    """
    otp auth url
    """
    url_template = 'otpauth://totp/{isr}:{uid}?secret={secret}&issuer={isr}'
    return url_template.format(
        uid=user_id,
        secret=secret,
        isr=issuer)


def get_image_b64(url):
    """
    generate QR-code image (base64-text)
    """
    qr = qrcode.make(url)
    img = BytesIO()
    qr.save(img)
    return base64.b64encode(img.getvalue()).decode()


def get_token(secret):
    return otp.get_totp(secret)

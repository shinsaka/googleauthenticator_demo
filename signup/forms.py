from django import forms
import onetimepass as otp


class SignupForm(forms.Form):
    user_id = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)


class ConfirmForm(forms.Form):
    otp_code = forms.CharField(max_length=6, min_length=6, widget=forms.NumberInput)
    secret = None

    def clean_otp_code(self):
        otp_code = self.cleaned_data['otp_code']
        if not otp.valid_totp(otp_code, self.secret):
            raise forms.ValidationError('Code is invalid.')

        return otp_code

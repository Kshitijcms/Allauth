from allauth.account.forms import LoginForm, SignupForm,ResetPasswordForm,ChangePasswordForm


def style_fields(form):
    for name, field in form.fields.items():
        if name == "remember":
            css_class = "checkbox checkbox-primary"
        else:
            css_class = "input input-bordered w-full"

        # Password fields ke liye autocomplete browser ko allow rahega
        field.widget.attrs.update({
            "class": css_class,
            "placeholder": field.label,
        })


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)
        
class CustomResetPasswordForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)
        
class CustomChangePasswordForm(ChangePasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_fields(self)
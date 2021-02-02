from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views.decorators import user_passes_test

def superuser_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url={% url 'login' %}):
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=REDIRECT_FIELD_NAME
    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
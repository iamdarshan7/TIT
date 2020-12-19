from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_number(value):
    if len(value) != 10:
        raise ValidationError(
            _('Invalid Phone Number.'),
            params={'value': value},
        )

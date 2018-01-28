from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )



CATEGORIES = ['African, Asian, American']

def validate_category(value):
	

	cat = value.capitalize()  # accept any form
	if not value in CATEGORIES :
		raise ValidationError(" not a valid category" )


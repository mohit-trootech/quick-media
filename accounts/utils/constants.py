from django.utils.translation import gettext_noop as _

# Models Constants
MALE_CODE = "M"
FEMALE_CODE = "F"
MALE_VALUE = _("Male")
FEMALE_VALUE = _("Female")
GENDER_CHOICE = ((MALE_CODE, MALE_VALUE), (FEMALE_CODE, FEMALE_VALUE))

PROFILE_UPLOAD_TO = "profile"

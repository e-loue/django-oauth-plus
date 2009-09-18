from django.utils.translation import ugettext_lazy as _

KEY_SIZE = 16
SECRET_SIZE = 16
VERIFIER_SIZE = 10
CONSUMER_KEY_SIZE = 256

PENDING = 1
ACCEPTED = 2
CANCELED = 3
REJECTED = 4

CONSUMER_STATES = (
    (PENDING,  _('Pending')),
    (ACCEPTED, _('Accepted')),
    (CANCELED, _('Canceled')),
    (REJECTED, _('Rejected')),
)

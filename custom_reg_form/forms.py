from .models import ExtraInfo
from django.forms import ModelForm


class ExtraInfoForm(ModelForm):
    """
    The fields on this form are derived from the ExtraInfo model in models.py.
    """

    def __init__(self, *args, **kwargs):
        super(ExtraInfoForm, self).__init__(*args, **kwargs)
        self.fields["favorite_movie"].error_messages.update(
            {
                "required": "Please tell us your favorite movie.",
                "invalid": "We're pretty sure you made that movie up.",
            }
        )
        self.fields["favorite_movie"].help_text = "Please tell us your favorite movie."

        self.fields["data_authorization"].error_messages = {
            "required": "Please authorize data processing"
        }

    class Meta(object):
        model = ExtraInfo
        fields = [
            "data_authorization",
            "favorite_movie",
            "employment_situation",
            "allow_newsletter",
        ]

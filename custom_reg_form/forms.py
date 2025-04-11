from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from .models import ExtraInfo


# According to edx-platform FormDescription
#
# https://github.com/fccn/edx-platform/blob/315ca44d10d47bf4e16f0c916295c70939cf27e1/openedx/core/djangoapps/user_api/helpers.py#L95
#
# ALLOWED_TYPES = ["text", "email", "select", "textarea", "checkbox", "plaintext", "password", "hidden"]
#
# ALLOWED_RESTRICTIONS = {
#     "text": ["min_length", "max_length"],
#     "password": ["min_length", "max_length", "min_upper", "min_lower",
#                     "min_punctuation", "min_symbol", "min_numeric", "min_alphabetic"],
#     "email": ["min_length", "max_length", "readonly"],
# }
#
# FIELD_TYPE_MAP = {
#     forms.CharField: "text",
#     forms.PasswordInput: "password",
#     forms.ChoiceField: "select",
#     forms.TypedChoiceField: "select",
#     forms.Textarea: "textarea",
#     forms.BooleanField: "checkbox",
#     forms.EmailField: "email",
# }
class ExtraInfoForm(ModelForm):
    """
    Form that represents user extra info and is compatible with edX's FormDescription system.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Example: text field with restrictions
        self.fields["full_name"].help_text = "Enter your full name."
        self.fields["full_name"].min_length = 3
        self.fields["full_name"].max_length = 100
        self.fields["full_name"].required = True
        self.fields["full_name"].restrictions = {
            "min_length": 3,
            "max_length": 100,
        }

        # Textarea field
        self.fields["bio"].widget = forms.Textarea()
        self.fields["bio"].help_text = "Write a short bio."
        self.fields["bio"].field_type = "textarea"
        self.fields["bio"].required = True
        self.fields["bio"].error_messages = {
            "required": "Please tell us something about yourself",
        }

        # Checkbox
        self.fields["wants_newsletter"].label = "Subscribe to newsletter?"

        # Select field
        self.fields["favorite_language"].help_text = (
            "Pick your preferred programming language."
        )

        # Plaintext hint
        self.fields["password_hint"].help_text = (
            "This will help you remember your password."
        )
        self.fields["password_hint"].placeholder = "Insert a hint"
        self.fields["password_hint"].min_length = 5
        self.fields["password_hint"].max_length = 10
        self.fields["password_hint"].required = True
        self.fields["password_hint"].error_messages = {
            "required": "Insert a hint for your password",
            "min_length": "Hint is too short",
            "max_length": "Hint is too long",
        }

        # Checkbox with custom message
        self.fields["data_authorization"].error_messages = {
            "required": "Please authorize data processing.",
        }

        # Agreement checkbox
        self.fields["terms_accepted"].label = "I accept the Terms and Conditions"
        self.fields["terms_accepted"].required = True
        
        self.fields["favorite_language"].required = True

    class Meta:
        model = ExtraInfo
        fields = [
            "data_authorization",
            "full_name",
            "bio",
            "wants_newsletter",
            "favorite_language",
            "password_hint",
            "terms_accepted",
        ]

        # According to edx-platform RegistrationFormFactory
        #
        # https://github.com/fccn/edx-platform/blob/315ca44d10d47bf4e16f0c916295c70939cf27e1/openedx/core/djangoapps/user_authn/views/registration_form.py#L457-L458
        #
        # here you have to use the same names as in the model and you can add default,
        # field_type and include_default_option
        serialization_options = {
            "password_hint": {
                "default": "Funny Password",
            },
        }

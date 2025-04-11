from django.conf import settings
from django.db import models
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    RegexValidator,
    EmailValidator,
)
from django.utils.translation import gettext_lazy as _

USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")


class ExtraInfo(models.Model):
    """
    Enhanced model with additional fields demonstrating various field types and restrictions.
    Fields are compatible with edx-platform FormDescription configuration.
    """

    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.CASCADE)

    data_authorization = models.BooleanField(
        verbose_name=_(
            "I have read and understood the <a href='https://www.nau.edu.pt/legal/politica-de-privacidade/'"
            " rel='noopener' target='_blank'>Privacy Policy</a>"
        )
    )

    full_name = models.CharField(
        blank=True,
        max_length=255,
        validators=[MinLengthValidator(2)],
        verbose_name=_("Full name"),
    )

    bio = models.TextField(
        blank=True,
        verbose_name=_("Biography"),
        help_text=_("Tell us a bit about yourself."),
    )

    wants_newsletter = models.BooleanField(
        default=False,
        verbose_name=_("Subscribe to newsletter"),
    )

    favorite_language = models.CharField(
        blank=True,
        max_length=50,
        choices=[
            ("python", "Python"),
            ("javascript", "JavaScript"),
            ("java", "Java"),
            ("go", "Go"),
        ],
        verbose_name=_("Favorite programming language"),
    )

    password_hint = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_("Password hint"),
        help_text=_("Optional hint to remember your password."),
    )

    terms_accepted = models.BooleanField(
        default=False,
        verbose_name=_("I accept the Terms and Conditions."),
    )

    registration_token = models.CharField(
        blank=True,
        max_length=64,
        editable=False,
        verbose_name=_("Registration token (internal)"),
    )

    def __str__(self):
        return f"{self.full_name} <{self.email}>"

    class Meta:
        verbose_name = _("Extra Info")
        verbose_name_plural = _("Extra Info entries")

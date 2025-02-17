from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """

    STUDENT = "Student"
    UNEMPLOYED = "Unemployed"
    PUBLIC_SERVICE_CONTRACT = "Public service contract"
    PRIVATE_INSTITUTION_CONTRACT = "Private institution contract"
    SELF_EMPLOYED = "Self employed entrepreneur"
    OTHER = "Other"

    EMPLOYMENT_SITUATION_CHOICES = [
        (STUDENT, "Student"),
        (UNEMPLOYED, "Unemployed"),
        (PUBLIC_SERVICE_CONTRACT, "Public service contract"),
        (PRIVATE_INSTITUTION_CONTRACT, "Private institution contract"),
        (SELF_EMPLOYED, "Self employed entrepreneur"),
        (OTHER, "Other"),
    ]

    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.CASCADE)

    data_authorization = models.BooleanField(
        verbose_name="I have read and understood the <a href='https://www.nau.edu.pt/legal/politica-de-privacidade/'"
        "rel='noopener' target='_blank'>Privacy Policy</a>",
    )

    favorite_movie = models.CharField(verbose_name="Fav Flick", max_length=100)

    employment_situation = models.TextField(
        verbose_name="Employment situation",
        choices=EMPLOYMENT_SITUATION_CHOICES,
    )

    allow_newsletter = models.BooleanField(
        verbose_name="I have read and agree to give my <a target='_blank' "
        "href='https://www.nau.edu.pt/legal/consentimento-para-o-envio-de-"
        "newsletters/'>consent to the sending of newsletters</a>",
    )

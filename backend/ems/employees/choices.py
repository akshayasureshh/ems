from django.db import models


class FieldTypes(models.TextChoices):
    TEXT = "text", "Text"
    NUMBER = "number", "Number"
    DATE = "date", "Date"
    PASSWORD = "password", "Password"

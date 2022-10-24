from enum import unique
from unittest.util import _MAX_LENGTH
from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

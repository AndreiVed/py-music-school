from django.db import models
from rest_framework.exceptions import ValidationError


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField()
    date_of_applying = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self):
        return True if self.age >= 21 else False

    def clean(self):
        if self.age < 14:
            raise ValidationError(
                f"Your age is {self.age}, "
                f"we do not accept people who are under 14"
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

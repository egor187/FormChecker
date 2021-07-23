from django.db import models


class FormTemplate(models.Model):
    name = models.CharField(max_length=120, verbose_name="form name", blank=True, null=True)
    email = models.EmailField(null=True, blank=True)
    tel_number = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"form {self.name}"


from rest_framework import serializers

from .models import FormTemplate

import re


class FormTemplateWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormTemplate
        fields = ("date", "tel_number", "email", "text",)
        read_only_fields = (fields,)

    def validate_tel_number(self, value: str):
        """
        validating 'tel_number' field
        """
        pattern = re.compile(r"^\+?[78] ?\d{3} \)?-?\d{3} -?\d{2} -?\d{2}$")
        reg_res = pattern.match(str(value))
        if reg_res:
            return value
        else:
            raise serializers.ValidationError("Incorrect tel number format. Required: +7 xxx xx xx")


class FormTemplateReadSerializer(FormTemplateWriteSerializer):
    class Meta(FormTemplateWriteSerializer.Meta):
        fields = ('name',)

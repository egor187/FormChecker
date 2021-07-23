from rest_framework import serializers

from .models import FormTemplate

import re


class FormTemplateWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormTemplate
        fields = "__all__"
        read_only_fields = (fields,)

    def validate_tel_number(self, value):
        """
        validating 'tel_number' field
        """
        pattern = re.compile(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
        reg_res = pattern.match(str(value))
        if reg_res:
            return value
        else:
            raise serializers.ValidationError("Incorrect tel number format")


class FormTemplateReadSerializer(FormTemplateWriteSerializer):
    class Meta(FormTemplateWriteSerializer.Meta):
        fields = ('name',)

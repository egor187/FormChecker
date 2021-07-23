from rest_framework import mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import FormTemplate

from .serializers import FormTemplateWriteSerializer, FormTemplateReadSerializer


class FormTemplateAPIView(APIView):

    def post(self, request):
        serializer = FormTemplateWriteSerializer(data=request.data)
        serializer.is_valid()

        print(f"{serializer.validated_data}")

        if serializer.validated_data:
            result = FormTemplate.objects.filter(**serializer.validated_data)

            if result:
                response_serializer = FormTemplateReadSerializer(instance=result, many=True)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.http.response import JsonResponse
from django.core.exceptions import FieldDoesNotExist

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import FormTemplate

from .serializers import FormTemplateWriteSerializer, FormTemplateReadSerializer


class FormTemplateAPIView(APIView):

    def post(self, request):
        serializer = FormTemplateWriteSerializer(data=request.data)
        serializer.is_valid()

        if serializer.validated_data:
            model = FormTemplate
            result = FormTemplate.objects.filter(**serializer.validated_data)

            if result:
                response_serializer = FormTemplateReadSerializer(instance=result, many=True)
                return Response(response_serializer.data, status=status.HTTP_200_OK)
            else:
                answer = []
                for key in request.data.keys():
                    try:
                        answer.append({key: model._meta.get_field(key).description})
                    except FieldDoesNotExist:
                        continue
                return JsonResponse(answer, safe=False)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

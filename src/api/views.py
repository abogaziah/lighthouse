from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MissingPerson, ContactPerson
from .serializers import MissingPersonSerializer, ContactPersonSerializer


class MissingPersonViewSet(viewsets.ViewSet):
    def view(self, request):
        missing = MissingPerson.objects.all()
        serializer = MissingPersonSerializer(missing, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MissingPersonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        missing_person = MissingPerson.objects.get(id=pk)
        serializer = MissingPersonSerializer(missing_person)
        return Response(serializer.data)

    def update(self, request, pk=None):
        missing_person = MissingPerson.objects.get(id=pk)
        serializer = MissingPersonSerializer(instance=missing_person, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        missing_person = MissingPerson.objects.get(id=pk)
        missing_person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
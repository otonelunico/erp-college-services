import  json

from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView
from .serializers import ListQualification, \
    QualificationSerializer, \
    Teacher_SubjectSerializer, \
    AttorneySerializer, \
    StudentSerializer
from django.http import Http404, JsonResponse
from rest_framework import viewsets
from rest_framework import response
from rest_framework import status

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from .models import Qualification,Student, Attorney, Teacher_Subject

from django.views.generic.list import ListView, BaseListView

# Qualification

class QualificationViewSet(APIView):
 
    def get(self, context, **response_kwargs):
        qualification = Qualification.objects.all()
        serializer = QualificationSerializer(qualification, many=True)

        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = QualificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QualificationStudent(APIView):

    def get_object(self, id):
        try:
            student = Student.objects.get(rut=id).id
            return Qualification.objects.filter(student=student)
        except Qualification.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):

        qualification = self.get_object(id)
        serializer = QualificationSerializer(qualification, many=True)
        return response.Response(serializer.data)

    def post(self, request, id, format=None):
        serializer = QualificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QualificationStudentDetail(APIView):

    def get_object(self, id, pk):
        try:
            student = Student.objects.get(rut=id).id
            return Qualification.objects.get(student=student, position=pk)
        except Qualification.DoesNotExist:
            raise Http404

    def get(self, request, id, pk, format=None):
        qualification = self.get_object(id, pk)
        serializer = QualificationSerializer(qualification)
        return response.Response(serializer.data)

    def put(self, request, id, pk, format=None):
        qualification = self.get_object(id, pk)
        serializer = QualificationSerializer(qualification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, pk, format=None):
        qualification = self.get_object(id, pk)
        qualification.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id, pk, format=None):
        serializer = QualificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# teacher_subject

class Teacher_SubjectList(APIView):

    def get(self, context, **response_kwargs):
        teacher_Subject = Teacher_Subject.objects.all()
        serializer = Teacher_SubjectSerializer(teacher_Subject, many=True)

        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = Teacher_SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttorneyList(APIView):

    def get(self, context, **response_kwargs):
        attorney = Attorney.objects.all()
        serializer = AttorneySerializer(attorney, many=True)

        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = AttorneySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentList(APIView):

    def get(self, context, **response_kwargs):
        model = Student.objects.all()
        serializer = StudentSerializer(model, many=True)

        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
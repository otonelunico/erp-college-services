import  json

from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView
from .serializers import ListQualification, \
    QualificationSerializer, \
    Teacher_SubjectSerializer, \
    AttorneySerializer, \
    StudentSerializer, \
    TeacherSerializer, \
    EnrollmentSerializer, \
    GradeSerializer
from django.http import Http404, JsonResponse
from rest_framework import viewsets
from rest_framework import response
from rest_framework import status

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from .models import Qualification,Student, Attorney, Teacher_Subject, Teacher, Enrollment, Grade

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

class Teacher_SubjectList(APIView):

    def get(self, context, **response_kwargs):
        model = Teacher_Subject.objects.all()
        serializer = Teacher_SubjectSerializer(model, many=True)

        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = Teacher_SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Teacher_SubjectTeacher(APIView):

    def get_object(self, rut):
        try:
            rut = Teacher.objects.get(rut=rut).id
            return Teacher_Subject.objects.filter(teacher=rut)
        except Qualification.DoesNotExist:
            raise Http404

    def get(self, request, rut, format=None):

        model = self.get_object(rut)
        serializer = Teacher_SubjectSerializer(model, many=True)
        return response.Response(serializer.data)

    def post(self, request, rut, format=None):
        serializer = Teacher_SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Teacher_SubjectDetail(APIView):

    def get_object(self, rut, sub):
        try:
            id = Teacher.objects.get(rut=rut).id
            return Teacher_Subject.objects.get(teacher=id, subject=sub)
        except Attorney.DoesNotExist:
            raise Http404

    def get(self, request, rut, sub, format=None):
        model = self.get_object(rut, sub)
        serializer = Teacher_SubjectSerializer(model)
        return response.Response(serializer.data)

    def put(self, request, rut, sub, format=None):
        model = self.get_object(rut, sub)
        serializer = Teacher_SubjectSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, rut, sub, format=None):
        model = self.get_object(rut, sub)
        model.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, rut, sub, format=None):
        serializer = Teacher_SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherList(APIView):

    def get(self, context, **response_kwargs):
        model = Teacher.objects.all()
        serializer = TeacherSerializer(model, many=True)

        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetail(APIView):

    def get_object(self, id):
        try:
            return Teacher.objects.get(rut=id)
        except Attorney.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        model = self.get_object(id)
        serializer = TeacherSerializer(model)
        return response.Response(serializer.data)

    def put(self, request, id, format=None):
        model = self.get_object(id)
        serializer = TeacherSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        model = self.get_object(id)
        model.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id, format=None):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
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


    def put(self, request, format=None):
        model = Attorney.objects.all()
        serializer = AttorneySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttorneyDetail(APIView):

    def get_object(self, id):
        try:
            return Attorney.objects.get(rut=id)
        except Attorney.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        model = self.get_object(id)
        serializer = AttorneySerializer(model)
        return response.Response(serializer.data)

    def put(self, request, id, format=None):
        model = self.get_object(id)
        serializer = AttorneySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        model = self.get_object(id)
        model.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id, format=None):
        serializer = AttorneySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AttorneyDetailId(APIView):

    def get_object(self, id):
        try:
            return Attorney.objects.get(id=id)
        except Attorney.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        model = self.get_object(id)
        serializer = AttorneySerializer(model)
        return response.Response(serializer.data)

    def put(self, request, id, format=None):
        model = self.get_object(id)
        serializer = AttorneySerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        model = self.get_object(id)
        model.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id, format=None):
        serializer = AttorneySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
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

class StudentDetail(APIView):

    def get_object(self, id):
        try:
            return Student.objects.get(rut=id)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        model = self.get_object(id)
        serializer = StudentSerializer(model)
        return response.Response(serializer.data)

    def put(self, request, id, format=None):
        model = self.get_object(id)
        serializer = StudentSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        model = self.get_object(id)
        model.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetailId(APIView):

    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        model = self.get_object(id)
        serializer = StudentSerializer(model)
        return response.Response(serializer.data)

    def put(self, request, id, format=None):
        model = self.get_object(id)
        serializer = StudentSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        model = self.get_object(id)
        model.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnrollmentList(APIView):

    def get(self, context, **response_kwargs):
        model = Enrollment.objects.all()
        serializer = EnrollmentSerializer(model, many=True)

        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EnrollmentDetail(APIView):

    def get_object(self, id):
        try:
            return Enrollment.objects.get(id=id)
        except Enrollment.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        model = self.get_object(id)
        serializer = EnrollmentSerializer(model)
        return response.Response(serializer.data)

    def put(self, request, id, format=None):
        model = self.get_object(id)
        serializer = EnrollmentSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        model = self.get_object(id)
        model.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id, format=None):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GradeList(APIView):


    def get(self, context, **response_kwargs):
        model = Grade.objects.all()
        serializer = GradeSerializer(model, many=True)

        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GradeDetail(APIView):
    model = Grade.objects.all()

    def get_object(self, id):
        try:
            return self.model.get(id=id)
        except Grade.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        model = self.get_object(id)
        serializer = GradeSerializer(model)
        return response.Response(serializer.data)

    def put(self, request, id, format=None):
        model = self.get_object(id)
        serializer = GradeSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        model = self.get_object(id)
        model.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id, format=None):
        serializer = GradeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

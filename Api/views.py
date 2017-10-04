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
    GradeSerializer, \
    SubjectSerializer
from django.http import Http404, JsonResponse
from rest_framework import viewsets
from rest_framework import response
from rest_framework import status

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from .models import Qualification,Student, Attorney, Teacher_Subject, Teacher, Enrollment, Grade, Subject

from django.views.generic.list import ListView, BaseListView

# Qualification

class QualificationViewSet(APIView):

    def get(self, context, **response_kwargs):
        qualification = Qualification.objects.all()
        serializer = QualificationSerializer(qualification, many=True)

        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = QualificationSerializer(data=request.data)
        if Qualification.objects.filter(period=request.data['period'],
                                        teacher_subject=request.data['teacher_subject'],
                                        student=request.data['student'],
                                        ).count()<1:
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response(serializer.default_error_messages, status=status.HTTP_400_BAD_REQUEST)

class QualificationListStudentSubject(APIView):

    def get(self, request, id, sub, format=None):
        qualification = Qualification.objects.filter(student=id, teacher_subject=sub)
        serializer = QualificationSerializer(qualification, many=True)
        return response.Response(serializer.data)

class QualificationListGradeSubject(APIView):

    def get(self, request, grade, sub, format=None):
        qualification = Qualification.objects.filter(student__enrollment__grade=grade, teacher_subject=sub)
        serializer = QualificationSerializer(qualification, many=True)
        return response.Response(serializer.data)

class QualificationStudent(APIView):

    def get_object(self, id):
        try:
            student = Student.objects.get(rut=id).id
            return Qualification.objects.filter(student=student).order_by('student')
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

class QualificationDetail(APIView):

    def get_object(self, id, pk, sub):
        try:
            return Qualification.objects.get(student=id, position=pk, teacher_subject=sub)
        except Qualification.DoesNotExist:
            raise Http404

    def get(self, request, id, pk, sub, format=None):
        qualification = self.get_object(id, pk, sub )
        serializer = QualificationSerializer(qualification)
        return response.Response(serializer.data)

    def put(self, request, id, pk, sub, format=None):
        qualification = self.get_object(id, pk, sub)
        serializer = QualificationSerializer(qualification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, pk, sub, format=None):
        qualification = self.get_object(id, pk, sub)
        qualification.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id, pk, sub, format=None):
        serializer = QualificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QualificationStudentDetail(APIView):

    def get_object(self, id, pk, sub):
        try:
            student = Student.objects.get(rut=id).id
            return Qualification.objects.get(student=student, position=pk, teacher_subject=sub)
        except Qualification.DoesNotExist:
            raise Http404

    def get(self, request, id, pk, sub, format=None):
        qualification = self.get_object(id, pk, sub )
        serializer = QualificationSerializer(qualification)
        return response.Response(serializer.data)

    def put(self, request, id, pk, sub, format=None):
        qualification = self.get_object(id, pk, sub)
        serializer = QualificationSerializer(qualification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, pk, sub, format=None):
        qualification = self.get_object(id, pk, sub)
        qualification.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id, pk, sub, format=None):
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

class Teacher_SubjectDetailSub(APIView):

    def get_object(self, sub):
        try:
            return Teacher_Subject.objects.get(subject=sub)
        except Attorney.DoesNotExist:
            raise Http404

    def get(self, request, sub, format=None):
        model = self.get_object(sub)
        serializer = Teacher_SubjectSerializer(model)
        return response.Response(serializer.data)

    def put(self, request, sub, format=None):
        model = self.get_object(sub)
        serializer = Teacher_SubjectSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,  sub, format=None):
        model = self.get_object(sub)
        model.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, sub, format=None):
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

class StudentListGrade(APIView):

    def get(self, context, grade, **response_kwargs):
        model = Student.objects.filter(enrollment__grade=grade)
        serializer = StudentSerializer(model, many=True)
        return response.Response(serializer.data)

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

class EnrollmentDetailGrade(APIView):

    def get_object(self, grade):
        try:
            return Enrollment.objects.filter(grade=grade)
        except Student.DoesNotExist:
            raise Http404

    def get(self, context, grade, **response_kwargs):
        model = self.get_object(grade)
        serializer = EnrollmentSerializer(model, many=True)
        return response.Response(serializer.data)

    def post(self, request, grade, format=None):
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

class SubjectList(APIView):

    def get(self, context, **response_kwargs):
        model = Subject.objects.all()
        serializer = SubjectSerializer(model, many=True)

        return response.Response(serializer.data)

    def post(self, request, format=None):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubjectDetail(APIView):

    def get_object(self, id):
        try:
            return Subject.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        model = self.get_object(id)
        serializer = SubjectSerializer(model)
        return response.Response(serializer.data)

    def put(self, request, id, format=None):
        model = self.get_object(id)
        serializer = SubjectSerializer(model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        model = self.get_object(id)
        model.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, id, format=None):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
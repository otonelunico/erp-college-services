from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from rest_framework import  serializers
from .models import Qualification, Student, Attorney, Teacher_Subject

class ListQualification(ModelSerializer):

    class Meta:
        model = Qualification
        fields = ('teacher_subject', 'value')


class QualificationSerializer(ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('student', 'teacher_subject', 'value', 'position', 'period')


class Teacher_SubjectSerializer(ModelSerializer):
    class Meta:
        model = Teacher_Subject
        fields = ('subject', 'teacher')


class AttorneySerializer(ModelSerializer):
    class Meta:
        model = Attorney
        fields = ('rut',
                  'first_name',
                  'last_name',
                  'gender',
                  'address',
                  'email',
                  'birthdate',
                  'age',
                  'phone',
                  'cellphone',
                  )


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = ('rut',
                  'first_name',
                  'last_name',
                  'gender',
                  'address',
                  'email',
                  'birthdate',
                  'age',
                  'phone',
                  'cellphone',
                  'attorney',
                  'grade',
                  )


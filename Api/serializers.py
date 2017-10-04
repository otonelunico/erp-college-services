from rest_framework.serializers import ModelSerializer
from .models import Qualification, Student, Attorney, Teacher_Subject, Teacher, Enrollment, Grade, Subject

class ListQualification(ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('id',
                  'teacher_subject',
                  'value'
                  )

class QualificationSerializer(ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('id',
                  'student',
                  'teacher_subject',
                  'value',
                  'position',
                  'period'
                  )

class Teacher_SubjectSerializer(ModelSerializer):
    class Meta:
        model = Teacher_Subject
        fields = ('id',
                  'subject',
                  'teacher')

class AttorneySerializer(ModelSerializer):
    class Meta:
        model = Attorney
        fields = ('id',
                  'rut',
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

class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id',
                  'rut',
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
        fields = ('id',
                  'rut',
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
                  )

class EnrollmentSerializer(ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('id',
                  'rode',
                  'tariff',
                  'monthly',
                  'total',
                  'remaining',
                  'updated_at',
                  'created_at',
                  'grade',
                  'period',
                  'student',
                  'payment'
                  )

class GradeSerializer(ModelSerializer):
    class Meta:
        model = Grade
        fields = ('id',
                  'name',
                  'number',
                  'latter',
                  'level',
                  'teacher',
                  )

class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ('id',
                  'name',
                  'specialty',
                  )
from django.conf.urls import url
from .views import QualificationViewSet, \
    QualificationStudent, \
    QualificationStudentDetail, \
    AttorneyList, \
    StudentList, \
    AttorneyDetail, \
    StudentDetail, \
    TeacherList, \
    TeacherDetail, \
    EnrollmentList, \
    EnrollmentDetail, \
    Teacher_SubjectList, \
    Teacher_SubjectTeacher, \
    Teacher_SubjectDetail, \
    GradeList, \
    GradeDetail, \
    StudentDetailId, \
    AttorneyDetailId, \
    SubjectList, \
    SubjectDetail, \
    Teacher_SubjectDetailSub, \
    EnrollmentDetailGrade, \
    StudentListGrade, \
    QualificationListStudentSubject, \
    QualificationListGradeSubject, \
    QualificationDetail,\
    QualificationStudentId,\
    EnrollmentDetailStudent,\
    GradeDetailTeacher, \
    TeacherDetailId

# quialification
urlpatterns = [
    url(r'^quali/$',
        QualificationViewSet.as_view(),
        name='quali'),
    url(r'^quali/(?P<id>[0-9,-]+\d)/$',
        QualificationStudent.as_view(),
        name='quali_student'),
    url(r'^quali_id/(?P<id>\d+)/$',
        QualificationStudentId.as_view(),
        name='quali_student_id'),
    url(r'^quali/(?P<id>[0-9,-]+\d)/(?P<sub>\d+)/(?P<pk>[0-9]+)/$',
        QualificationStudentDetail.as_view(),
        name='quali_student_detail'),
    url(r'^quali_detail/(?P<id>\d+)/(?P<sub>\d+)/(?P<pk>\d+)/$',
        QualificationDetail.as_view(),
        name='quali_detail'),
    url(r'^quali_sub/(?P<id>\d+)/(?P<sub>\d+)/$',
        QualificationListStudentSubject.as_view(),
        name='quali_student_detail_sub'),
    url(r'^quali_grade/(?P<grade>\d+)/(?P<sub>\d+)/$',
        QualificationListGradeSubject.as_view(),
        name='quali_grade_sub'),
]

# teacher_Subject

urlpatterns += [
    url(r'^teacher_subject/$',Teacher_SubjectList.as_view(), name='teacher_Subject_list'),
    url(r'^teacher_subject/(?P<rut>[0-9,-]+\d)/$', Teacher_SubjectTeacher.as_view(), name='teacher_Subject_teacher'),
    url(r'^teacher_subject_sub/(?P<sub>\d+)/$', Teacher_SubjectDetailSub.as_view(), name='teacher_Subject_teacher_sub'),
    url(r'^teacher_subject/(?P<rut>[0-9,-]+\d)/(?P<sub>[0-9]+)/$',Teacher_SubjectDetail.as_view(), name='teacher_subject_detail'),
]

# Person attorney

urlpatterns += [
    url(r'^attorney/$',AttorneyList.as_view(), name='attorney_list'),
    url(r'^attorney/(?P<id>[0-9,-]+\w+)/$', AttorneyDetail.as_view(), name='attorney_detail'),
    url(r'^attorney_id/(?P<id>\d+)/$', AttorneyDetailId.as_view(), name='attorney_detail_id'),
]

# Person student

urlpatterns += [
    url(r'^student/$',StudentList.as_view(), name='student_list'),
    url(r'^student/(?P<id>[0-9,-]+\w+)/$', StudentDetail.as_view(), name='student_detail'),
    url(r'^student_id/(?P<id>\d+)/$', StudentDetailId.as_view(), name='student_detail_id'),
    url(r'^student_list_grade/(?P<grade>\d+)/$', StudentListGrade.as_view(), name='student_list_grade'),
]

# Person teacher

urlpatterns += [
    url(r'^teacher/$',TeacherList.as_view(), name='teacher_list'),
    url(r'^teacher/(?P<id>[0-9,-]+\d)/$', TeacherDetail.as_view(), name='teacher_detail'),
    url(r'^teacher_id/(?P<id>\d+)/$', TeacherDetailId.as_view(), name='teacher_detail_id'),
]

# Person teacher

urlpatterns += [
    url(r'^enrollment/$',EnrollmentList.as_view(), name='enrollment_list'),
    url(r'^enrollment/grade/(?P<grade>\d+)/$', EnrollmentDetailGrade.as_view(), name='enrollment_grade'),
    url(r'^enrollment/(?P<id>\d+)/$', EnrollmentDetail.as_view(), name='enrollment_detail'),
    url(r'^enrollment_st/(?P<id>\d+)/$', EnrollmentDetailStudent.as_view(), name='enrollment_detail_student'),
]

# Grade

urlpatterns += [
    url(r'^grade/$',GradeList.as_view(), name='grade_list'),
    url(r'^grade/(?P<id>\d+)/$', GradeDetail.as_view(), name='grade_detail'),
    url(r'^grade_teacher/(?P<id>\d+)/$', GradeDetailTeacher.as_view(), name='grade_detail_teacer'),
    ]


# Subject

urlpatterns += [
    url(r'^subject/$',SubjectList.as_view(), name='subject_list'),
    url(r'^subject/(?P<id>\d+)/$', SubjectDetail.as_view(), name='subject_detail'),
    ]


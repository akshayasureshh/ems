from rest_framework.routers import DefaultRouter
from .views import DynamicFormViewSet, EmployeeViewSet, FormFieldCreateView, FormFieldListView, employee_form_view
from django.urls import path, include
from .views import UpdateFieldOrder

router = DefaultRouter()
router.register('forms', DynamicFormViewSet)
router.register('employees', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reorder/', UpdateFieldOrder.as_view()),
    path('fields/', FormFieldCreateView.as_view()),                 
    path('forms/<int:form_id>/fields/', FormFieldListView.as_view()),
    path('employee-form/', employee_form_view),
]

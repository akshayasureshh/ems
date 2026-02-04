from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import DynamicForm, FormField, Employee
from .serializers import DynamicFormSerializer, EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import FormField
from .serializers import FormFieldCreateSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class DynamicFormViewSet(ModelViewSet):
    queryset = DynamicForm.objects.all()
    serializer_class = DynamicFormSerializer
    permission_classes = [IsAuthenticated]


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]


class UpdateFieldOrder(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        for item in request.data:
            FormField.objects.filter(id=item['id']).update(order=item['order'])

        return Response({"message": "Order updated"})
    

class FormFieldCreateView(CreateAPIView):
    queryset = FormField.objects.all()
    serializer_class = FormFieldCreateSerializer
    permission_classes = [IsAuthenticated]


class FormFieldListView(ListAPIView):
    serializer_class = FormFieldCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        form_id = self.kwargs['form_id']
        return FormField.objects.filter(form_id=form_id).order_by('order')
    
    
def employee_form_view(request):
    return render(request, 'frontend/templates/form.html')
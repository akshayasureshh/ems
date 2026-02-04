from rest_framework import serializers
from .models import DynamicForm, FormField, Employee

class FormFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormField
        fields = '__all__'


class FormFieldCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormField
        fields = ['id', 'form', 'label', 'field_type', 'order']


class DynamicFormSerializer(serializers.ModelSerializer):
    fields = FormFieldSerializer(many=True)
    
    def create(self, validated_data):
        fields_data = validated_data.pop("fields")
        dynamic_form = DynamicForm.objects.create(**validated_data)
        for field in fields_data:
            FormField.objects.create(form=dynamic_form, **field)
        return dynamic_form

    class Meta:
        model = DynamicForm
        fields = ['id', 'name', 'fields']


class EmployeeSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        form = attrs['form']
        data = attrs['data']

        for field in form.fields.all():
            value = data.get(field.label)

            if field.required and value in [None, ""]:
                raise serializers.ValidationError(
                    f"{field.label} is required"
                )

            if field.field_type == 'number':
                if not str(value).isdigit():
                    raise serializers.ValidationError(
                        f"{field.label} must be a number"
                    )

        return attrs

    class Meta:
        model = Employee
        fields = '__all__'

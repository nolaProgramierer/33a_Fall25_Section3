from django import forms
from django.forms import ModelForm

from .models import Student, Advisor, Course

#---------------------------------------------
# Model forms
#---------------------------------------------
# Inherits from ModelForm, form fields, validation, & save logic
class CourseForm(ModelForm):
    
    # Defines metadata for CourseForm
    class Meta:
        model = Course
        fields = ['dept','course_num', 'subject', 'description']

    # Customize initialization of CourseForm 
    def __init__(self, *args, **kwargs):
        # Call parent class (ModelForm) __init__ method
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # Update HTML attributes on widget
            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": f"Enter {field.label}"
            })

                
class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['fname', 'lname', 'student_advisor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for name, field in self.fields.items():
            field.widget.attrs.update({
                "class": "form-control",
                "placeholder": f"Enter {field.label}"
            })
            if name == "student_advisor":
                field.empty_label = "Select Advisor"
                

class AdvisorForm(ModelForm):
    class Meta:
        model = Advisor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs.update({
                "class": "form-control",
                "placeholder": f"Enter {field.label}"
            })


#---------------------------------------------
# Form form
#---------------------------------------------
class CourseSelectionForm(forms.Form):
    # Define field for selecting an object from a queryset
    course = forms.ModelChoiceField(queryset=Course.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))


class DropCourseForm(forms.Form):
    # Initially set queryset to none, will be set in __init__
    course = forms.ModelChoiceField(queryset=Course.objects.none(), label="Select a course to drop")

    def __init__(self, *args, **kwargs):
        # Retrieve 'student' from kwargs if provided'
        student = kwargs.pop("student", None)
        super().__init__(*args, **kwargs)
       
       # If a student is provided, set the queryset for the course field
        if student:
            self.fields["course"].queryset = student.courses.all()
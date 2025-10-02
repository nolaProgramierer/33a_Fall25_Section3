from django.db import models


class Advisor(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['lname']
    
    def __str__(self):
        return f'{self.lname}, {self.fname}'
    
    def advisee_count(self):
        return self.advisees.count()
    

def get_default_advisor():  
    default_advisor, created = Advisor.objects.get_or_create(
        fname="Default", lname="Advisor"
    )
    return default_advisor.id


class Student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
    student_advisor = models.ForeignKey(Advisor, 
                                        # If advisor is deleted, set to default advisor
                                        on_delete=models.SET(get_default_advisor),
                                        related_name="advisees",
                                        # Auto assign default advisor if none provided
                                        default=get_default_advisor,
                                        # Do not allow null values
                                        null=False,
                                        # Do not allow blank values in forms 
                                        blank=False
                                        )

    class Meta:
        ordering = ['lname', 'fname']

    def __str__(self):
        return f'{self.lname}, {self.fname} (ID: {self.id})'
    
    def get_full_name(self):
        return f'{self.fname} {self.lname}'
    
    def courses_count(self):
        return self.courses.count()
    
    
class Course(models.Model):
    dept = models.CharField(max_length=3)
    course_num = models.IntegerField()
    subject = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    students = models.ManyToManyField(Student, 
                                      blank=True, 
                                      related_name="courses"
                                      )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['dept', 'course_num'], name='unique_course'
            )
        ]
        ordering = ['dept', 'course_num']

    def __str__(self):
        return f'{self.dept} {self.course_num}: {self.subject}'
    
    # Returns a string from the iterable (students queryset)
    def student_names(self):
        return ", ".join(student.get_full_name() for student in self.students.all())
                      
   
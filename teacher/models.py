from django.db import models

# Create your models here.
from django.urls import reverse


class Subject(models.Model):
    """
    Model for holding subjects.
    """
    name = models.CharField(unique=True, null=False, max_length=60)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    """
    Holds teacher related details.
    """
    first_name = models.CharField(null=False, max_length=60, verbose_name='First Name')
    last_name = models.CharField(null=False, max_length=60, verbose_name='Last Name')
    phone_number = models.CharField(null=False, max_length=60, verbose_name='Phone Number')
    email = models.EmailField(unique=True, verbose_name='Email')
    profile_picture = models.ImageField(upload_to='profile_images/', verbose_name='Profile Picture', blank=True, null=True)
    room_no = models.CharField(max_length=40, verbose_name='Room Number')
    subjects = models.ManyToManyField(Subject)

    def get_absolute_url(self):
        return reverse('teacher_details', args=[str(self.id)])

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def get_subjects_list(self):
        return self.subjects.all().values_list('name', flat=True)

    # @property
    # def subjects(self):
    #     return ", ".join(self._subjects.values_list("name", flat=True))
    #
    # @subjects.setter
    # def subjects(self, value):
    #     if not value:
    #         self._subjects.clear()
    #     else:
    #         for subject_name in map(lambda x: x.strip().title(),
    #                                 value.split(",")):
    #             subject, created = \
    #                 Subject.objects.get_or_create(name=subject_name)
    #             if created:
    #                 subject.save()
    #             self._subjects.add(subject)

    def __repr__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'

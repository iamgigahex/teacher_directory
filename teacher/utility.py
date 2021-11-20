import csv
import os
import zipfile

from django.conf import settings

from teacher.models import Teacher, Subject


class Utilities:
    """
    Class for Utility functions
    """

    @staticmethod
    def upload_from_csv(csv_file, image_files=None):
        """
        Upload teachers details from csv and zip file.
        :param csv_file : csv file containing teachers details.
        :param image_files : zip file containing images.
        """
        data = csv_file.file.read()
        csv_content = data.decode('UTF-8').split('\n')
        reader = csv.DictReader(csv_content)
        success = failed = 0
        if image_files and zipfile.is_zipfile(image_files):
            with zipfile.ZipFile(image_files) as images:
                for teacher in reader:
                    try:
                        if not teacher['Email Address']:
                            continue
                        teacher_obj = Teacher(
                            first_name=teacher['First Name'],
                            last_name=teacher['Last Name'],
                            email=teacher['Email Address'],
                            phone_number=teacher['Phone Number'],
                            room_no=teacher['Room Number']
                        )
                        teacher_obj.save()
                        for subject_name in map(lambda x: x.strip().title(), teacher['Subjects taught'].split(",")[:5]):
                            subject, created = Subject.objects.get_or_create(name=subject_name)
                            if created:
                                subject.save()
                            teacher_obj.subjects.add(subject)
                        teacher_obj.save()
                        if teacher['Profile picture'] in images.namelist():
                            with images.open(teacher['Profile picture']) as profile_picture:
                                teacher_obj.profile_picture.save(teacher['Profile picture'], profile_picture, True)
                        success += 1
                    except Exception as e:
                        failed += 1
                return success, failed


from django import forms


class BulkUploadForm(forms.Form):
    csv_file = forms.FileField(label="Teacher's CSV file ", widget=forms.FileInput(attrs={'accept': '.csv', 'class':
        'form-control'}))
    image_zipfile = forms.FileField(label="Zipfile with images",
                                    widget=forms.FileInput(attrs={'accept': '.zip', 'class': 'form-control'}))

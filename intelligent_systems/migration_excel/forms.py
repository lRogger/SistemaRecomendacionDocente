# forms.py

from django import forms
class CargarExcelForm(forms.Form):
    archivo_excel_estudiantes = forms.FileField(label="Indicadores ESTUDIANTES", required=True, widget=forms.ClearableFileInput(attrs={'accept': '.xls,.xlsx'}))
    archivo_excel_profesores = forms.FileField(label="Indicadores PROFESORES", required=True, widget=forms.ClearableFileInput(attrs={'accept': '.xls,.xlsx'}) )


    class Meta:
        fields = ('archivo_excel_estudiantes', 'archivo_excel_profesores')

    def __init__(self, *args, **kwargs):
        super(CargarExcelForm, self).__init__(*args, **kwargs)

        self.fields['archivo_excel_estudiantes'].widget.attrs['class'] = 'mt-2 block w-full border-0 hover:border-blue-100 text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
        self.fields['archivo_excel_profesores'].widget.attrs['class'] = 'mt-2 block w-full border-0 hover:border-blue-100 text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'


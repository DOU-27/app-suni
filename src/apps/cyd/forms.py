from django import forms
from django.forms.models import inlineformset_factory
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User

from apps.cyd.models import Curso, CrAsistencia, CrHito, Sede, Grupo, Participante


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'


CrHitoFormSet = inlineformset_factory(
    Curso,
    CrHito,
    fields='__all__',
    extra=10,
    can_delete=True)
CrAsistenciaFormSet = inlineformset_factory(
    Curso,
    CrAsistencia,
    fields='__all__',
    extra=10,
    can_delete=True)


class SedeForm(forms.ModelForm):
    capacitador = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='cyd_capacitador'))
    lat = forms.CharField(max_length=25, required=False)
    lng = forms.CharField(max_length=25, required=False)

    class Meta:
        model = Sede
        fields = '__all__'
        exclude = ('mapa',)
        widgets = {
            'municipio': forms.Select(attrs={'class': 'select2'})
        }

    def __init__(self, *args, **kwargs):
        capacitador = kwargs.pop('capacitador', None)
        super(SedeForm, self).__init__(*args, **kwargs)
        if capacitador:
            self.fields['capacitador'].queryset = self.fields['capacitador'].queryset.filter(id=capacitador.id)
        self.fields['capacitador'].label_from_instance = lambda obj: "%s" % obj.get_full_name()


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = '__all__'
        widgets = {
            'sede': forms.Select(attrs={'class': 'select2'})
        }


class SedeFilterForm(forms.Form):
    capacitador = forms.ModelChoiceField(
        queryset=User.objects.filter(groups__name='cyd_capacitador'),
        widget=forms.Select(attrs={'class': 'form-control', 'data-url': reverse_lazy('sede_api_list')}))
    sede = forms.ModelChoiceField(
        queryset=Sede.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(SedeFilterForm, self).__init__(*args, **kwargs)
        self.fields['capacitador'].label_from_instance = lambda obj: "%s" % obj.get_full_name()


class CalendarioFilterForm(forms.Form):
    sede = forms.ModelChoiceField(
        queryset=Sede.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control select2', 'data-url': reverse_lazy('grupo_api_list')}))
    grupo = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'data-url': reverse_lazy('calendario_api_list')}))


class ParticipanteForm(forms.ModelForm):
    sede = forms.ModelChoiceField(
        queryset=Sede.objects.none(),
        widget=forms.Select(attrs={'class': 'select2', 'data-url': reverse_lazy('grupo_api_list')}))
    grupo = forms.ModelChoiceField(
        queryset=Grupo.objects.none(),
        widget=forms.Select(attrs={'data-url': reverse_lazy('participante_api_list')}))
    udi = forms.CharField()

    class Meta:
        model = Participante
        fields = [
            'sede', 'grupo', 'udi', 'nombre', 'apellido', 'genero', 'rol',
            'mail', 'tel_movil', 'fecha_nac']
        exclude = ('slug',)
        widgets = {
            'sede': forms.Select(attrs={'class': 'select2'})
        }

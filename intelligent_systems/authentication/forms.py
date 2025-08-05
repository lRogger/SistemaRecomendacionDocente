from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    firstname = forms.CharField(max_length=100, label='Nombre')
    lastname = forms.CharField(max_length=100, label='Apellido')
    username = forms.CharField(max_length=100, label='Nombre de usuario')
    email = forms.EmailField(max_length=150, label='Correo electrónico')
    password1 = forms.CharField(max_length=100, label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Confirmar contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('firstname', 'lastname', 'username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['firstname'].widget.attrs[
            'class'
        ] = 'block w-full rounded-lg border border-transparent shadow ring-1 ring-black/10 px-[calc(theme(spacing.2)-1px)] py-[calc(theme(spacing[1.5])-1px)] text-base/6 sm:text-sm/6 data-[focus]:outline data-[focus]:outline-2 data-[focus]:-outline-offset-1 data-[focus]:outline-black'
        self.fields['lastname'].widget.attrs[
            'class'
        ] = 'block w-full rounded-lg border border-transparent shadow ring-1 ring-black/10 px-[calc(theme(spacing.2)-1px)] py-[calc(theme(spacing[1.5])-1px)] text-base/6 sm:text-sm/6 data-[focus]:outline data-[focus]:outline-2 data-[focus]:-outline-offset-1 data-[focus]:outline-black'
        self.fields['username'].widget.attrs[
            'class'
        ] = 'block w-full rounded-lg border border-transparent shadow ring-1 ring-black/10 px-[calc(theme(spacing.2)-1px)] py-[calc(theme(spacing[1.5])-1px)] text-base/6 sm:text-sm/6 data-[focus]:outline data-[focus]:outline-2 data-[focus]:-outline-offset-1 data-[focus]:outline-black'
        self.fields['email'].widget.attrs[
            'class'
        ] = 'block w-full rounded-lg border border-transparent shadow ring-1 ring-black/10 px-[calc(theme(spacing.2)-1px)] py-[calc(theme(spacing[1.5])-1px)] text-base/6 sm:text-sm/6 data-[focus]:outline data-[focus]:outline-2 data-[focus]:-outline-offset-1 data-[focus]:outline-black'
        self.fields['password1'].widget.attrs[
            'class'
        ] = 'block w-full rounded-lg border border-transparent shadow ring-1 ring-black/10 px-[calc(theme(spacing.2)-1px)] py-[calc(theme(spacing[1.5])-1px)] text-base/6 sm:text-sm/6 data-[focus]:outline data-[focus]:outline-2 data-[focus]:-outline-offset-1 data-[focus]:outline-black'
        self.fields['password2'].widget.attrs[
            'class'
        ] = 'block w-full rounded-lg border border-transparent shadow ring-1 ring-black/10 px-[calc(theme(spacing.2)-1px)] py-[calc(theme(spacing[1.5])-1px)] text-base/6 sm:text-sm/6 data-[focus]:outline data-[focus]:outline-2 data-[focus]:-outline-offset-1 data-[focus]:outline-black'

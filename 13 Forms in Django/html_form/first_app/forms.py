from django import forms
from django.core import validators


class contactForm(forms.Form):
    name = forms.CharField(
        label='User Name',
        help_text='Total length must be within 70 characters',
        required=False,
        widget=forms.Textarea(attrs={
            'id': 'text_area',
            'class': 'bg-light',
            'placeholder': 'Enter your name'
        })
    )
    # file = forms.FileField()
    email = forms.EmailField()
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    check = forms.BooleanField()
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    appointment = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'datetime-local'}))
    size = forms.ChoiceField(
        choices=[
            ('S', 'Small'),
            ('M', 'Medium'),
            ('L', 'Large')
        ],
        widget=forms.RadioSelect
    )
    food = forms.MultipleChoiceField(
        choices=[
            ('A', 'Apple'),
            ('B', 'Banana'),
            ('M', 'Mango'),
            ('L', 'Lemon'),
            ('P', 'Pineapple'),
        ],
        widget=forms.CheckboxSelectMultiple
    )


def len_check(val):
    if len(val) < 10:
        raise forms.ValidationError("Enter at least 10 characters")


class StudentData(forms.Form):
    # <!-- Validation -->
    # name = forms.CharField(widget=forms.TextInput)
    # email = forms.CharField(widget=forms.EmailInput)

    # <!-- Option: 1 -->
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Invalid email address")
    #     return valemail

    # <!-- Option: 2 -->
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     if '.com' not in valemail:
    #         raise forms.ValidationError("Invalid email address")

    # <!-- Option: 3 -->
    name = forms.CharField(
        widget=forms.TextInput,
        validators=[validators.MinLengthValidator(
            10,
            message="Enter a name with at least 10 characters"
        )]
    )
    text = forms.CharField(
        widget=forms.TextInput,
        validators=[len_check]  # Custom func for validation
    )
    email = forms.CharField(
        widget=forms.EmailInput,
        validators=[
            validators.EmailValidator(message="Enter a valid email")
        ]
    )
    age = forms.IntegerField(
        validators=[
            validators.MaxValueValidator(40, message="Age must be 40 maximum"),
            validators.MinValueValidator(16, message="Age must be at least 16")
        ]
    )
    file = forms.FileField(
        validators=[
            validators.FileExtensionValidator(
                allowed_extensions=['pdf'],
                message="File extension must be ended with .pdf"
            )
        ]
    )


class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        val_name = self.cleaned_data['name']
        if len(val_name) < 10:
            raise forms.ValidationError("Name must be at least 10 characters")
        if val_pass != val_conpass:
            raise forms.ValidationError("Password didn't match")

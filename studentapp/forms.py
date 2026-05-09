from django import forms
from .models import Course, Student, CustomUser


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'price']


from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = [
            'full_name',
            'phone',
            'email',
            'course',
            'is_active'
        ]

    # FULL NAME VALIDATION

    def clean_full_name(self):

        full_name = self.cleaned_data.get('full_name')

        if len(full_name) < 3:
            raise forms.ValidationError(
                "Full name kamida 3 ta belgidan iborat bo‘lishi kerak"
            )

        return full_name

    # PHONE VALIDATION

    def clean_phone(self):

        phone = self.cleaned_data.get('phone')

        if not phone.startswith('+998'):
            raise forms.ValidationError(
                "Telefon raqam +998 bilan boshlanishi kerak"
            )

        if len(phone) < 13:
            raise forms.ValidationError(
                "Telefon raqam kamida 13 ta belgidan iborat bo‘lishi kerak"
            )

        return phone

    # EMAIL VALIDATION

    def clean_email(self):

        email = self.cleaned_data.get('email')

        if '@' not in email:
            raise forms.ValidationError(
                "Email ichida @ bo‘lishi kerak"
            )

        return email

#register
class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number']

    def clean(self):
        cleaned_data = super().clean()

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parollar bir xil emas!")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)

        password = self.cleaned_data.get('password1')

        user.set_password(password)  # 🔥 MUHIM QISM

        if commit:
            user.save()

        return user
from django import forms
from .models import forms

class ContactMe(forms.ModelForm):
	class Meta:
		model = Form

		fields = "__all__"
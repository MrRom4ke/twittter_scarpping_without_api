from django import forms


class MainForm(forms.Form):
    urls = forms.URLField(widget=forms.Textarea(attrs={"rows": "5", "cols": "40"}))


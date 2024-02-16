from django import forms


class Entry(forms.Form):
    entry = forms.CharField(label="entry")

from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(max_length=40,
                             widget=forms.TextInput(attrs={
                                 'class': 'form-control',
                                 'placeholder': 'Your name',
                             })
                             )
    body = forms.CharField(widget=forms.Textarea(
        {
            'class': 'form-control',
            'placeholder': 'Leave a comment!',
        }
    ))

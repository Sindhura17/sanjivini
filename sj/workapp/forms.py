

class ngoform(forms.ModelFrom):
    Username=forms.CharField()
    Password=forms.CharField(widget=forms.PasswordInput())
    Email=forms.EmailField()
    Name=forms.CharField()
    Phone=forms.CharField()
    Website=forms.URLField()
    Description=forms.CharField(widget=forms.Textarea(attrs={"rows":5,"cols":20}))
    class Meta:
        model=ngo
        field=('username','password','email','name','ph','link','text',)



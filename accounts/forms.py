from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):  # написан дочерний класс от UserCreationForm для его расширения
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None   # удалить поля help_text
            self.fields[fieldname].widget.attrs.update(
                {'class': 'form-control'}
            )
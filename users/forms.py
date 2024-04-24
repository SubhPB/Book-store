# The best way to predict the future is to create it.

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# fields to create user
class CustomUserCreationForm(UserCreationForm):

    class Meta: 
        model = get_user_model()
        fields = ('email', 'username')

# fields to edit the user
class CustomUserChangeForm(UserChangeForm):

    class Meta: 
        fields = ('email', 'username')
        model = get_user_model()
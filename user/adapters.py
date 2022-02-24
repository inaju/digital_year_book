from allauth.account.adapter import DefaultAccountAdapter


class CustomUserAccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_field

        user = super().save_user(request, user, form, False)
        user_field(user, 'email', request.data.get('email', ''))
        user_field(user, 'FirstName', request.data.get('FirstName', ''))
        user_field(user, 'LastName', request.data.get('LastName', ''))
        user_field(user, 'Matno', request.data.get('Matno', ''))

        user_field(user, 'NameOfProgram',
                   request.data.get('NameOfProgram', ''))
        user_field(user, 'NameOfCollage',
                   request.data.get('NameOfCollage', ''))
        user_field(user, 'NameOfDepartment',
                   request.data.get('NameOfDepartment', ''))

        user.save()
        return user

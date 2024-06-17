from client_hotel_reservation.models.custom_user_model import CustomUser

class UserHelper:
    def validate_data(self,request):
        errors = {}

        if 'email' in request.data and request.data['email'] == '':
            errors['email'] =  'Email should not be empty'

        if 'password' in request.data and request.data['password'] == '':
            errors['password'] =  'Password should not be empty'

        ############## Check if Existing ####################
        if request.data['username'] and CustomUser.objects.filter(username=request.data["username"]).count() != 0:
            errors['username'] = 'First name is already used'

        if request.data['email'] and CustomUser.objects.filter(email=request.data["email"]).count() != 0:
            errors['email'] = 'Email has already been used'

        ############## Validate Fields ######################
        if request.data['password'] != request.data['password2']:
            errors['password'] = 'Password does not match'

        return errors
    
    def validate_user(self,request):
        errors = {}

        if request.user.is_anonymous:
            errors['user'] = 'User is not logged in'
            return errors
        if request.user.api_secret_key != request.META.get('HTTP_API_SECRET_KEY'):
            errors['api_secret'] = 'Invalid API secret key'
            return errors
            
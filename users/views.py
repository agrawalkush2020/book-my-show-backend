from django.http.response import HttpResponse
import json
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from movies.utility import get_all_movies_for_city

@csrf_exempt
def handle_signup(request):

    if request.method == "POST":
        credentials = json.loads(request.body)

        # Extract credentials
        email = credentials.get('email')
        phone_number = credentials.get('phoneNumber')
        full_name = credentials.get('fullName')
        password = credentials.get('password')

        # Check if user already exists
        if CustomUser.is_existing_user(email=email, phone_number=phone_number):
            return HttpResponse(json.dumps({"success": False, "message": "User Already Exists!"}),
                                content_type="application/json")

        # Create new user
        new_user = CustomUser(
            email=email,
            phone_number=phone_number,
            full_name=full_name,
            password=make_password(password)  # Ensure you hash the password
        )
        new_user.save()
        return HttpResponse(json.dumps({"success": True}),
                            content_type="application/json")

    return HttpResponse(json.dumps({"success": False, "message": "Invalid request method"}),
                        content_type="application/json")


@csrf_exempt
def handle_login(request):
    if request.method == "POST":
        credentials = json.loads(request.body)

        # Extract credentials
        phone_number = credentials.get('phoneNumber')
        password = credentials.get('password')

        # checking if any user with credentials exist
        user = authenticate(request, phone_number=phone_number, password=password)

        if user is None:
            return HttpResponse(
                json.dumps({"success": False, 'message': 'Invalid phone number or password!'}),
                content_type="application/json",
                status=200
            )

        try:
            login(request, user)
            movies = get_all_movies_for_city()

            return HttpResponse(json.dumps({"success": True,
                                            'user': user.full_name,
                                            'movies': movies}),
                                content_type="application/json", status=200)

        except Exception as ex:
            return HttpResponse(
                json.dumps({"success": False, 'message': 'Something went Wrong!'}),
                content_type="application/json",
                status=200
            )


    # when request method is not Post
    else:
        print(f'{request.method}')
        response_data = json.dumps({"success": False, 'message': 'Invalid request method'})
        return HttpResponse(response_data, content_type="application/json", status=405)



@csrf_exempt
def handle_logout(request):
    logout(request)
    return HttpResponse(json.dumps({"success": True}), content_type="application/json", status=200)

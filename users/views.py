from django.http.response import HttpResponse, JsonResponse
import json
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout

@csrf_exempt
def handle_signup(request):

    if request.method == "POST":
        credentials = json.loads(request.body)

        # Extract credentials
        username = credentials.get('userName')
        email = credentials.get('email')
        phone_number = credentials.get('phoneNumber')
        full_name = credentials.get('fullName')
        password = credentials.get('password')

        # Check if user already exists
        if CustomUser.is_existing_user(username=username, email=email, phone_number=phone_number):
            return HttpResponse(json.dumps({"success": False, "message": "User Already Exists!"}),
                                content_type="application/json")

        # Create new user
        new_user = CustomUser(
            username=username,
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
        username = credentials.get('userName')
        password = credentials.get('password')

        # Check if user already exists
        # if CustomUser.is_existing_user(username=username) is False:
        #     return HttpResponse(json.dumps({"success": False, "message": "Wrong Username !!"}),
        #                         content_type="application/json")

        # agr credentials match krgye toh user ka object return otherwise None return hoga
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse(json.dumps({"success": True, 'user': user.username}),
                                content_type="application/json", status=200)
        else:
            return HttpResponse(json.dumps({"success": False, 'message': 'Invalid Password!'}),
                                content_type="application/json", status=200)

    # when request method is not Post
    else:
        print(f'{request.method}')
        response_data = json.dumps({"success": False,'message': 'Invalid request method'})
        return HttpResponse(response_data, content_type="application/json", status=405)



@csrf_exempt
def handle_logout(request):
    logout(request)
    return HttpResponse(json.dumps({"success": True}), content_type="application/json", status=200)


@csrf_exempt
def fetch_all_users(request):
    # Get the current logged-in user's username
    current_username = request.user.username
    # Fetch all users except superusers and the current logged-in user
    users = CustomUser.objects.filter(is_superuser=False).exclude(username=current_username).values_list('username', flat=True)
    return JsonResponse({'success':True,'users':users,'current_username':current_username},status=200)


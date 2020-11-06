import json
import jwt
import my_settings

from django.http import JsonResponse

from .models import User
from my_settings  import SECRET,ALGORITHM

def token_check(func): 
    def wrapper(self, request, *args, **kwargs):

        if "AUTHORIZATION" not in request.headers: 
            return JsonResponse({"message" : "INVALID_LOGIN"}, status=400)

        encode_token = request.headers["AUTHORIZATION"] 

        try:
            user_id     = jwt.decode(encode_token, SECRET, algorithm = ALGORITHM)                         
            user_filter = User.objects.get(id=user_id["user_id"])
            
            if user_filter :
                request.user = user_filter
                return func(self, request,*args ,**kwargs) 
            else : 
                return JsonResponse({"message":"INVALID_USER"}, status=400)
        
        except jwt.DecodeError:
            return JsonResponse({"message":"INVALID_TOKEN"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"message":"UNKNOWN_USER"}, status=400)
            
    return wrapper
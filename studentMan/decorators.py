from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')

    return wrapper_func

def allowed_users(roles):
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			role = request.user.role				

			if role in roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('Bạn không có quyền truy cập')
		return wrapper_func
	return decorator
from django.shortcuts import redirect

def getAuthSession(request):
    name_user = request.session.get('user_name', 'default')
    return {'name': name_user}
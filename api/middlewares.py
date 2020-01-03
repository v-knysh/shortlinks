def user_ip_middleware(get_response):
    def middleware(request):
        request.user_ip = request.META.get('REMOTE_ADDR')
        response = get_response(request)
        return response
    return middleware

class RequestLogMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # PATH
        print(f"Path: {request.path}")

        # METHOD
        print(f"Method: {request.method}")

        # USER
        if request.user.is_authenticated:
            print(f"User: {request.user.username}")
        else:
            print("User: Anonymous")

        print("-" * 40)

        response = self.get_response(request)
        return response
from django.shortcuts import redirect

ALLOWED_URLS = ["/shop/", "/items/", "/about/"]


class BeOnSiteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 404 or response.status_code >= 500:
            return redirect("/shop/")

        return response

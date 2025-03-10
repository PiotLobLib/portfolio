from django.shortcuts import render


def home(request):
    return render(
        request=request,
        template_name='infos/home.html',
        context={'title': 'Home'}
    )


def me(request):
    return render(
        request=request,
        template_name='infos/me.html',
        context={'title': 'Me'}
    )


def contact(request):
    return render(
        request=request,
        template_name='infos/contact.html',
        context={'title': 'Contact'}
    )

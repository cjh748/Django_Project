from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from accounts.forms import SignUpForm
from django.conf import settings
from django.utils.encoding import force_bytes
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.contrib.auth.models import User

#from accounts.models import User


def index(request):
    return render(request, 'html/index.html')


def sign_up(request):
    form = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        #email = form.cleaned_data.get('email')
        if form.is_valid():
            # user = User.objects.create(
            #     email=email,
            #     is_active=False
            # )
            # send_account_activation_email(request, user)
            form.save()
            return index(request)

        else:
            print("form invalid")
    return render(request, 'html/sign_up.html', {'register_form': form})


def log_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print("User found!")
            if user.is_active:
                print("Login Successful")
                login(request, user)
                return redirect('menu')
        else:
            print("Invalid login details for User: " + username + ", Pass: " + password)
            return render(request, 'html/login.html')
    else:
        print("Login page started...")
        return render(request, 'html/login.html')


def send_account_activation_email(request, user):
        text_content = 'Account Activation Email'
        subject = 'Email Activation'
        template_name = "emails/account/activation.html"
        from_email = settings.DEFAULT_FROM_EMAIL
        recipients = [user.email]
        kwargs = {
            "uidb64": urlsafe_base64_encode(force_bytes(user.pk)).decode(),
            "token": default_token_generator.make_token(user)
        }
        activation_url = reverse("app:activate_user_account", kwargs=kwargs)

        activate_url = "{0}://{1}{2}".format(request.scheme, request.get_host(), activation_url)

        context = {
            'user': user,
            'activate_url': activate_url
        }
        html_content = render_to_string(template_name, context)
        email = EmailMultiAlternatives(subject, text_content, from_email, recipients)
        email.attach_alternative(html_content, "text/html")
        email.send()


def activate_user_account(request, uidb64=None, token=None):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except User.DoesNotExist:
        user = None
    if user and default_token_generator.check_token(user, token):
        user.is_email_verified = True
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return HttpResponse("Activation link has expired")

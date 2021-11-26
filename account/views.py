from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from .forms import SignupForm

# Create your views here.

User = get_user_model()

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            #cleaned_data- 데이터를 획득하고, 기본 유효성 검사 도구를 이용해 입력값을 다듬는다(cleaned).
            # 안전하지 않을 수 있는 입력값을 필터링하며, 해당 입력값에 맞는 표준 형식으로 변환한다.
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
        else:
            return render(request, "account/signup.html", {
                    'error': '패스워드가 불일치합니다.',
                })
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})

@login_required
def mybook(request):
    books = request.user.get_rent_books()
    return render(request, 'account/mybook.html', {'books': books})
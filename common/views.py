
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
# from common.forms import UserForm
from common.forms import UserCreationForm
from .models import User
from .forms import UserChangeForm

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'common/signup.html', {'form': form})




# def login(request):
#     """
#     로그인
#     """
#     print(request)
#     print(request.email)
#     user = authenticate(email=request.email, password=request.raw_password)
#     login(request, user)

#     return redirect('index')


# def user_confirm(request):
#     """
#     유저 정보 전 인증
#     """
#     return render(request, 'common/user_confirm.html')

def userinfo(request):
    """
    유저 정보
    """
    return render(request, 'common/userinfo.html')


def userinfo_modify(request):
    """
    유저 정보 수정
    """
    user = get_object_or_404(User, pk=request.user.id)
    if request.method == "POST":
        # 질문 수정을 위해 값 덮어쓰기
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('index')
    else:
        # 질문 수정 화면에 기존 제목, 내용 반영
        form = UserChangeForm(instance=user)

    context = {'form':form}
    return render(request, 'common/userinfo_modify.html', context)















































# def signup(request):
#     """
#     계정생성
#     """
#     if request.method == "POST":
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = UserForm()
#     return render(request, 'common/signup.html', {'form': form})


# def userinfo(request):
#     """
#     유저 정보
#     """
#     return render(request, 'common/userinfo.html')

# def userinfo(request, user_id):
#     """
#     유저 정보
#     """
#     username = get_object_or_404(User, pk=user_id)
#     context = {'username': username}
#     return render(request, 'login_out/question_detail.html', context)


# def detail(request, question_id):
#     """
#     pybo 내용 출력
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     context = {'question': question}
#     return render(request, 'login_out/question_detail.html', context)


# @login_required(login_url='common:login')
# def question_modify(request, question_id):
#     """
#     pybo 질문수정
#     """
#     question = get_object_or_404(Question, pk=question_id)
#     if request.user != question.author:
#         messages.error(request, '수정권한이 없습니다')
#         return redirect('pybo:detail', question_id=question_id)

#     if request.method == "POST":
#         # 질문 수정을 위해 값 덮어쓰기
#         form = QuestionForm(request.POST, instance=question)
#         if form.is_valid():
#             question = form.save(commit=False)
#             question.author = request.user
#             question.modify_date = timezone.now()   # 수정일시 저장
#             question.save()
#             return redirect('pybo:detail', question_id=question.id)
#     else:
#         # 질문 수정 화면에 기존 제목, 내용 반영
#         form = QuestionForm(instance=question)

#     context = {'form':form}

#     return render(request, 'pybo/question_form.html', context)


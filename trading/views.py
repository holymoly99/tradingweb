from django.shortcuts import render, get_object_or_404, redirect
from .models import Write, Answer
from django.utils import timezone
from .forms import WriteForm, AnswerForm

def index(request):
    """글 목록 출력"""
    write_list = Write.objects.order_by('-create_date')
    context = {'write_list': write_list}

    return render(request, 'trading/write_list.html', context)

def detail(request, write_id):
    """글 내용 출력"""
    write = get_object_or_404(Write, pk=write_id)
    context = {'write' : write}

    return render(request, 'trading/write_detail.html', context)

def answer_create(request, write_id):
    """댓글 입력"""
    write = get_object_or_404(Write, pk=write_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.write = write
            answer.save()
            return redirect('trading:detail', write_id=write.id)
    else:
        form = AnswerForm()

    context = {'write':write, 'form':form}
    return redirect(request, 'trading/write_detail.html', context)

def write_create(request):
    """글 작성"""
    if request.method == 'POST':
        form = WriteForm(request.POST)
        if form.is_valid():
            write = form.save(commit=False)
            write.price = request.POST.get('price')
            write.tmethod = request.POST.get('tmethod')
            write.category = request.POST.get('category')
            write.images = request.FILES['images']
            write.create_date = timezone.now()
            write.save()
            return redirect('trading:index')
    else:
        form = WriteForm()
        
    context = {'form' : form}
    return render(request, 'trading/write_form.html', context)
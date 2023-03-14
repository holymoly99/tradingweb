from django.shortcuts import render, get_object_or_404, redirect
from ..models import Sell

from django.db.models import Q
from django. contrib.auth.decorators import login_required

from django.core.paginator import Paginator

@login_required(login_url='common:login')
def sell_mypost(request, sell_id):
    """
    joonggo 목록 출력
    """
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    
    sell_list = Sell.objects.order_by('-create_date')
    if kw:
        sell_list = sell_list.filter(
            Q(subject__icontains=kw) | #제목 검색
            Q(content__icontains=kw) | #내용 검색
            Q(author__username__icontains=kw)
        )
   
    paginator = Paginator(sell_list, 12)
    page_obj = paginator.get_page(page)

    context = {'sell_list': page_obj,
               'page': page,
               'kw': kw,
               }
    
    return render(request, 'joonggo/sell_mypost.html', context)
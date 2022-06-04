from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count

from ..models import Question, Category


def index(request, category_name='qna'):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')
    question_list = Question.objects.order_by('-create_date')

    category_list = Category.objects.all()
    category = get_object_or_404(Category, name=category_name)
    question_list = Question.objects.filter(category=category)

    if so == 'recommend':
        # aggretation, annotation에는 relationship에 대한 역방향 참조도 가능 (ex. Count('voter'))
        question_list = question_list.annotate(num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = question_list.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:
        question_list = question_list.order_by('-create_date')

        # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # 질문 제목검색
            Q(content__icontains=kw) |  # 질문 내용검색
            Q(answer__content__icontains=kw) |  # 답변 내용검색
            Q(author__username__icontains=kw) |  # 질문 작성자검색
            Q(answer__author__username__icontains=kw)  # 답변 작성자검색
        ).distinct()

        # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개식 보여주기
    page_obj = paginator.get_page(page)
    max_index = len(paginator.page_range)

    context = {'question_list': page_obj, 'max_index': max_index, 'page': page, 'kw': kw, 'so': so,
               'category_list': category_list, 'category': category}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

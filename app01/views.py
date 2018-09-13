from django.shortcuts import render,HttpResponse,redirect
from django.db.models import Max,Min,Avg,Count
from app01.models import login,book
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
# from app01.models import Book,Publish,Author,AuthorDetail
# Publish = Publish.objects.all()
# def wudi(request):
#     # publish_obj = Publish.objects.get(nid=1)
#     # print(publish_obj)
#     # book_obj = Book.objects.create(title="金瓶眉", publishDate="2012-12-12", price=100, publish=publish_obj)
#     # book_obj = Book.objects.create(title="追风筝的人", price=200, publishDate="2012-11-12", publish_id=1)
#     # alex_obj= Author.objects.filter(name='alex').first()
#     # egon_obj = Author.objects.filter(name='yuan').first()
#     # book_obj = Book.objects.filter(title='追风筝的人').first()
#     # book_obj.authors.add(alex_obj,egon_obj)
#     # book_obj = Book.objects.filter(nid=1).first()
#     # publish_obj = Publish.objects.filter(book=book_obj).first()
#     # print(book_objpublish.city)
#     # publish = Publish.objects.filter(name='苹果出版社').first()
#     # book_list = publish.book_set.all()
#     # for i in book_list:
#     #     print(i.title)
#     # addr_obj = AuthorDetail.objects.get(addr='北京')
#     # print(addr_obj.author.name)
#     # book_obj = Book.objects.filter(publish__name='苹果出版社').values('title','price')
#     # author_list = book_obj.authors.all()
#     # book_obj = Book.objects.filter(authors__authorDetail__telephone='110').values('authors__name)
#     # for i in author_list:
#     # book_obj = Book.objects.all().aggregate(MAX = Max('price'),MIN = Min("price"),AVG = Avg('price'))
#     #     print(i.name,i.authorDetail.telephone
#     book_obj = Book.objects.annotate(c = Count('publish__id')).values_list('publish__name','c')
#     # for i in book_obj:
#     # book_obj = Book.objects.annotate(c = Count("authors")).values_list('c','a')
#     #
#     #     print(i.publish.name,i.c)
#     print(book_obj)
#
#     return HttpResponse("OK")
def index2(request):
    # book_list = book.objects.all()
    # paginator = Paginator(book_list,10)
    # print('count:',paginator.count)
    # print('num_Pages:',paginator.num_pages)
    # print('page_range:',paginator.page_range)

    # for i in page1:
    #     print(i)
    # print(page1.object_list)
    # page2 = paginator.page(2)
    # # for i in page2:
    # #     print(i)
    # #
    # print('是否有下一页', page2.has_next())
    # print('下一页的页码', page2.next_page_number())
    # print('是否有上一页', page2.has_previous())
    # print('上一页的页码', page2.previous_page_number())
    book_list = book.objects.all()
    paginator = Paginator(book_list, 10)
    page = request.GET.get('page',1)
    currentPage = int(page)
    page1 = paginator.page(page)
    return render(request, 'page.html', {"book_list":book_list,'paginator':paginator,'currentPage':currentPage,'page1':page1})

def index(request):
    #  如果页数十分多时，换另外一种显示方式
    book_list = book.objects.all()

    paginator = Paginator(book_list, 1)
    page = request.GET.get('page', 1)
    currentPage = int(page)
    if paginator.num_pages > 11:

        if currentPage - 5 < 1:
            pageRange = range(1, 11)
        elif currentPage + 5 > paginator.num_pages:
            pageRange = range(currentPage - 5, paginator.num_pages + 1)

        else:
            pageRange = range(currentPage - 5, currentPage + 5)

    else:
        pageRange = paginator.page_range

    try:
        print(page)
        book_list = paginator.page(page)
    except PageNotAnInteger:
        book_list = paginator.page(1)
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)

    return render(request, "page.html", locals())
def add_book(request):
    n = 1
    for i in range(100):
        ret = book.objects.create(title='西游记'+'%s'%n,publish='北京出版社',price=120+n)
        n+=1
    return HttpResponse('ok')

def add_login(request):
    login.objects.create(usename ='chen',password=123)
    return HttpResponse('OK')

def test(request):
    # return render(request,'nb.html')
    return HttpResponse('ok')

def handle(request):
    return render(request,'ajax_test.html')

def login_do(request):
    print(request.POST)
    user = request.POST.get('username')
    pwd = request.POST.get('password')
    ret = login.objects.filter(usename=user,password=pwd).first()
    if ret:
        return HttpResponse('登录成功')
    # print(user,pwd)
    else:
        return HttpResponse('账号或密码错误')
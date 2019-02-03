from django.shortcuts import render,HttpResponse
from app01.models import *
# Create your views here.

def add(request):

    ####################################绑定一对多的关系####################################
    #为book表绑定publish

    #方式1：
    #book_obj=Book.objects.create(title="hongloumeng",price=100,publish="2019-01-18",publish_id=1)
    # pub_obj= Publish.objects.filter(nid=1).first()
    #
    # book_obj = Book.objects.create(title="hongloumeng",price=100,publishDate="2019-01-18",publish=pub_obj)
    # print(book_obj.title)
    # print(book_obj.price)
    # print(book_obj.publish)
    # print(book_obj.publish_id)
    #
    # return HttpResponse("OK")

    ####################################绑定多对多的关系####################################
    #为book表绑定publish

    #book_obj = Book.objects.create(title="qqq", price=123, publishDate="2019-01-18", publish_id=2)

    # book_obj = Book.objects.create(title="aaa", price=123, publishDate="2019-09-19",publish_id=1)
    #
    # lx = Author.objects.get(name="lx")
    # ww = Author.objects.get(name="ww")

    #绑定多对多关系的API
    # book_obj.authors.add(lx,ww)
    # book_obj.authors.add(1,2)
    # book_obj.authors.add(*[1,2])

    #解除多对多关系的API
    # book=Book.objects.filter(nid=1).first()
    # book.authors.remove(1)

    #清空所有该对象多对多关系
    # book.authors.clear()

    #查
    # book.authors.all()   #查询这本书的所有作者对象   是个queryset

    return HttpResponse("OK")


def query(request):
    """
    跨表查询
        1 基于对象查询
        2 基于双下划线查询
        3 聚合和分组查询
        4 F 与 Q查询

    :param request:
    :return:
    """
    #############################################基于对象查询（子查询）#######################################
    #一对多的正向查询：     查询qqq这本书的出版社名字

    #正向查询：按字段
    # book_obj = Book.objects.filter(title="qqq").first()
    #
    # print(book_obj.publish)    #与这本书关联的出版社对象
    # print(book_obj.publish.name)


    # 一对多的反向查询：     查询人民出版社出版过的书籍名称
    #反向查询：按表名小写_set

    # publish = Publish.objects.first(name="人民出版社").first()
    # publish.book_set.all()

    # 多对多的正向查询：查询qqq这本书的所有作者的名字
    # 正向查询：按字段

    # book=Book.objects.filter(title='aaa').first()
    # #print(book)
    # author_list = book.authors.all()        #queryset对象
    # for author in author_list:
    #     print(author.name)

    # 多对多的反向查询：     查询lx出版过的所有书籍名称
    # 反向查询：按表名小写_set

    # aa = Author.objects.filter(name="lx").first()
    # book_list = aa.book_set.all()
    # for book in book_list:
    #     print(book.title)

    #一对一的正向查询 : 查询lx的手机号
    #正向查询：按字段
    # lx=Author.objects.filter(name="lx").first()
    # print(lx.authordetail.telphone)

    # 一对一的反向查询 :  查询手机号为。。。的作者的名字和年龄
    # 反向查询：按表名小写
    # tel = AuthorDetail.objects.filter(telphone=12345678909).first()
    # print(tel.author.name)
    # print(tel.author.age)

    #############################################基于双下划线的跨表查询（join查询）#######################################
    #正向查询按字段
    #反向查询按表名小写
    # 一对多的正向查询：     查询qqq这本书的出版社名字
    ret=Book.objects.filter(title="qqq").values("publish__name")

    #反
    book= Publish.objects.filter(book__title="qqq").values("name")

    # 多对多的正向查询：     查询qqq这本书的所有作者的名字
    Book.objects.filter(title="qqq").values("authors__name")
    #反
    Author.objects.filter(book__title="qqq").values("name")

    #############################################聚合查询aggregate:返回值是一个字典#######################################
    from django.db.models import Avg,Max,Min,Count
    #查询所有书籍的平均价格
    Book.objects.all().aggregate(Avg("price"))



    #############################################分组查询annotate  返回queryset#######################################
    #单表分组查询：
    #查询每一个部门的名称以及员工的平均薪水
    ret = Emp.objects.values("dep").annotate(avg_salary=Avg("salary"))
    print(ret)

    # 跨表分组查询
    ret = Publish.objects.values("nid").annotate(c=Count("book__title")).values("name","c")

    #20190203
    return HttpResponse("OK")
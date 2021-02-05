from django.shortcuts import render

# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        import pymysql
        conn = pymysql.connect(host="127.0.0.1", port=3306, user='demo', passwd='demo@2020', db='app')
        cursor = conn.cursor()
        cursor.execute('select * from users where username=%s and password=%s' % (username, password))
        result = cursor.rowcount
        cursor.colse()
        conn.colse()
        if result:
            return HttpResponse('登录成功')
        else:
            return HttpResponse('登录失败')
    else:
        return render(request, template_name='login.html')


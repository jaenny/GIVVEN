from .models import *
from django.shortcuts import get_object_or_404, redirect, render
import datetime
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.

def check_password(checkpw,originalpw):
    if checkpw==originalpw:
        return True
    else:
        return False

def login_view(req):
    if req.method=="GET":
        return render(req,'login.html')
    elif req.method=="POST":
        user_id = req.POST.get('user_id')
        user_pw = req.POST.get('user_pw')

        res_data={}
        if not (user_id and user_pw):
            res_data['error']="모든 칸을 다 입력해주세요"

        else:
            #기존(DB)에 있는 Fuser 모델과 같은 값인 걸 가져온다.
            user = User.objects.get(email=user_id) #(필드명=값)

            #비밀번호가 맞는지 확인한다.
            if check_password(user_pw,user.password):
                #응답 데이터 세션에 값 추가. 수신측 쿠키에 저징됨
                req.session['user'] = user.id 
                return redirect('/')
            else:
                res_data['error'] = "비밀번호가 틀렸습니다."
        return render(req,'login.html',res_data) #응답 데이터 res_data 전달


def logout_view(request):
    logout(request)
    return redirect("/")

def register_view(req):
    if req.method == 'POST':
        user = User()
        user.email = req.POST['email']
        user.name = req.POST['name']
        user.password = req.POST['password']
        user.save()
        return redirect('/')
    return render(req,'signup.html')
      

def select_plan(request):
    user_pk = request.session.get('user')
    if not user_pk:
        return redirect('/login')
    elif user_pk:
        if request.method == 'POST':
            user = get_object_or_404(User,pk=user_pk)
            user.plan = request.POST['plan']
            user.save()
            return redirect('/')
    return render(request,'select_plan.html')

def read_organi(req):
    orga = Organization.objects.all()
    context = {
        'data' : orga
    }
    return render(req,'all_orga.html',context)
    
def cnt_coin(user):
    total_coin = 0
    if user.plan == "simple" :
        total_coin = 10
    elif user.plan == "premium":
        total_coin = 20
    elif user.plan == "nobless":
        total_coin = 50
    return total_coin
def create_user_choice(req):
    user_pk = req.session.get('user')
    if not user_pk :
        return redirect('/login')
    elif user_pk : 
        user = User.objects.get(pk=user_pk)
        total_coin = cnt_coin(user)
        context={
            'data' : total_coin
        }
        if req.method == 'POST':
            list = req.POST.getlist("orga_coin[]")
            for i in range(0,len(list),2): 
                if i==0:
                    f_date = datetime.datetime.now()
                user_choice = User_Choiced()
                user_choice.user = user
                user_choice.orga = Organization.objects.get(name=list[i])
                user_choice.coin = list[i+1]
                user_choice.date = f_date
                user_choice.save()
        return render(req,'create_user_choice.html',context)

def update_user_choice(req):
    user_pk = req.session.get('user')
    if not user_pk :
        return redirect('/login')
    elif user_pk : 
        nuser = User.objects.get(pk=user_pk)
        user_choiced = User_Choiced.objects.filter(user=nuser).order_by('-date')[:1]
        delete_date=user_choiced[0].date
        User_Choiced.objects.filter(user=nuser,date=delete_date).delete()
        total_coin = cnt_coin(nuser)
        context={
            'data' : total_coin
        }
        if req.method == 'POST':
            list = req.POST.getlist("orga_coin[]")
            for i in range(0,len(list),2): 
                if i==0:
                    f_date = datetime.datetime.now()
                user_choice = User_Choiced()
                user_choice.user = nuser
                user_choice.orga = Organization.objects.get(name=list[i])
                user_choice.coin = list[i+1]
                user_choice.date = f_date
                user_choice.save()
        return render(req,'create_user_choice.html',context)




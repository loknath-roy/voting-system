from django.shortcuts import render,redirect
import mysql.connector as sql
from django.contrib import messages

ad=''
pwd=''
# Create your views here.
def Login(request):
    global ad,pwd

    # Connecting Database
    if request.method=='POST':
        mysql=sql.connect(host='localhost',user='root',password="root@123",database='signup_info')
        cursor=mysql.cursor()
        ad=request.POST.get('Aadhaar_no')
        pwd=request.POST.get('Password')
        
        c="SELECT * FROM users WHERE Aadhaar_no='{}' AND Password='{}'".format(ad,pwd)
        cursor.execute(c)
        res=tuple(cursor.fetchall())
        #print(res)


        for row in res:
            for col in res:
                if col[8]==None:
                    request.session['ad'] = ad
                    request.session['pwd'] = pwd
                    # print('your aid : ',request.session.get('ad'))
                    # print('your pass : ',request.session.get('pwd'))
                    return render(request,'home.html')
                else:
                    messages.warning(request, "Already voted")
                    return render(request,'login_page.html')  
            
        else:
            messages.warning(request, "Invalid credentials" )
            return render(request,'login_page.html')
                        
    return render(request,'login_page.html')



def Home(request):
    if 'ad' in request.session:
        return render(request,'home.html')
    return redirect('login')


def Logout(request):
    if 'ad' in request.session:
        request.session.flush()
    return redirect('login')

def About(request):
    return render(request,'about.html')

def Vote(request):
    candidate=request.GET.get("data")
    #print(candidate)
    con=sql.connect(host="localhost",user="root",password="root@123",database="signup_info")
    cor=con.cursor()
    cor.execute("update users set Status=1 ,Candidate=%s where Aadhaar_no=%s",tuple((candidate,ad)))
    con.commit()
    con.close()
   
    return redirect('logout')

 
def Result(request):
   
    return render (request,'result.html')










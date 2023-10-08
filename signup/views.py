from django.shortcuts import render,redirect
import mysql.connector as sql
from django.contrib import messages

# Create your views here.

fn=''
ln=''
em=''
ad=''
dob=''
pwd=''
cpwd=''
gn=''

def Registration(request):
    global fn,ln,em,ad,dob,pwd,cpwd,gn
    if request.method=='POST':
        mysql=sql.connect(host='localhost',user='root',password="root@123",database='signup_info')
        cursor=mysql.cursor()
        res=request.POST
        for key,value in res.items():
            
            if key == 'First_name':
                fn=value
            if key == 'Last_name':
                ln=value
            if key == 'Email':
                em=value
            if key == 'Aadhaar_no':
                ad=value
            if key == 'DOB':
                dob=value
            if key == 'Password':
                pwd=value
            if key == 'Confirm_password':
                cpwd=value
            if key == 'Gender':
                gn=value

        if pwd != cpwd:
            messages.warning(request, " Your password and confirm password does not match" )
            return redirect('signup') 
        else:
            data="INSERT INTO users('First_name','Last_name','Email','Aadhaar_no','DOB','Password','Confirm_password,'Gender')values('{}','{}','{}','{}','{}','{}','{}','{}')".format(fn,ln,em,ad,dob,pwd,cpwd,gn)
            cursor.execute(data)
            mysql.commit()
            messages.success(request, "Congratulations! Account created successfully" )
        return redirect('login')


    return render(request,'signup_page.html')



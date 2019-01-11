from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
#importing the models that is classes defined in models.py file
from .models import *

import datetime
import calendar

# Create your views here.
def index(request):
    return render(request,'dtenapp/index.html')

def login(request):
    print ("------------------- login called ----------------------")
    loginmail = request.POST.get('mailid')
    loginpass = request.POST.get('password')
    allpn = Person.objects.all()
    endit = 1
    for i in allpn:
        if i.mailid == loginmail:
            if i.password == loginpass:
                endit = 2
                allsub = Subject.objects.all()
                sublistreturn = []
                for i in allsub:
                    if i.creator == request.POST.get("mailid"):
                        subdict = {"name":i.name,"division":i.division,"department":i.department,"type":i.type_of_subject}
                        sublistreturn.append(subdict)

                alldiv = Division.objects.all()
                divsortout = 1
                for i in alldiv:
                    if i.creator == request.POST.get("mailid"):
                        divdict = {"name":i.name,"department":i.department}
                        divsortout = 2

                if divsortout == 1:
                    divdict = {"name":"no","department":"no"}

                for i in sublistreturn:
                    print (i)     
                return render(request,'dtenapp/teacher.html',{"allsub":sublistreturn,"divdict":divdict})
                sublistreturn = []
        else:
            pass        

    if endit == 1:
        return render(request,'dtenapp/index.html')

def sign(request):
    count = len(Person.objects.all())
    insertcount = count + 1
    if request.POST.get('profession') == "teacher":
        if request.POST.get('enrolkey') == "teacher":
            pn = Person()
            pn.id_person = insertcount
            pn.name = request.POST.get('name')
            pn.surname = request.POST.get('surname')
            pn.mailid = request.POST.get('mailid')
            pn.profession = request.POST.get('profession')
            pn.college = request.POST.get('college')
            pn.password = request.POST.get('password')
            pn.save()

            allsub = Subject.objects.all()
            sublistreturn = []
            for i in allsub:
                if i.creator == request.POST.get("mailid"):
                    sublistreturn.append(i.name)

            for i in sublistreturn:
                print (i)     
        
            return render(request,'dtenapp/teacher.html',{"allsub":sublistreturn})
            sublistreturn = []
        else:
            return render(request,'Dtenapp/index.html')   
    else:
        if request.POST.get('enrolkey') == "student":
            pn = Person()
            pn.id_person = insertcount
            pn.name = request.POST.get('name')
            pn.surname = request.POST.get('surname')
            pn.mailid = request.POST.get('mailid')
            pn.profession = request.POST.get('profession')
            pn.college = request.POST.get('college')
            pn.password = request.POST.get('password')
            pn.save()
            return render(request,'Dtenapp/sign.html')
        else:
            return render(request,'Dtenapp/index.html')   
             
def student(request):
    print (request.POST.get('mailid'))
    allpn = Person.objects.all()
    for i in allpn:
        print (i.mailid)
        if i.mailid == request.POST.get('mailid'):
            print (i.mailid)
            print ("caught")
            i.department = request.POST.get('department')
            i.division = request.POST.get('division')
            print (request.POST.get('department'))
            print (request.POST.get('division'))
            print (i.department)
            print (i.division)
            i.save()
            return render(request,'Dtenapp/student.html')


        #this code is having the error    
        # print (request.POST.get('mailid'))
        # print (i.mailid)
        # if i.mailid == request.POST.get('mailid'):
        #     i.department = request.POST.get('department')
        #     i.division = request.POST.get('division')
        #     i.save()
        #     return render(request,'Dtenapp/student.html')
        # else:
        #     return render(request,'Dtenapp/sign.html')
 
def teacher(request):
    pass           

def profession(request):
    allpn = Person.objects.all()
    for i in allpn:
        if i.mailid == request.POST.get('mailid'):
            i.profession = request.POST.get('profession')
            i.college = request.POST.get('college')
            if request.POST.get('profession') == "student":
                i.department = request.POST.get('department')
                i.division = request.POST.get('division')
                i.save()
                return render(request,'Dtenapp/student.html')
            else:
                i.save() 
                return render(request,'Dtenapp/teacher.html')
        else:
            return render(request,'Dtenapp/sign.html')       
                    
def attend(request):
    name = request.POST.get("name")  
    division = request.POST.get("division")
    department = request.POST.get("department")
    typeofsubject = request.POST.get("type")

    d = datetime.datetime.now()
    k = d.strptime(str(d.hour) + ":" + str(d.minute), "%H:%M")
    print (d.year)
    print (d.month)
    print (d.day)
    dateobj = str(d.day) + "-" + str(d.month) +  "-" + str(d.year) 
    print (dateobj)
    print (k.strftime("%I"))
    print (k.strftime("%M"))
    print (d.second)
    timeobj1 = str(k.strftime("%I")) + ":" + str(k.strftime("%M"))
    print (timeobj1)
    timeobj2 = str(int(k.strftime("%I"))+1) + ":" + str(k.strftime("%M"))
    print (timeobj2)
    print (k.strftime("%p"))
    atd = {"name":name,"division":division,"department":department,"typeofsubject":typeofsubject,"date":dateobj,"time":timeobj1,"time2":timeobj2} 
    print (atd)
    return render(request,'dtenapp/attend.html',{"atd":atd})     

def division(request):
    if request.method == 'POST':
        count = len(Person.objects.all())
        insertcount = count + 1
        subjectlist = ""
        divisionobject = Division()
        divisionobject.id_division = insertcount 
        divisionobject.department = request.POST.get("department")
        divisionobject.name = request.POST.get("subjectname")
        divisionobject.enrol_key  =  request.POST.get("enrolkey")
        divisionobject.creator = request.POST.get("mailid")
        divisionobject.total_students = "null"
        divisionobject.division_dict = subjectlist
        divisionobject.save()
        allsub = Subject.objects.all()
        sublistreturn = []
        for i in allsub:
            if i.creator == request.POST.get("mailid"):
                subdict = {"name":i.name,"division":i.division,"department":i.department,"type":i.type_of_subject}
                sublistreturn.append(subdict)

        alldiv = Division.objects.all()
        divsortout = 1
        for i in alldiv:
            if i.creator == request.POST.get("mailid"):
                divdict = {"name":i.name,"department":i.department}
                divsortout = 2

        if divsortout == 1:
            divdict = {"name":"no","department":"no"}

        for i in sublistreturn:
            print (i)     
        return render(request,'dtenapp/teacher.html',{"allsub":sublistreturn,"divdict":divdict})
        sublistreturn = []

def subject(request):
    if request.method == 'POST':
        subjectobject = Subject()
        subjectobject.department = request.POST.get("department")
        subjectobject.division = request.POST.get("division")
        subjectobject.name = request.POST.get("subjectname")
        subjectobject.creator = request.POST.get("mailid")
        subjectobject.type_of_subject = request.POST.get("type")
        subjectobject.batch = request.POST.get("batch")
        if request.POST.get("type") == "theory":
            subjectobject.total_l_or_p = request.POST.get("tlectures")
        else:
            subjectobject.total_l_or_p = request.POST.get("tpracticales")    
        subjectobject.save()

        alldiv = Division.objects.all()

        for i in alldiv:           
            if i.department == request.POST.get("department"):
                if i.name == request.POST.get("division"):
                    if i.division_dict == "":
                        i.division_dict = i.division_dict +"  "+ request.POST.get("subjectname")
                        i.save()
                    else:
                        i.division_dict = i.division_dict +","+ request.POST.get("subjectname")
                        i.save()

        allsub = Subject.objects.all()
        sublistreturn = []
        for i in allsub:
            if i.creator == request.POST.get("mailid"):
                subdict = {"name":i.name,"division":i.division,"department":i.department,"type":i.type_of_subject}
                sublistreturn.append(subdict)

        alldiv = Division.objects.all()
        divsortout = 1
        for i in alldiv:
            if i.creator == request.POST.get("mailid"):
                divdict = {"name":i.name,"department":i.department}
                divsortout = 2

        if divsortout == 1:
            divdict = {"name":"no","department":"no"}

        for i in sublistreturn:
            print (i)     
        return render(request,'dtenapp/teacher.html',{"allsub":sublistreturn,"divdict":divdict})
        sublistreturn = []
 
def stddata(request):
    if request.method == 'POST':
        stddataobject = stddata()
        stddataobject.department = request.POST.get("department")
        stddataobject.division = request.POST.get("division")
        stddataobject.save()
        return render(request,'dtenapp/student.html')            

def present(request):
    if request.method == "POST":
        attendobj = Attend()
        attendobj.department = request.POST.get("department")
        attendobj.division = request.POST.get("division")
        attendobj.subject = request.POST.get("name")
        attendobj.date = request.POST.get("date")
        attendobj.time = request.POST.get("time")
        attendobj.present_list = request.POST.get("present")
        attendobj.save()
        allsub = Subject.objects.all()
        sublistreturn = []
        for i in allsub:
            if i.creator == request.POST.get("mailid"):
                subdict = {"name":i.name,"division":i.division,"department":i.department,"type":i.type_of_subject}
                sublistreturn.append(subdict)

        alldiv = Division.objects.all()
        divsortout = 1
        for i in alldiv:
            if i.creator == request.POST.get("mailid"):
                divdict = {"name":i.name,"department":i.department}
                divsortout = 2

        if divsortout == 1:
            divdict = {"name":"no","department":"no"}

        for i in sublistreturn:
            print (i)     
        return render(request,'dtenapp/teacher.html',{"allsub":sublistreturn,"divdict":divdict})
        sublistreturn = []

def absent(request):
    if request.method == "POST":
        attendobj = Attend()
        attendobj.department = request.POST.get("department")
        attendobj.division = request.POST.get("division")
        attendobj.subject = request.POST.get("name")
        attendobj.date = request.POST.get("date")
        attendobj.time = request.POST.get("time")
        attendobj.absent_list = request.POST.get("absent")
        attendobj.save()
        allsub = Subject.objects.all()
        sublistreturn = []
        for i in allsub:
            if i.creator == request.POST.get("mailid"):
                subdict = {"name":i.name,"division":i.division,"department":i.department,"type":i.type_of_subject}
                sublistreturn.append(subdict)

        alldiv = Division.objects.all()
        divsortout = 1
        for i in alldiv:
            if i.creator == request.POST.get("mailid"):
                divdict = {"name":i.name,"department":i.department}
                divsortout = 2

        if divsortout == 1:
            divdict = {"name":"no","department":"no"}

        for i in sublistreturn:
            print (i)     
        return render(request,'dtenapp/teacher.html',{"allsub":sublistreturn,"divdict":divdict})
        sublistreturn = []

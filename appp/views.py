from django.shortcuts import render

# Create your views here.
def func1(request):
    result=None
    if request.method=="POST":
        a=request.POST.get('num')
        b=int(a)
        if b>1:
            for i in range(1, (b//2)+1):
                if (b%i)==0:
                    result=False
                    break
                else:
                    result=True 
        else:
            result=False 
            
      
    return render(request,'index3.html',{'res': result})

def func2(request):
    result=None
    if request.method=="POST":
        a=request.POST.get('num1')
        b=request.POST.get('num2')
        c=int(a)
        d=int(b)
        if c>=d:
            result=True
        else:
            result=False
    return render(request,'index4.html',{'res':result})

def func3(request):
    result=None
    if request.method=="POST":
        a=request.POST.get('num')
      
        sum=0
        n=len(str(a))
        tem = int(a)
        while tem>0:
            digit=tem%10
            sum+= digit**n
            tem//=10
        if a== sum:
            result=True
        else:
            result=False

    return render(request,'armstrong.html',{'res':result})

d={'marks':[{'name':'MADHU','pinno':'224g5a0209','passsub':15,'failsub':0,'attendence':95},
{'name':'MANIKANTA','pinno':'224g5a0210','passsub':14,'failsub':1,'attendence':96},
{'name':'MUSTAQ','pinno':'224g5a0211','passsub':9,'failsub':6,'attendence':73},
{'name':'MYTHRI','pinno':'224g5a0212','passsub':13,'failsub':2,'attendence':90},
{'name':'NANDEESWAR','pinno':'224g5a0213','passsub':15,'failsub':0,'attendence':94},
{'name':'NARESH REDDY','pinno':'224g5a0214','passsub':8,'failsub':7,'attendence':70}]}


def func4(request):
    d={'marks':[{'name':'MADHU','pinno':'224g5a0209','passsub':15,'failsub':0,'attendence':95},
{'name':'MANIKANTA','pinno':'224g5a0210','passsub':14,'failsub':1,'attendence':96},
{'name':'MUSTAQ','pinno':'224g5a0211','passsub':9,'failsub':6,'attendence':73},
{'name':'MYTHRI','pinno':'224g5a0212','passsub':13,'failsub':2,'attendence':90},
{'name':'NANDEESWAR','pinno':'224g5a0213','passsub':15,'failsub':0,'attendence':94},
{'name':'NARESH REDDY','pinno':'224g5a0214','passsub':8,'failsub':7,'attendence':70}]}

    result=None
    if request.method=="POST":
        a=request.POST.get('pinno')
        for i in d.get('marks'):
            if a==i.get('pinno'):
                result=i
                break
        print(result)
        return render(request,'exams.html',result) 
    return render(request,'exams.html',result)                
                
    
            




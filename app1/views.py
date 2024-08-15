from django.shortcuts import render

# Create your views here.
def func1(request):
    result=None
    if request.method=="POST":
        a=request.POST.get('num')
        b=int(a)
        print(b)
        if b%2==0:
            result=True
        else:
            result=False    
    return render(request,'index.html',{'res': result})

def func2(request):
    a=request.POST.get('sname')
    r="hi,  " + a
    print(r)
    return render(request,'index2.html',{'res':r})
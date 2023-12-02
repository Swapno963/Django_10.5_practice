from django.shortcuts import render

# Create your views here.
def home(request):
    d = {'author':'swapno mondol','lst':[1,2,4,2,4],
         'txt':['This','is','diffrent','text'],
         'may_empty':'',
         'firs_cap':'my first letter is not uppercase.'
         
         }
    return render(request,'index.html',d)
import re
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html', {'hbar':'home'})
def about(request):
    return render(request, 'about.html', {'abar':'about'})
def kor(request):
    return render(request, 'kor.html', {'kbar':'kor'})
def eng(request):
    return render(request, 'eng.html', {'ebar':'eng'})

def result(request):
            text = request.GET['fulltext']
            hangul = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+')
            result = hangul.sub('',text)
            anoder_result = hangul.findall(text)
            
            d = re.compile('[^0-9]')

            r = d.sub('',text) 



            return render(request, 'result.html', {'full':text , 're':result, 'a':r})

def result_han(request):
    
    return render(request, 'request_han.html', {'gbar':'result_han'})


def result_eng(request):
    return render(request, 'request_eng.html', {'ebar':'result_eng'})
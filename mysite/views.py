from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    # check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    charcount = request.POST.get('charcount','off')

    # check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()[]{};:'".\,<>/?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Remove punctuations','analyze_text': analyzed}
        djtext = analyzed
    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Full text caps','analyze_text':analyzed}
        djtext = analyzed
        
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose':'remove new lines','analyze_text':analyzed}
        djtext = analyzed

    if spaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Remover','analyze_text':analyzed}
        djtext = analyzed
    
    if charcount == 'on':
        counter = str(len(djtext))
        counter = f"Number of character in Text is {counter}"
        params = {'purpose':'Count Characters in Text','analyze_text':djtext, 'count':counter}

    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on" and charcount != "on":
        return HttpResponse("Error")

    return render(request,'analyze.html', params)
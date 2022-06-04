
import operator
from django.shortcuts import render


def home(request):
    return render(request, 'word_count/index.html')


def count(request):
    fulltext = request.GET['text']
    text = request.GET['text'].split()
    word_number = len(text)
    dicoword = {}
    
    for word in text:
        if word in dicoword:
            dicoword[word] += 1
        else:
            dicoword[word] = 1
    
    context = {
        'n': word_number,
        'words': sorted(dicoword.items(), key= operator.itemgetter(1), reverse=True),
        'text': fulltext
    }
    return render(request, 'word_count/count.html', context=context)

def about(request):
    return render(request, 'word_count/about.html')
from django.shortcuts import render
from .models import Test

# Create your views here.
def test_list(request):
    thetests = Test.objects.all().order_by('date')
    return render(request,'thetest/testlist.html', {
        'thetests':thetests
    })
    
def single_test(request,slug):
    test = Test.objects.get(slug=slug)
    return render(request, 'thetest/thetest.html', {
        'test':test
    })
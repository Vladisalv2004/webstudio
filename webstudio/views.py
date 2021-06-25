from django.shortcuts import render
from .forms import OrderForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect




def main_page(request):
    return render(request,'webstudio/main_page.html',{})

def order_new(request):

    if request.method == 'POST':
        # если метод POST, проверим форму и отправим письмо
        form = OrderForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            send_mail(f'{subject} от {from_email}', message,"вставь сюда нужны email", "сюда тот же самый  email")

            return redirect('main_page')
    else:
        form = OrderForm()
    return render(request,'webstudio/order_new.html',{'form':form})

# Create your views here.

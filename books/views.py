from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Book

from django.core.mail import send_mail
from django.http  import HttpResponseRedirect

from books.forms import ContactForm

from django.http import Http404
from django.template import TemplateDoesNotExist
#from django.views.generic.simple import direct_to_template

def hello(request):
    return HttpResponse("Welcome to the page at %s" %request.path)

def ua_display(request):
    ua = request.META.get('HTTP_USER_AGENTT','unknown')
    return HttpResponse("Your browser is %s" %ua)

#def search_form(request):
#    return render_to_response('search_form.html')

#def search(request):
#    if 'q' in request.GET and request.GET['q']:
#        q = request.GET['q']
#        books = Book.objects.filter(title__icontains =q)
#        return render_to_response('search_results.html',{'books':books,'query':q})
#        
#    else:
#        return render_to_response('search_form.html',{'error':True})


#def search(request):
#    errors = []
#    if 'q' in request.GET:
#        q = request.GET['q']
#        if not q:
#            errors.append('Enter a search term.')
#        elif len(q) > 20:
#            errors.append('please enter at most 20 characters.')
#        else:    
#            books = Book.objects.filter(title__icontains =q)
#            return render_to_response('search_results.html',{'books':books,'query':q})
#    return render_to_response('search_form.html',{'errors':errors})    
#
#
#def contact(request):
#    errors = []
#    if request.method =='POST':
#        
#        if not request.POST.get('subject',''):
#            errors.append('Enter a subject.')
#        if not request.POST.get('message',''):
#            errors.append('Enter a message.')
#        if request.POST.get('email') and '@' not in request.POST['email']:
#            errors.append('Enter a valid e-mail address.')
#        if not errors:
#            send_mail(
#                    request.POST['subject'],
#                    request.POST['message'],
#                    request.POST.get('email','noreply@example.com'),
#                    ['709580504@qq.com'],
#                    )
#            return HttpResponseRedirect('/contact/thanks/')
#    return render_to_response('contact_form.html',
#                         {"errors":errors,
#                          'subject':request.POST.get('subject',''),
#                          'message':request.POST.get('message',''),
#                          'mail':request.POST.get('email',''),})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                    cd['subject'],
                    cd['message'],
                    cd.get('email','xuyuan10002720@163.com'),
                    ['xuyuan.xy@alibaba-inc.com'],
           )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
                initial={ 'subject':'I love you !'}
                )
    return render_to_response('contact_form.html',{'form':form})


#def aoubt_pages(request,page):
#    try:
#        return direct_to_template(request,template="about/%s.html" %page)
#    except:TemplateDoesNoteExist:
#        raise Http404()

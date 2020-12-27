from django.shortcuts import render
from django.http import JsonResponse
from .forms import FormDatas
from .models import FacultyData, PercentageData
from django.views.generic import TemplateView
# Create your views here.

# def hello(request):

#     return render(request, 'index.html')


# def create_post(request):
#     posts = Data.objects.all()
#     response_data = {}

#     if request.POST.get('action') == 'post':
#         name = request.POST.get('name')
#         email = request.POST.get('email')

#         response_data['name'] = name
#         response_data['email'] = email

#         Data.objects.create(
#             name= name,
#             email = email,
#             )
#         return JsonResponse(response_data)    

#     return render(request, 'index.html', {'posts':posts})            



# def add_data(request):
#     form = FormDatas(request.POST or None)
#     data = {}
#     if request.is_ajax():
#         if form.is_valid():
#             form.save()
#             data['email'] = form.cleaned_data.get('email')
#             data['status'] = 'ok'
#             return JsonResponse(data)
#     context = {
#         'form': form
#     }
#     return render(request, 'index.html', context)


def add_data(request):
    if request.method == "POST":
        form = FormDatas(request.POST or None)
        data = {}
        if request.is_ajax():
            if form.is_valid():
                form.save()
                data['status'] = 'ok! success'
                return JsonResponse(data)
                form = FormDatas()
    else:
        form = FormDatas()

    context = {
        'form': form,
    }
    return render(request, 'index.html', context)

# def add_another_data(request):
#     if request.method == "POST":
#         fm = AnotherFormDatas(requeest.POST)
#         if fm.is_valid():
#             fm.save()
#             fm = AnotherFormDatas()
#     else: 
#         fm = AnotherFormDatas()

#     return render(request, 'index.html', {'fm': fm})    


class Contact(TemplateView):
    template_name = "contact.html"



# def get_program_data(request):        ``
#     qs_val = list(FacultyData.objects.values())
#     return JsonResponse({"data": qs_val})

# def get_percentage_data(request):
#     qs_val = list(PercentageData.objects.values())
#     return JsonResponse({"data": qs_val})


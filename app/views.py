from django.shortcuts import render
from django.http import JsonResponse
from .forms import FormDatas

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
        form = FormDatas(request.POST)
        data = {}
        if request.is_ajax():
            if form.is_valid():
                form.save()
                data['email'] = form.cleaned_data.get('email')
                data['status'] = 'ok'
                return JsonResponse(data)
                form = FormDatas()
    else:
        form = FormDatas()

    context = {
        'form': form
    }
    return render(request, 'index.html', context)
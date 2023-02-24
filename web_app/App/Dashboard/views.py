from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from AstralObject.models import Astral

# Create your views here.
@login_required()
def dashboardView(request):
    if request.method == 'POST':
        ultraviolet = request.POST.get('ultraviolet')
        green = request.POST.get('green')
        near = request.POST.get('near')
        red = request.POST.get('red')
        infrared = request.POST.get('infrared')
        julian = request.POST.get('julian')
        spectroscopic = request.POST.get('spectroscopic')
        redshift = request.POST.get('redshift')
        plate = request.POST.get('plate')

        new_object = Astral(
            created_by=str(request.user),
            ultraviolet_filter=ultraviolet,
            green_filter=green,
            near_infrared_filter=near,
            red_filter=red,
            infrared_filter=infrared,
            modified_julian_date=julian,
            spectroscopic_objects_id=spectroscopic,
            redshift_value=redshift,
            plate_id=plate,
        )
        new_object.save()
        # After
        return redirect('checkView', new_object.astral_id)

    return render(request, 'dashboard.html')


def resultView(request):
    userResult = Astral.objects.filter(created_by=str(request.user)).values()
    context = {
        'results': userResult,
    }
    return render(request, 'results.html', context)


def delete(request, id):
    member = Astral.objects.get(astral_id=id)
    member.delete()
    return redirect('resultView')

# Here we get the info about the model , so we can work with datas.
def checkView(request, id):
    result = Astral.objects.get(astral_id=id)
    context = {
        'result': result,
    }
    return render(request, 'finalResult.html')
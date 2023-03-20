from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from AstralObject.models import Astral

import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')
# model = pickle.load(open("web_app/App/Dashboard/Models/model.pkl", "rb"))
# scaler = pickle.load(open("web_app/App/Dashboard/Models/scaler.pkl", "rb"))
# pca = pickle.load(open("web_app/App/Dashboard/Models/pca.pkl", "rb"))

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("models/pca.pkl", "rb") as f:
    pca = pickle.load(f)

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

        new_data = pd.DataFrame({'u': [ultraviolet],
                                 'g': [green],
                                 'r': [red],
                                 'i': [infrared],
                                 'z': [near],
                                 'spec_obj_ID': [spectroscopic],
                                 'redshift': [redshift],
                                 'plate': [plate],
                                 'MJD': [julian]})
        new_data_scaled = scaler.transform(new_data)
        new_data_pca = pca.transform(new_data_scaled)

        prediction = model.predict(new_data_pca)[0]

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
            prediction=prediction,
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


# Here we get the info about the model , so we can work with data.
def checkView(request, id):
    result = Astral.objects.get(astral_id=id)
    context = {
        'result': result,
    }
    return render(request, 'finalResult.html')


def get_prediction(ultraviolet, green, near, red, infrared, julian, spectroscopic, redshift, plate):
    # load necessary objects for prediction
    model = pickle.load(open("data/model.pkl", "rb"))
    scaler = pickle.load(open("data/scaler.pkl", "rb"))
    pca = pickle.load(open("data/pca.pkl", "rb"))

    # input the data into a dataframe
    new_data = pd.DataFrame({'u': [ultraviolet],
                             'g': [green],
                             'r': [red],
                             'i': [infrared],
                             'z': [near],
                             'spec_obj_id': [spectroscopic],
                             'redshift': [redshift],
                             'plate': [plate],
                             'mjd': [julian]})

    # scale and pca the data
    new_data_scaled = scaler.transform(new_data)
    new_data_pca = pca.transform(new_data_scaled)

    # make the prediction
    prediction = model.predict(new_data_pca)

    return str(predicted_class[0])
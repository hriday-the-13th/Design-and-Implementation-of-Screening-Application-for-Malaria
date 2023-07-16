from django.shortcuts import render
from .models import image_classification
from django.http import HttpResponseRedirect
from .py_templates.my_model import get_prediction

def home(request):
    print('Predicting Image')
    images = image_classification.objects.all()
    latest_image = images.last()
    
    if latest_image:
        url = latest_image.pic.url
    else:
        url = "placeholder image url"
    
    try:
        prediction = get_prediction(url)
        label_mapping = {0: 'Parasitized', 1: 'Uninfected'}
        out = label_mapping.get(prediction.item(), 'Unknown')
        
        return render(request, 'home.html', {'print': out, 'url': url})
    
    except Exception as e:
        return render(request, 'home.html', {'print': 'Please Upload A photo', 'url': url})

def uploadImage(request):
    print('Image Handling')
    
    try:
        img = request.FILES['image']
        image = image_classification(pic=img)
        image.save()
        return HttpResponseRedirect('/')
    
    except Exception as e:
        # Handle image upload error
        return render(request, 'home.html', {'print': 'Image Upload Error', 'url': "placeholder image url"})

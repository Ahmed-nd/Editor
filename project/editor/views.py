from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from . import util
from django.conf import settings
import requests
import json
from PIL import Image
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib
import string, random


def postData(url, data):
    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }

    return requests.request("POST", url, headers=headers, data=payload)


def arrayToImageRGB(response):
    r = response.json()['lhs']
    if len(r[1]["mwdata"]) != 1:
        imgnpR = np.asarray(r[0]["mwdata"], dtype=np.uint8).reshape(
            (r[0]['mwsize'][1], r[0]['mwsize'][0]))
        imgnpG = np.asarray(r[1]["mwdata"], dtype=np.uint8).reshape(
            (r[0]['mwsize'][1], r[0]['mwsize'][0]))
        imgnpB = np.asarray(r[2]["mwdata"], dtype=np.uint8).reshape(
            (r[0]['mwsize'][1], r[0]['mwsize'][0]))
        imgnpRGB = np.dstack((imgnpR, imgnpG, imgnpB))
    else:
        imgnpRGB = imgnpR = np.asarray(r[0]["mwdata"], dtype=np.uint8).reshape(
            (r[0]['mwsize'][1], r[0]['mwsize'][0]))
    imgnpRGB = np.rot90(np.fliplr(imgnpRGB), 1)
    return Image.fromarray(imgnpRGB)


def drawChart(title, xlabel, ylabel, values, save):
    x = np.arange(len(values))
    fig, ax = plt.subplots(figsize=(5, 5))
    width = 0.2
    ax.bar(x, values, color='black')
    ax.set_title(title, fontsize=12)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    fig.savefig(save)
    plt.close(fig)

def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

MLfunctions = [
    "Brightness",
    "addTwoImages",
    "Butterworth_HPF",
    "Butterworth_LPF",
    "Contrast",
    "Dir_Ord_Resize",
    "edge_detection",
    "Gamma",
    "GaussianFilter",
    "Gaussian_HPF",
    "Gaussian_LPF",
    "Gray",
    "Ideal_HPF",
    "Ideal_LPF",
    "MaxFilter",
    "MeanFilter",
    "Median",
    "Histogram",
    "MidpoFilter",
    "MinFilter",
    "Negative",
    "Reverse_0_order",
    "Reverse_with_order_1",
    # "sharp_image",
    "subTwoImages",
    "unsharp_algorithm",
]


def index(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        image_url = util.media_save(upload.name, upload)
        return render(request, 'editor/index.html', {
            'selectedImages': util.list_media(),
            'MLfunctions': MLfunctions})
    return render(request, 'editor/index.html', {
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions})


def closeAll(request):
    for name in util.list_media():
        util.media_delete(name)
    return HttpResponseRedirect('/')


def selectImg(request, name):
    return render(request, 'editor/index.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions,
        'image_info': util.media_info('./media/' + name)})


def closeImg(request, name):
    if util.media_delete(name):
        return HttpResponseRedirect('/')

# 1 value


def Brightness(request, name):
    if request.method == 'POST' and request.POST['value']:
        try:
            response = postData("http://localhost:9910/Functions/Brightness", {
                "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }", int(request.POST['value'])]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        
        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        if request.POST['submit'] == "Preview":
            return render(request, 'editor/brightness.html', {
                'image_url': f'/media/{name}',
                'selectedImages': util.list_media(),
                'MLfunctions': MLfunctions,
                'image_info': util.media_info('./media/' + name)})
        elif request.POST['submit'] == "Ok":
            return HttpResponseRedirect('/')
    return render(request, 'editor/brightness.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'image_info': util.media_info('./media/' + name)})


def Gamma(request, name):
    if request.method == 'POST' and request.POST['value']:
        try:
            response = postData("http://localhost:9910/Functions/Gamma", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }", float(request.POST['value'])]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        
        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        if request.POST['submit'] == "Preview":
            return render(request, 'editor/Gamma.html', {
                'image_url': f'/media/{name}',
                'selectedImages': util.list_media(),
                'MLfunctions': MLfunctions,
                'image_info': util.media_info('./media/' + name)})
        elif request.POST['submit'] == "Ok":
            return HttpResponseRedirect('/')
    return render(request, 'editor/Gamma.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'image_info': util.media_info('./media/' + name)})


def Butterworth_HPF(request, name):
    if request.method == 'POST' and request.POST['value']:
        try:
            response = postData("http://localhost:9910/Functions/Butterworth_HPF", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }", int(request.POST['value'])]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        
        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        if request.POST['submit'] == "Preview":
            return render(request, 'editor/Butterworth_HPF.html', {
                'image_url': f'/media/{name}',
                'selectedImages': util.list_media(),
                'MLfunctions': MLfunctions,
                'image_info': util.media_info('./media/' + name)})
        elif request.POST['submit'] == "Ok":
            return HttpResponseRedirect('/')
    return render(request, 'editor/Butterworth_HPF.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'image_info': util.media_info('./media/' + name)})


def Butterworth_LPF(request, name):
    if request.method == 'POST' and request.POST['value']:
        try:
            response = postData("http://localhost:9910/Functions/Butterworth_LPF", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }", int(request.POST['value'])]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        
        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        if request.POST['submit'] == "Preview":
            return render(request, 'editor/Butterworth_LPF.html', {
                'image_url': f'/media/{name}',
                'selectedImages': util.list_media(),
                'MLfunctions': MLfunctions,
                'image_info': util.media_info('./media/' + name)})
        elif request.POST['submit'] == "Ok":
            return HttpResponseRedirect('/')
    return render(request, 'editor/Butterworth_LPF.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'image_info': util.media_info('./media/' + name)})


def Gaussian_HPF(request, name):
    if request.method == 'POST' and request.POST['value']:
        try:
            response = postData("http://localhost:9910/Functions/Gaussian_HPF", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }", int(request.POST['value'])]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        
        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        if request.POST['submit'] == "Preview":
            return render(request, 'editor/Gaussian_HPF.html', {
                'image_url': f'/media/{name}',
                'selectedImages': util.list_media(),
                'MLfunctions': MLfunctions,
                'image_info': util.media_info('./media/' + name)})
        elif request.POST['submit'] == "Ok":
            return HttpResponseRedirect('/')
    return render(request, 'editor/Gaussian_HPF.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'image_info': util.media_info('./media/' + name)})


def Gaussian_LPF(request, name):
    if request.method == 'POST' and request.POST['value']:
        try:
            response = postData("http://localhost:9910/Functions/Gaussian_LPF", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }", int(request.POST['value'])]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        
        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        if request.POST['submit'] == "Preview":
            return render(request, 'editor/Gaussian_LPF.html', {
                'image_url': f'/media/{name}',
                'selectedImages': util.list_media(),
                'MLfunctions': MLfunctions,
                'image_info': util.media_info('./media/' + name)})
        elif request.POST['submit'] == "Ok":
            return HttpResponseRedirect('/')
    return render(request, 'editor/Gaussian_LPF.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'image_info': util.media_info('./media/' + name)})


def Ideal_HPF(request, name):
    if request.method == 'POST' and request.POST['value']:
        try:
            response = postData("http://localhost:9910/Functions/Ideal_HPF", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }", int(request.POST['value'])]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        
        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        if request.POST['submit'] == "Preview":
            return render(request, 'editor/Ideal_HPF.html', {
                'image_url': f'/media/{name}',
                'selectedImages': util.list_media(),
                'MLfunctions': MLfunctions,
                'image_info': util.media_info('./media/' + name)})
        elif request.POST['submit'] == "Ok":
            return HttpResponseRedirect('/')
    return render(request, 'editor/Ideal_HPF.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'image_info': util.media_info('./media/' + name)})


def Ideal_LPF(request, name):
    if request.method == 'POST' and request.POST['value']:
        try:
            response = postData("http://localhost:9910/Functions/Ideal_LPF", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }", int(request.POST['value'])]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        
        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        if request.POST['submit'] == "Preview":
            return render(request, 'editor/Ideal_LPF.html', {
                'image_url': f'/media/{name}',
                'selectedImages': util.list_media(),
                'MLfunctions': MLfunctions,
                'image_info': util.media_info('./media/' + name)})
        elif request.POST['submit'] == "Ok":
            return HttpResponseRedirect('/')
    return render(request, 'editor/Ideal_LPF.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'image_info': util.media_info('./media/' + name)})

# 1 image


def addTwoImages(request, name):
    if request.method == 'POST' and request.POST['selectedImage']:
        try:
            response = postData("http://localhost:9910/Functions/addTwoImages", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }", f"http://127.0.0.1:8000/media/{ request.POST['selectedImage']}"]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        
        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        if request.POST['submit'] == "Preview":
            return render(request, 'editor/addTwoImages.html', {
                'image_url': f'/media/{name}',
                'selectedImages': util.list_media(),
                'MLfunctions': MLfunctions,
                'image_info': util.media_info('./media/' + name)})
        elif request.POST['submit'] == "Ok":
            return HttpResponseRedirect('/')

    return render(request, 'editor/addTwoImages.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'image_info': util.media_info('./media/' + name)})


def subTwoImages(request, name):
    if request.method == 'POST' and request.POST['selectedImage']:
        try:
            response = postData("http://localhost:9910/Functions/addTwoImages", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }", f"http://127.0.0.1:8000/media/{ request.POST['selectedImage']}"]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        
        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        if request.POST['submit'] == "Preview":
            return render(request, 'editor/subTwoImages.html', {
                'image_url': f'/media/{name}',
                'selectedImages': util.list_media(),
                'MLfunctions': MLfunctions,
                'image_info': util.media_info('./media/' + name)})
        elif request.POST['submit'] == "Ok":
            return HttpResponseRedirect('/')
    return render(request, 'editor/subTwoImages.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'image_info': util.media_info('./media/' + name)})

# 2 input


def Reverse_0_order(request, name):
    if request.method == 'POST' and request.POST['width'] and request.POST['height']:
        try:
            response = postData("http://localhost:9910/Functions/Reverse_0_order", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }", int(request.POST['width']), int(request.POST['height'])]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        
        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        if request.POST['submit'] == "Preview":
            return render(request, 'editor/Reverse_0_order.html', {
                'image_url': f'/media/{name}',
                'selectedImages': util.list_media(),
                'MLfunctions': MLfunctions,
                'image_info': util.media_info('./media/' + name)})
        elif request.POST['submit'] == "Ok":
            return HttpResponseRedirect('/')
    return render(request, 'editor/Reverse_0_order.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'image_info': util.media_info('./media/' + name)})


def Reverse_with_order_1(request, name):
    if request.method == 'POST' and request.POST['width'] and request.POST['height']:
        try:
            response = postData("http://localhost:9910/Functions/Reverse_with_order_1", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }", int(request.POST['width']), int(request.POST['height'])]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        
        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        if request.POST['submit'] == "Preview":
            return render(request, 'editor/Reverse_with_order_1.html', {
                'image_url': f'/media/{name}',
                'selectedImages': util.list_media(),
                'MLfunctions': MLfunctions,
                'image_info': util.media_info('./media/' + name)})
        elif request.POST['submit'] == "Ok":
            return HttpResponseRedirect('/')
    return render(request, 'editor/Reverse_with_order_1.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'image_info': util.media_info('./media/' + name)})


def Dir_Ord_Resize(request, name):
    if request.method == 'POST' and request.POST['scal']:
        try:
            response = postData("http://localhost:9910/Functions/Dir_Ord_Resize", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }", int(request.POST['scal'])]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        
        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        if request.POST['submit'] == "Preview":
            return render(request, 'editor/Dir_Ord_Resize.html', {
                'image_url': f'/media/{name}',
                'selectedImages': util.list_media(),
                'MLfunctions': MLfunctions,
                'image_info': util.media_info('./media/' + name)})
        elif request.POST['submit'] == "Ok":
            return HttpResponseRedirect('/')
    return render(request, 'editor/Dir_Ord_Resize.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'image_info': util.media_info('./media/' + name)})

# 0


def Contrast(request, name):
    try:
        response = postData("http://localhost:9910/Functions/Contrast", {
        "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }"]})
        returnImage = arrayToImageRGB(response)     
    except:
        print(response.json())
        return HttpResponseRedirect('/')
    

    util.media_delete(name)
    returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
    return render(request, 'editor/index.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions,
        'image_info': util.media_info('./media/' + name)})


def edge_detection(request, name):
    try:
        response = postData("http://localhost:9910/Functions/edge_detection", {
        "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }"]})
        returnImage = arrayToImageRGB(response)     
    except:
        print(response.json())
        return HttpResponseRedirect('/')
    

    util.media_delete(name)
    returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
    return render(request, 'editor/index.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions,
        'image_info': util.media_info('./media/' + name)})


def GaussianFilter(request, name):
    try:
        response = postData("http://localhost:9910/Functions/GaussianFilter", {
        "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }"]})
        returnImage = arrayToImageRGB(response)     
    except:
        print(response.json())
        return HttpResponseRedirect('/')
    

    util.media_delete(name)
    returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
    return render(request, 'editor/index.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions,
        'image_info': util.media_info('./media/' + name)})


def Gray(request, name):
    try:
        response = postData("http://localhost:9910/Functions/Gray", {
        "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }"]})
        returnImage = arrayToImageRGB(response)     
    except:
        print(response.json())
        return HttpResponseRedirect('/')
    

    util.media_delete(name)
    returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
    return render(request, 'editor/index.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions,
        'image_info': util.media_info('./media/' + name)})


def MaxFilter(request, name):
    try:    
        response = postData("http://localhost:9910/Functions/MaxFilter", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }"]})
        returnImage = arrayToImageRGB(response) 
    except:
        print(response.json())
        return HttpResponseRedirect('/')
    

    util.media_delete(name)
    returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
    return render(request, 'editor/index.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions,
        'image_info': util.media_info('./media/' + name)})


def MeanFilter(request, name):
    if request.method == 'GET':
        try:
            response = postData("http://localhost:9910/Functions/MeanFilter", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }"]})
            returnImage = arrayToImageRGB(response)     
        except:
            print(response.json())
            return HttpResponseRedirect('/')
        

        util.media_delete(name)
        returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
        return render(request, 'editor/index.html', {
            'image_url': f'/media/{name}',
            'selectedImages': util.list_media(),
            'MLfunctions': MLfunctions,
            'image_info': util.media_info('./media/' + name)})


def Median(request, name):
    try:
        response = postData("http://localhost:9910/Functions/Median", {
        "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }"]})
        returnImage = arrayToImageRGB(response)     
    except:
        print(response.json())
        return HttpResponseRedirect('/')
    

    util.media_delete(name)
    returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
    return render(request, 'editor/index.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions,
        'image_info': util.media_info('./media/' + name)})


def MidpoFilter(request, name):
    try:    
        response = postData("http://localhost:9910/Functions/MidpoFilter", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }"]})
        returnImage = arrayToImageRGB(response) 
    except:
        print(response.json())
        return HttpResponseRedirect('/')
        

    util.media_delete(name)
    returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
    return render(request, 'editor/index.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions,
        'image_info': util.media_info('./media/' + name)})


def MinFilter(request, name):
    try:    
        response = postData("http://localhost:9910/Functions/MinFilter", {
            "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }"]})
        returnImage = arrayToImageRGB(response) 
    except:
        print(response.json())
        return HttpResponseRedirect('/')
    

    util.media_delete(name)
    returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
    return render(request, 'editor/index.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions,
        'image_info': util.media_info('./media/' + name)})


def Negative(request, name):
    try:
        response = postData("http://localhost:9910/Functions/Negative", {
        "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }"
        ]})
        returnImage = arrayToImageRGB(response)     
    except:
        print(response.json())
        return HttpResponseRedirect('/')
    

    util.media_delete(name)
    returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
    return render(request, 'editor/index.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions,
        'image_info': util.media_info('./media/' + name)})


def sharp_image(request, name):
    try:
        response = postData("http://localhost:9910/Functions/sharp_image", {
        "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }"]})
        returnImage = arrayToImageRGB(response)     
    except:
        print(response.json())
        return HttpResponseRedirect('/')
    

    util.media_delete(name)
    returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
    return render(request, 'editor/index.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions,
        'image_info': util.media_info('./media/' + name)})


def unsharp_algorithm(request, name):
    try:
        response = postData("http://localhost:9910/Functions/unsharp_algorithm", {
        "nargout": 3, "rhs": [f"http://127.0.0.1:8000/media/{ name }"]})
        returnImage = arrayToImageRGB(response)     
    except:
        print(response.json())
        return HttpResponseRedirect('/')
    

    util.media_delete(name)
    returnImage.save(settings.MEDIA_ROOT + "\\" + name, 'JPEG')
    return render(request, 'editor/index.html', {
        'image_url': f'/media/{name}',
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions,
        'image_info': util.media_info('./media/' + name)})


def Histogram(request, name):
    try:
        response = postData("http://localhost:9910/Functions/Histogram", {
        "nargout": 1, "rhs": [f"http://127.0.0.1:8000/media/{ name }"]})  
        newName = 'histogram_'+random_char(3) +'_'+ name
        returnImage = drawChart(f"Histogram ({name})", "Pixels",
                            "Pixels Level", response.json()['lhs'][0]["mwdata"], settings.MEDIA_ROOT + "\\" +newName )
    except:
        print(response.json())
        return HttpResponseRedirect('/')
    
    return render(request, 'editor/index.html', {
        'image_url': f'/media/{newName}',
        'selectedImages': util.list_media(),
        'MLfunctions': MLfunctions,
        'image_info': util.media_info('./media/' + newName)})

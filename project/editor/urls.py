from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("s=<str:name>/close", views.closeImg, name="closeImg"),
    path("closeAll", views.closeAll, name="closeAll"),
    path("s=<str:name>", views.selectImg, name="selectImg"),
    path("s=<str:name>/Brightness", views.Brightness, name="Brightness"),
    path("s=<str:name>/addTwoImages", views.addTwoImages, name="addTwoImages"),
    path("s=<str:name>/Butterworth_HPF", views.Butterworth_HPF, name="Butterworth_HPF"),
    path("s=<str:name>/Butterworth_LPF", views.Butterworth_LPF, name="Butterworth_LPF"),
    path("s=<str:name>/Contrast", views.Contrast, name="Contrast"),
    path("s=<str:name>/Dir_Ord_Resize", views.Dir_Ord_Resize, name="Dir_Ord_Resize"),
    path("s=<str:name>/edge_detection", views.edge_detection, name="edge_detection"),
    path("s=<str:name>/Gamma", views.Gamma, name="Gamma"),
    path("s=<str:name>/GaussianFilter", views.GaussianFilter, name="GaussianFilter"),
    path("s=<str:name>/Gaussian_HPF", views.Gaussian_HPF, name="Gaussian_HPF"),
    path("s=<str:name>/Gaussian_LPF", views.Gaussian_LPF, name="Gaussian_LPF"),
    path("s=<str:name>/Gray", views.Gray, name="Gray"),
    path("s=<str:name>/Ideal_HPF", views.Ideal_HPF, name="Ideal_HPF"),
    path("s=<str:name>/Ideal_LPF", views.Ideal_LPF, name="Ideal_LPF"),
    path("s=<str:name>/MaxFilter", views.MaxFilter, name="MaxFilter"),
    path("s=<str:name>/MeanFilter", views.MeanFilter, name="MeanFilter"),
    path("s=<str:name>/Median", views.Median, name="Median"),
    path("s=<str:name>/MidpoFilter", views.MidpoFilter, name="MidpoFilter"),
    path("s=<str:name>/MinFilter", views.MinFilter, name="MinFilter"),
    path("s=<str:name>/Negative", views.Negative, name="Negative"),
    path("s=<str:name>/Reverse_0_order", views.Reverse_0_order, name="Reverse_0_order"),
    path("s=<str:name>/Reverse_with_order_1", views.Reverse_with_order_1, name="Reverse_with_order_1"),
    path("s=<str:name>/sharp_image", views.sharp_image, name="sharp_image"),
    path("s=<str:name>/subTwoImages", views.subTwoImages, name="subTwoImages"),
    path("s=<str:name>/unsharp_algorithm", views.unsharp_algorithm, name="unsharp_algorithm"),
    path("s=<str:name>/Histogram", views.Histogram, name="Histogram"),
]

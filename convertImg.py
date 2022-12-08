import removeLight
import imgTransparent
import kornia
import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
kornia.__version__

def machinRunning(fileName):
    # 오리진은 빛 제거 전, 그냥은 빛 제거 후
    img = removeLight.removeLight(fileName)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # convert to torch tensor
    data: torch.tensor = kornia.image_to_tensor(img, keepdim=False)/255.  # BxCxHxW

    # create the operator
    canny = kornia.filters.Canny(0.1,0.175)

    # blur the image
    x_magnitude, x_canny = canny(data.float())
    img_canny: np.ndarray = kornia.tensor_to_image(x_canny.byte())


    fig, axs = plt.subplots(1, 1, figsize=(16,16))
    axs.axis('off')
    axs.imshow(img_canny, cmap='Greys')

    #이미지 저장 To do : 좀 더 완성도 있는 이미지로 저장하기
    # 원하는 디렉토리로 파일저장
    fig.savefig("convertImg"+fileName)
    #배경을 투명하게 하기
    imgTransparent.imgTransparent(fileName)
    
def PngToSvg(fileName):
    x=plt.imread(fileName)[...,0]    
    svgfilename = fileName.split('.')[0]+".svg"
    plt.imsave(svgfilename,x,format='svg',cmap='gray')
    return svgfilename
    
def SvgToPng(fileName):
    drawing = svg2rlg(fileName)
    pngfilename = fileName.split('.')[0]+".png"
    renderPM.drawToFile(drawing, pngfilename, fmt='PNG')
    return pngfilename
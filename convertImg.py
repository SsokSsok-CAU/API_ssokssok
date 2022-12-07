import removeLight

import kornia

import os
import torch
import cv2
import numpy as np
import matplotlib.pyplot as plt
kornia.__version__

def machinRunning(fileName):
    # 오리진은 빛 제거 전, 그냥은 빛 제거 후
    img = removeLight.removeLight(fileName)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # convert to torch tensor
    data: torch.tensor = kornia.image_to_tensor(img, keepdim=False)/255.  # BxCxHxW

    # create the operator
    canny = kornia.filters.Canny(0.05,0.15)

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
    # im = Image.open("convertImg"+fileName).convert('RGB')
    # im_inv = ImageOps.invert("convertImg"+fileName)
    # im_inv_L = im_inv.convert('L')
    # im.putalpha(im_inv_L)
    # im.save("convertImg"+fileName, "png")

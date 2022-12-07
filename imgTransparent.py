from PIL import Image, ImageOps, ImageFilter
def imgTransparent(fileName):
    im = Image.open("convertImg"+fileName).convert('RGBA')
    datas = im.getdata()

    newData = []
    cutoff = 255

    for item in datas:
        if item[0] >= cutoff and item[1] >= cutoff and item[2] >= cutoff:
            newData.append((255,255,255,0))
        else:
            newData.append(item)
    im.putdata(newData)
    im.save("convertImg"+fileName+".png",'PNG')

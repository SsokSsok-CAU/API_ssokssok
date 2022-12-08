from PIL import Image
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
    im.save("convertImg"+fileName,'PNG', qualty=70)

def resizingImg(fileName):
    img = Image.open(fileName)
    print(img.size)
    if img.width > 1500 and img.height > 1500:
        img = img.resize((int(img.width / 2), int(img.height / 2)))
    print(img.size)
    img.save(fileName, 'PNG')

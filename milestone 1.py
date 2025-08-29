def boundColor(x):
    from math import floor
    if 0 < x < 255:
        return floor(x)
    elif x < 0 or x == 0:
        return 0
    elif x > 255 or x == 255:
        return 255
print (boundColor(234.5))
print(boundColor(-10))
print (boundColor(500))


def getColor(line):
    num = line.split()
    givenum = map(int, num[2:5])
    givenum2 = list(givenum)
    return givenum2
print (getColor('1 2 3 4 5'))


def getLocation(line):
    num = line.split()
    givenum = map(int, num[0:2])
    givenum2 = list(givenum)
    return givenum2
print (getLocation('1 2 3 4 5'))


def checkPixel(x, y, width, height):
    if x >= 0 and y >= 0 and x < width and y < height:
        return True
    else:
        return False
print (checkPixel(-1,0,10,20))
print (checkPixel(20,0,10,20))
print (checkPixel(5,5,10,20))

def createColorDict(color):
    final = {'red' : boundColor(color[0]), 'green' : boundColor(color[1]), 'blue' : boundColor(color[2])}
    return final
print(createColorDict([-10, 100.5, 300]))


def createPixel(color, x, y):
    final = {'color' : color, 'x' : x, 'y' : y}
    return final
print (createPixel({'red': 0, 'green': 100, 'blue': 255},2,3))

def addPixelToList(pixelList, pixel):
    final = pixelList
    final.append(pixel)
    return None
print (addPixelToList([{'color': {'red': 1, 'green': 2, 'blue': 3},'x': 4, 'y': 5}],{'color': {'red': 0, 'green': 100, 'blue':255}, 'x': 2, 'y': 3}))

def readPixels(filename, pixels):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            color_values = getColor(line)
            location_values = getLocation(line)
            color_dict = createColorDict(color_values)
            pixel = createPixel(color_dict, location_values[0], location_values[1])
            addPixelToList(pixels, pixel)

def createImage(width, height):
    image = []
    for val in range(height):
        row = []
        for num in range (width):
            row.append(createColorDict([0, 0, 0]))
        image.append(row)
    return image
print (createImage(2,3))

def drawPixels(image, pixels):
    height = len(image)
    width = len(image[0])
    for pixel in pixels:
        x = pixel['x']
        y = pixel['y']
        color = pixel['color']
        if checkPixel(x, y, width, height):
            image[y][x] = color

def writeImage(filename, image):
    height = len(image)
    width = len(image[0])
    with open(filename, "w") as phail:
        phail.write('P3\n')
        phail.write(f'{width} {height}\n')
        phail.write('255\n')
        for row in image:
            for pixel in row:
                erupu = pixel['red']
                akupacha = pixel['green']
                neeli = pixel['blue']
                phail.write(f'{erupu} {akupacha} {neeli}\n')

def createSolidCircle(pixels, x, y, r, color):
    for xT in range(x - r, x + r + 1):
        for yT in range(y - r, y + r + 1):
            if ((xT - x) ** 2) + ((yT - y) ** 2) <= r * r:
                pixel = createPixel(color, xT, yT)
                pixels.append(pixel)

def createSolidRectangle(pixels, x1, y1, x2, y2, color):
    left = min(x1, x2)
    right = max(x1, x2)
    dom = min(y1, y2)
    sub = max(y1, y2)
    for xcord in range(left, right + 1):
        for ycord in range(dom, sub + 1):
            pixel = createPixel(color, xcord, ycord)
            pixels.append(pixel)



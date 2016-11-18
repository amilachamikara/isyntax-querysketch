import cv2

def optimalSize(img, sqr=800):
    height, width = img.shape

    ratio = height/width

    if(ratio<=1):
        h = ratio * sqr
        w = sqr
    else:
        h = sqr
        w = (1/ratio) * sqr

    scaledRatio = h/height

    output = cv2.resize(img, None, fx=w/width, fy=h/height, interpolation = cv2.INTER_CUBIC)
    return scaledRatio, output

##commment
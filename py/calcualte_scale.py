import math
import cv2
import numpy as np

colors = [[31, 255],[255, 99],[112, 255],[255, 173],[179, 255],\
                [210, 255],[155, 239],[255, 207],[146, 255],[255, 137],\
                [74, 255],[255, 57],[240, 255]]

waves = [515, 525, 535, 545, 555, 565, 575, 585, 595, 605, 615, 625, 635]

def gaussianModel(sigma, miu, x):
    # pref = 1.0 / (float(sigma) * math.sqrt(2.0 * math.pi))
    index = math.pow(float(x) - float(miu), 2) / math.pow(float(sigma), 2) / 2.0
    result = math.exp(-index)
    return result

oldR = []
for i in range(0, 13):
    oldR.append(gaussianModel(58, 580, waves[i]))

print oldR

def gaussianModelForMiu(sigma, x, y):
    # pref = float(sigma) * math.sqrt(2.0 * math.pi)
    square = -2.0 * math.log(y)    
    temp = math.sqrt(square) * sigma
    miu1 = x + temp
    miu2 = x - temp
    if miu1 > miu2:
        return miu1
    else:
        return miu2
    

y = gaussianModel(58, 590, 525)
print y

miu = gaussianModelForMiu(48, 525, y)
print miu

for wave in waves:
    print gaussianModel(48, 548, wave) / gaussianModel(58, 590, wave)




# rgRatio = [1.82162714788,1.67058239371,1.51125163989,1.34854718003,1.18701438016,1.03063833065,0.882708025999,0.745741540413,0.621469859213,0.510872211987,0.414252335596,0.331343248496,0.26142779557]

# wave = [515,525,535,545,555,565,575,585,595,605,615,625,635]

# points = np.zeros(shape = (13,2))

# for i in range(0,13):
#     points[i] = [wave[i], rgRatio[i]]

# [vx, vy, x0, y0] = cv2.fitLine(points, cv2.cv.CV_DIST_L2, 0, 0.01, 0.01)

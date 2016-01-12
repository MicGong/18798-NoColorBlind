import cv2 
import math
import numpy as np

miuG = 548
sigmaG = 48
miuR = 590
sigmaR = 58

def gaussianModel(sigma, miu, x):
    pref = 1.0 / (float(sigma) * math.sqrt(2.0 * math.pi))
    index = math.pow(float(x) - float(miu), 2) / math.pow(float(sigma), 2) / 2.0
    result = math.exp(-index)
    return result

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

class ResultPageCV():
    def __init__(self, results):
        self.cap = cv2.VideoCapture(0)
        self.results = results
        self.testColors = [[31, 255],[255, 99],[112, 255],[255, 173],[179, 255],\
                [210, 255],[155, 239],[255, 207],[146, 255],[255, 137],\
                [74, 255],[255, 57],[240, 255]]
        self.grRatio = [1.82162714788,1.67058239371,1.51125163989,1.34854718003,\
                1.18701438016,1.03063833065,0.882708025999,0.745741540413,0.621469859213,\
                0.510872211987,0.414252335596,0.331343248496,0.26142779557]
        self.mappingN2O = [[1,1],[2,12],[3,3],[4,10],[5,5],[6,6],[7,8],[8,9],[9,4],\
                [10,2],[11,11],[12,13],[13,7]]
        self.mappingO2N = [[1,1],[2,10],[3,3],[4,9],[5,5],[6,6],[7,13],[8,7],[9,8],\
                [10,4],[11,11],[12,2],[13,12]]
        self.waves = [515, 525, 535, 545, 555, 565, 575, 585, 595, 605, 615, 625, 635]
        self.oldR = [0.5336726453935995, 0.6378746072647454, 0.7400918528382704, \
                0.8335388969942682, 0.9112888501455416, 0.9671106823558161, 0.9962910805892409,\
                0.9962910805892409, 0.9671106823558161, 0.9112888501455416, 0.8335388969942682,\
                0.7400918528382704, 0.6378746072647454]
        self.newGRRatio = []
        self.leftSet = [1,3,5,9,10]
        self.userLeftSet = []
        self.rightSet = [2,4,8,10,12]
        self.userRightSet = []
        self.flag = 0
        self.miuGShifted = 0

    def parseResult(self):
        leftCount = 0
        rightCount = 0
        for result in self.results:
            if result[0] in  self.leftSet:
                self.userLeftSet.append(result[0])
                leftCount += 1
            elif result[0] in self.rightSet:
                self.userRightSet.append(result[0])
                rightCount += 1
            else:
                pass
        if leftCount > rightCount:
            self.flag = -1
        else:
            self.flag = 1
        
        if self.flag == -1:
            minInd = 13
            for i in range(0, len(self.userLeftSet)):
                if self.mappingN2O[self.userLeftSet[i]][1] < minInd:
                    minInd = self.mappingN2O[self.userLeftSet[i]][1]
            tempY = gaussianModel(sigmaR, miuR, self.waves[minInd])
            self.miuGShifted = gaussianModelForMiu(sigmaG, self.waves[minInd], tempY)
        else:
            maxInd = -1
            for i in range(0, len(self.userRightSet)):
                if self.mappingN2O[self.userRightSet[i]][1] > maxInd:
                    maxInd = self.mappingN2O[self.userRightSet[i]][1]
            tempY = gaussianModel(sigmaR, miuR, self.waves[maxInd])
            self.miuGShifted = gaussianModelForMiu(sigmaG, self.waves[maxInd], tempY)

        print self.miuGShifted

        for i in range(0, 13):
            newG = gaussianModel(sigmaG, self.miuGShifted, self.waves[i])
            self.newGRRatio.append(newG / self.oldR[i])

        self.rr = []
        for i in range(0, 13):
            self.rr.append(self.newGRRatio[i] / self.grRatio[i])
        
        print self.rr

    def showCamera(self):

        _, frameTest = self.cap.read()
        height = frameTest.shape[0]
        width = frameTest.shape[1]
        height = height * 0.4
        width = width * 0.4
        
        while(True):
            _, frame = self.cap.read()
            frameSmall = cv2.resize(frame, (0,0), fx = 0.4, fy = 0.4)
            # height, width, channels = frameSmall.shape
            r,g,b = cv2.split(frameSmall)
            gRatio = np.zeros((height, width), np.float32)
            imgGRRatio = cv2.divide(g,r)
            
            for i in range(0, int(height)):
                for j in range(0, int(width)):
                    if imgGRRatio[i,j] >= 1.8:
                        gRatio[i,j] = 2 * 0.1
                    elif imgGRRatio[i,j] >= 1.67 and imgGRRatio[i,j] < 1.8:
                        gRatio[i,j] = 1.8 * 0.1
                    elif imgGRRatio[i,j] >= 1.5 and imgGRRatio[i,j] < 1.67:
                        gRatio[i,j] = 1.67 * 0.15
                    elif imgGRRatio[i,j] >= 1.3 and imgGRRatio[i,j] < 1.5:
                        gRatio[i,j] = 1.5 * 0.26
                    elif imgGRRatio[i,j] >= 1.0 and imgGRRatio[i,j] < 1.3:
                        gRatio[i,j] = 1.3 * 0.46
                    elif imgGRRatio[i,j] >= 0.8 and imgGRRatio[i,j] < 1.0:
                        gRatio[i,j] = 1.0 * 0.81
                    elif imgGRRatio[i,j] >= 0.6 and imgGRRatio[i,j] < 0.8:
                        gRatio[i,j] = 0.8 * 1.42
                    elif imgGRRatio[i,j] >= 0.4 and imgGRRatio[i,j] < 0.6:
                        gRatio[i,j] = 0.6 * 2.51
                    else:
                        gRatio[i,j] = 0.5 * 4.44

            newG = np.zeros((height, width), np.float32)
            newG = cv2.multiply(np.float32(g), gRatio)

            frameNew = cv2.merge([r,np.uint8(newG),b])
            cv2.imshow('Result', frameNew)
            cv2.waitKey(300)

        self.cap.release()

# def main():
#     resultPageCV = ResultPageCV([[1,159]])
#     resultPageCV.parseResult()
#     resultPageCV.showCamera()

# if __name__ == '__main__':
#     main()
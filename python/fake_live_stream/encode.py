import cv2
import json
import datetime
import threading

size = (1080, 1920, 3)
root2 = 1.414
innerSize = (int(940 * root2), int(540 * root2))
# left_top = (int((size[1] - innerSize[0]) / 2), int((size[0] - innerSize[1]) / 2))

# black = np.zeros(size)
black = cv2.imread("./imgs/black.jpg")
# fake = cv2.imread("./imgs/Genshin Impact_20210808145950.png")
target = cv2.imread("./imgs/r6s.png")

target = cv2.resize(target, innerSize, interpolation=cv2.INTER_NEAREST)
# fake = cv2.resize(fake, innerSize, interpolation=cv2.INTER_NEAREST)

pixelMap = {}
with open("./index.json", "r") as file:
    pixelMap = json.loads(file.read())


threadingPool = []

def progressArea(x, y, width, height, toFill):
    x = int(x)
    y = int(y)
    width = int(width)
    height = int(height)
    for copyingIndexX in range(x, x + width):
        for copyingIndexY in range(y, y + height):
            # black[copyingIndexY][copyingIndexX] = fake[copyingIndexY][copyingIndexX]

            # black[encodeDataIndexY][encodeDataIndexX] = target[copyingIndexY][copyingIndexX]
            index = pixelMap[str(copyingIndexY)][str(copyingIndexX)]
            toFill[index[0]][index[1]] = target[copyingIndexY][copyingIndexX]
    return toFill


def divideInto(x, y, target):
    # divide target and return the left top point and width, height
    points = []
    partX = int(target[0] / x)
    partY = int(target[1] / y)
    for i in range(x):
        for j in range(y):
            points.append([partX * i, partY * j])
    return points, partX, partY


points, width, height = divideInto(3, 3, innerSize)

starttime = datetime.datetime.now()

for point in points:
    t1 = threading.Thread(target=progressArea, args=(point[0], point[1], width, height, black))
    t1.start()
    threadingPool.append(t1)
endtime = datetime.datetime.now()
print("all thread started",(endtime - starttime))
for i in threadingPool:
    i.join()
endtime = datetime.datetime.now()
print((endtime - starttime))

# target.resize(innerSize)
cv2.imwrite("./imgs/test.jpg", black)


print("DONE")

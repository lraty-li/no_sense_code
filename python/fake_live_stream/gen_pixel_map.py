import cv2
import json
size = (1080, 1920, 3)
root2 = 1.414
innerSize = (int(940 * root2), int(540 * root2))

pixelMap = {}

encodeDataIndexX = innerSize[0]
encodeDataIndexY = 0
for copyingIndexX in range(innerSize[0]):
  for copyingIndexY in range(innerSize[1]):
    # black[copyingIndexY][copyingIndexX] = fake[copyingIndexY][copyingIndexX]


    #TODO gen a map, avoid the judge
    if(encodeDataIndexY < innerSize[1]):
      if(encodeDataIndexX >= size[1]):
        encodeDataIndexY += 1
        encodeDataIndexX = innerSize[0]
    else:
       if(encodeDataIndexX >= size[1]):
        encodeDataIndexY += 1
        encodeDataIndexX = 0

    # black[encodeDataIndexY][encodeDataIndexX] = target[copyingIndexY][copyingIndexX]
    try:
      pixelMap[copyingIndexY][copyingIndexX] = [encodeDataIndexY,encodeDataIndexX]
    except KeyError as e:
      pixelMap[copyingIndexY] = {}
      pixelMap[copyingIndexY][copyingIndexX] = [encodeDataIndexY,encodeDataIndexX]
    encodeDataIndexX += 1


with open('./index.json','w+') as file:
  file.write(json.dumps(pixelMap))    
print("DONE")

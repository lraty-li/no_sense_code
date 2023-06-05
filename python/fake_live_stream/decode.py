import cv2
import json
encrypted = cv2.imread('./imgs/test.jpg')

size = (1080, 1920, 3)
root2 = 1.414
innerSize = (int(940 * root2), int(540 * root2))

decode = cv2.imread('./imgs/decode_template.jpg')

pixelMap = {}
with open('./index.json','r') as file:
  pixelMap = json.loads(file.read())

encodeDataIndexX = innerSize[0]
encodeDataIndexY = 0

# with open('./idnexX.json','r') as file:
#   pixelMapX = json.loads(file.read())
# with open('./idnexY.json','r') as file:  
#   pixelMapY = json.loads(file.read())

for copyingIndexX in range(innerSize[0]):
  for copyingIndexY in range(innerSize[1]):

    index = pixelMap[str(copyingIndexY)][str(copyingIndexX)]
    decode[copyingIndexY][copyingIndexX] =  encrypted[index[0]][index[1]] 
    encodeDataIndexX += 1

cv2.imwrite("/imgsdecode.jpg", decode)
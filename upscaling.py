import cv2
from cv2 import dnn_superres

img_path = "sample.png"
option = 1
target_img=cv2.imread(img_path, option)

#업스케일 도구 가져오기
sr = dnn_superres.DnnSuperResImpl_create()

#모델 읽어오기
path = 'EDSR_x2.pb'
sr.readModel(path)

#모델의 이미지 스케일 지정하기(x3일때는 3, EDSR_x4.pb일때는 4를 입력하면 된다.)
sr.setModel('edsr', 2)

upscaled = sr.upsample(target_img)

cv2.imwrite('upscale.png', upscaled)
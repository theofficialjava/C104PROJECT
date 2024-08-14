import cv2

image_path = "C:/Users/theof/iCloudDrive/Desktop/Code/WhiteHat Jr_/class104/C104PROJECT/solar-system.jpg"

img = cv2.imread(image_path)

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.7
text_color = (255, 255, 255)
text_thickness = 2

cv2.putText(img, "Mercury", (30, 220), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img, "Venus", (130, 240), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img, "Earth", (250, 220), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img, "Mars", (380, 180), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img, "Jupiter", (520, 130), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img, "Saturn", (680, 110), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img, "Uranus", (900, 80), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))
cv2.putText(img, "Neptune", (1100, 50), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,255,255))

cv2.imshow("labelled diagram of solar system", img)
cv2.waitKey(0)
cv2.imwrite("labelledsolarsystem.jpg", img)

print("code successful!")
import cv2
img=cv2.imread('Photo4.png') # Чтение изображения

cv2.imshow('Result', img)  # inshow - вывод: Result - название окна, img путь.
cv2.waitKey(0)  # waitKey - время жизни окна в милисекундах: 1000 - 1с, 0 - пока не закроем окно

new_img=img

# new_img=cv2.resize(img,(img.shape[1] // 2,img.shape[0] // 2)) 
## resize - Изменение размера: img -путь, кортеж(высота, ширина).
## shape - возвращает размеры картинки по индексу: [0] - ширина, [1] - высота.
# cv2.imshow('Result', new_img)
# cv2.waitKey(0) 

# cv2.imshow("Result", img[5:300,340:540]) 
# # при указании img[5:300, 340:540] - картинка обрезается по высоте, ширине. 
# # Обрезка идет по пикселям.
# cv2.waitKey(0) 

new_img=cv2.medianBlur(new_img,7)
# GaussianBlur - размытие изображения: img - путь,
# 7 - параметр/кф хз.
# cv2.imshow("Result", new_img)
# cv2.waitKey(0)

new_img=cv2.GaussianBlur(new_img, (11,11), 0)
# GaussianBlur - размытие изображения: img - путь,
# кортеж(Очень важно! Элементы должны быть только нечетными, иначе ошибка), 1 - по гориз., 2- по верт.
# 0 - множитель.
# cv2.imshow("Result", new_img)
# cv2.waitKey(0)

new_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
#cvtColor - изменение формата изображения, дальше параметр (cv2. -> выбираем из списка) Вместо RGB тут BRG
# cv2.imshow("Result", new_img)
# cv2.waitKey(0)

new_img = cv2.Canny(new_img, 70, 70) ## копнуть глубже по тех. части
cv2.imshow("Result", new_img)
cv2.waitKey(0)

## поиграться со всеми параметрами для более качественного результата.
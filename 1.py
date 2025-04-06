import cv2
img=cv2.imread('Photo4.png') # Чтение изображения

cv2.imshow('Result', img)  # inshow - вывод: Result - название окна, img путь.
cv2.waitKey(0)  # waitKey - время жизни окна в милисекундах: 1000 - 1с, 0 - пока не закроем окно

oper_img = img.copy()
oper_img = cv2.cvtColor(oper_img, cv2.COLOR_BGR2GRAY)

# oper_img=cv2.resize(img,(img.shape[1] // 2,img.shape[0] // 2)) 
## resize - Изменение размера: img -путь, кортеж(высота, ширина).
## shape - возвращает размеры картинки по индексу: [0] - ширина, [1] - высота.
# cv2.imshow('Result', oper_img)
# cv2.waitKey(0) 

# cv2.imshow("Result", img[5:300,340:540]) 
# # при указании img[5:300, 340:540] - картинка обрезается по высоте, ширине. 
# # Обрезка идет по пикселям.
# cv2.waitKey(0)

# oper_img = cv2.cvtColor(oper_img, cv2.COLOR_BGR2GRAY)
# #cvtColor - изменение формата изображения, дальше параметр (cv2. -> выбираем из списка) Вместо RGB тут BGR
# # cv2.imshow("Result", oper_img)
# # cv2.waitKey(0)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)) #Специальнвй объект для работы с контрастом - CLAHE(Contrast Limited Adaptive Histogram Equalization)
# clipLimit (обычно 2.0–4.0) — чем выше, тем сильнее контраст, но может усиливать шум.
# tileGridSize (например, (8,8)) — чем меньше блок, тем более локальная коррекция, но возможны артефакты.
oper_img = clahe.apply(oper_img)
#.apply (как метод CLAHE) - применяет CLAHE к изображению
# cv2.imshow("Result", oper_img)
# cv2.waitKey(0)

oper_img=cv2.medianBlur(oper_img,5)
# GaussianBlur - размытие изображения: img - путь,
# 7 - параметр/кф хз.
# cv2.imshow("Result", oper_img)
# cv2.waitKey(0)

oper_img=cv2.GaussianBlur(oper_img, (15,15), 0)
# GaussianBlur - размытие изображения: img - путь,
# кортеж(Очень важно! Элементы должны быть только нечетными, иначе ошибка), 1 - по гориз., 2- по верт.
# 0 - множитель.
# cv2.imshow("Result", oper_img)
# cv2.waitKey(0)

Canny_img = cv2.Canny(oper_img, 100, 100) ## копнуть глубже по тех. части
cv2.imshow("Result", Canny_img)
cv2.waitKey(0)

dst=cv2.cornerHarris(Canny_img, blockSize=2, ksize=5, k=0.1) # cornerHarris - Детектор Харриса, который помогает выделять углы
# dst — это матрица того же размера, что и входное изображение, где каждое значение — это "угловая метрика" R.
# edges — входное изображение (обычно границы после Canny или просто grayscale).
# blockSize — размер окрестности для усреднения матрицы M (например, 2 означает окно 2×2).
# ksize — размер ядра оператора Собеля для вычисления градиентов (3 означает ядро 3×3).
# k — коэффициент в формуле для R (обычно 0.04).
dst = cv2.dilate(dst, None)
# dst содержит слабые значения углов. 
# dilate делает углы более выраженными, чтобы они были более заметны

img[dst > 0.03 * dst.max()] = [0, 0, 255]
# img=cv2.resize(img,(img.shape[1] * 2 ,img.shape[0] * 2 )) 
cv2.imshow("Result", img)
cv2.waitKey(0)



## поиграться со всеми параметрами для более качественного результата.
import cv2

# Загрузка изображения
image = cv2.imread('Example_1.jpeg')

# Координаты прямоугольника (в формате [x_min, y_min, x_max, y_max])
rectangle_coordinates = [845.5067138671875, 322.81951904296875, 1622.8408203125, 1067.642578125]

# Извлечение координат
x_min, y_min, x_max, y_max = rectangle_coordinates

# Нарисовать прямоугольник на изображении
cv2.rectangle(image, (int(x_min), int(y_min)), (int(x_max), int(y_max)), (0, 255, 0), 2)







# Отобразить изображение с прямоугольником
cv2.imwrite('image_with_bbox.jpg', image)


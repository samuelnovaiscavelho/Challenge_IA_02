import cv2

classificador = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
imagem = cv2.imread(r"fotos/homem.jpg")

cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = classificador.detectMultiScale(cinza, scaleFactor=2, minSize=(100, 100))

for x, y, l, a in faces:
    imagem = cv2.rectangle(imagem, (x,y), (x+l, y+a), (47,79,79), 2)
    print(l, a)
    
cv2.imshow("Faces detectadas", imagem)
cv2.waitKey()
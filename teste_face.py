import cv2
#opencv-contrib-python
detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

foto = cv2.imread('imagem.jpg')
foto_cinza = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
faces_detectadas = detector.detectMultiScale(foto_cinza, scaleFactor=1.02, minSize=(52, 52))
print("Pessoas detectadas", len(faces_detectadas))

for x, y, l, a in faces_detectadas:
    #arquivo_img, ponto_inicial, ponto_final, cor_BGR, espessura_px
    foto = cv2.rectangle(foto, (x, y), (x+l, y+a), (0, 0, 255), 2)

print(faces_detectadas)
cv2.imshow("Umas pessoas aleatorias", foto)
cv2.waitKey()

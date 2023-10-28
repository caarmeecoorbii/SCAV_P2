import sys
import os

#Exercici 1
#Mètode per convertir de RGB a YUV
def rgb_to_yuv(rgb):
    r,g,b = rgb #Separem el valor RGB 
    y = 0.299 * r + 0.587 * g + 0.114 * b #Calculem la component Y
    u = -0.14713 * r - 0.288862 * g + 0.436 * b #Calculem la component U
    v = 0.615 * r - 0.51499 * g - 0.10001 * b #Calculem la component V
    return y, u, v

#Mètode per convertir de YUV a RGB
def yuv_to_rgb(yuv):
    y,u,v = yuv #Separem el valor YUV
    r = y + 1.13983 * v #Calculem la component R
    g = y - 0.39465 * u - 0.58060 * v #Calculem la component G
    b = y + 2.03211 * u #Calculem la component B
    return r, g, b


#Exercici 2
#Funció per redimensionar i reduir la calitat d'una imatge
def resize_and_lower_quality(imatge_entrada, imatge_sortida, amplada, alcada, qualitat):
    try:
        #  FFmpeg commanda per redimensionar i reducir la qualitat
        ffmpeg_command = f"ffmpeg -i {imatge_entrada} -vf 'scale={amplada}:{alcada}' -q:v {qualitat} -frames:v 1 {imatge_sortida}"

        # Executa la comanda FFmeg
        os.system(ffmpeg_command)

        print(f"Imatge redimensionada i qualitat reduida correctament i guardada com: {imatge_sortida}")
    except Exception as e:
        print(f"Error: {e}")


#Exercici 3
#Funció per llegir els bytes d'una imatge en un patró
def serpentine(ruta_arxiu):
    bytes_zigzag = []

    with open(ruta_arxiu, 'rb') as arxiu:
        byte = arxiu.read(1)
        bytes_zigzag.append(byte)
        fila, columna = 0, 0
        direccio = 1  # 1 per dreta-dalt, -1 per esquerra-baix

        while byte:
            if fila == 0:
                if columna % 2 == 0:
                    direccio = 1  # Moure cap a la dreta
                else:
                    direccio = -1  # Moure cap a l'esquerra

            if direccio == 1:
                columna += 1
            else:
                columna -= 1
                fila += 1

            byte = arxiu.read(1)

            if byte:
                bytes_zigzag.append(byte)

    return bytes_zigzag


#Exercici 4
#Funció per convertir a blanc i negre amb compressió extrema
def convert_to_bw_with_hard_compression(imatge_entrada, imatge_sortida):
    try:
        # Comanda FFmeg per convertir el blanc i negre i aplicar la compresió extrema
        ffmpeg_command = f"ffmpeg -i {imatge_entrada} -vf format=gray -crf 51 {imatge_sortida}"
        os.system(ffmpeg_command)
        print(f"Imatge convetida a blanc i negre amb compressió extrema i guardada com: {imatge_sortida}")
    except Exception as e:
        print(f"Error: {e}")

#Exercici 5
#Funció per aplicar Run-Length Encoding (RLE) a una seqüència de bytes
def codificacio_run_length(byte_seq):
    seq_codificada = []
    i = 0
    n = len(byte_seq)

    while i < n:
        comptador = 1
        while i < n - 1 and byte_seq[i] == byte_seq[i + 1]:
            comptador += 1
            i += 1
        seq_codificada.append((byte_seq[i], comptador))
        i += 1

    return seq_codificada

#Exercici 6
# Classe per calcular la DCT i IDCT donada una imatge d'entrada
from scipy.fftpack import dct, idct

class DCTConverter:
    def __init__(self):
        pass

    def dct2(self, image):
        return dct(dct(image.T, norm='ortho').T, norm='ortho')

    # implement 2D IDCT
    def idct2(self,image):
        return idct(idct(image.T, norm='ortho').T, norm='ortho')

#Funció principal
def main():
    if len(sys.argv) < 2:
        print("Ús: python rgb_yuv.py [exercici]")
        return
    
    exercici = sys.argv[1]

    #Exercici 1: Conversió de RGB a YUV
    if exercici == '1':
        #Declaro les variables r, g, b
        r = 120
        g = 25
        b = 255
        rgb = (r, g, b)
        
        print(f"RGB d'entrada: {rgb}")

        yuv = rgb_to_yuv(rgb) #Passa de RGB a YUV
        print(f"RGB a YUV: {yuv}")
        
        rgb_result = yuv_to_rgb(yuv) #Passa de YUV a RGB
        print(f"YUV a RGB: {rgb_result}")

    #Exercici 2: Redimensiona i redueix la qualitat de la imatge
    elif exercici == '2':
        imatge_entrada = '/home/ccorbi/foto_islandia.JPG' #Imatge d'entrada
        imatge_sortida = 'imatge_islandia_reduida.JPG' #Nom de la imatge de sortida
        amplada = 800 #Nova amplada de la imatge de sortida
        alcada = 600 #Nova alçada de la imatge de sortida
        qualitat = 2
        resize_and_lower_quality(imatge_entrada, imatge_sortida, amplada, alcada, qualitat)

    #Exercici 3: Llegeix els bytes d'una imatge i els retorna amb el patró serpentina
    elif exercici == '3':
        imatge_entrada = '/home/ccorbi/foto_islandia2.JPG' #Imatge d'entrada
        zigzag_bytes = serpentine(imatge_entrada)
        # Mostrar els 20 primer bytes
        print(zigzag_bytes[:20])

    #Exercici 4: Converteix una imatge de color a blanc i negre amb compressió extrema
    elif exercici == '4':
        imatge_entrada = '/home/ccorbi/foto_islandia3.JPG' #Imatge d'entrada
        imatge_sortida_bn = 'foto_islandia3_bn.JPG' #Nom imatge de sortida

        convert_to_bw_with_hard_compression(imatge_entrada, imatge_sortida_bn)    

    #Exercici 5: Aplica Run-Length Encoding (RLE) a una seqüència de bytes
    elif exercici == '5':
        sequencia_byte = [1, 4, 9, 5, 5, 7, 1, 8, 6]
        sequencia_encoded = codificacio_run_length(sequencia_byte)
        print(f"Seqüència d'entrada",sequencia_byte)
        print(f"Seqüència RLE:", sequencia_encoded)

    #Exercici 6: Aplicar DCT a una imatge
    elif exercici == '6':
        #Creem instància de la classe DCTConverter
        converter = DCTConverter()
        #Importem les llibreries necessàries
        from skimage.io import imread
        from skimage.color import rgb2gray
        import matplotlib.pylab as plt

        #Llegim una imatge en escala de grisos
        imatge_entrada = rgb2gray(imread('/home/ccorbi/foto_islandia2.JPG')) 
        # Apliquem la transformada DCT 2D a la imatge
        imF = converter.dct2(imatge_entrada)
        # Realitzem la transformada IDCT 2D a la imatge
        im1 = converter.idct2(imF)
         # Creem una figura de trama de dues imatges: Original i Reconstruïda
        plt.gray()
        plt.subplot(121), plt.imshow(imatge_entrada), plt.axis('off'), plt.title('Imatge Original', size=20)
        plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title('Imatge Reconstruïda (IDCT)', size=20)

        # Mostrem la figura amb les tres imatges
        plt.show()
       


          
    else:
        print("Exercici no vàlid. Proporcionar un número del 1 al 6")

if __name__ == "__main__":
    main()



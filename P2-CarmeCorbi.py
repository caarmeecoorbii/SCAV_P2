import sys
import os
import subprocess

#Exercici 5
from rgb_yuv import rgb_to_yuv,yuv_to_rgb

#Exercici 1: Passar de mp4 a mp2 i guarda l'informació.
def info(fitxer_sortida,fitxer_info):
    #Definir la comanda FFmpeg per guarda l'informació del vídeo
    comanda_info = f'ffmpeg -i "{fitxer_sortida}" 2> "{fitxer_info}"'
    #Executar la comanda FFmeg
    subprocess.run(comanda_info,shell= True)

#Exercici 2: Modificar la resolució del vídeo
def modificar_resolucio(video_entrada, video_sortida, resolucio):
    # Definir la comanda FFmpeg per canviar la resolució
    comanda_resolucio = f'ffmpeg -i "{video_entrada}" -vf "scale={resolucio}" -c:a copy "{video_sortida}"'

    # Executar la comanda FFmpeg per modificar la resolució
    subprocess.run(comanda_resolucio, shell=True)


#Exercici 3: Canviar el cromasubmostreig del vídeo
def modificar_cromasubmostreig(video_entrada, video_sortida, cromasubmostreig):
    # Definir la comanda FFmpeg per canviar el cromasubmostreig
    comanda_cromasubmostreig = f'ffmpeg -i "{video_entrada}" -vf "format={cromasubmostreig}" -c:a copy "{video_sortida}"'

    # Executar la comanda FFmpeg per modificar el cromasubmostreig
    subprocess.run(comanda_cromasubmostreig, shell=True)


#Exercici 4: Imprimir aspectes rellevants del vídeo
def obtenir_info_video(video_entrada):
    # Comanda per executar ffprobe
    comanda = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'v:0',
        '-show_entries', 'stream= codec_type,width,height,pix_fmt,sample_aspect_ratio,chroma_location,duration,bit_rate,color_range,color_space',
        '-of', 'default=noprint_wrappers=1',
        video_entrada
    ]

    # Executar la comanda i obtenir la sortida
    sortida = subprocess.check_output(comanda, stderr=subprocess.STDOUT, text=True)

    linies = sortida.strip().split('\n')
    dades = {}

    for linia in linies:
        clau, valor = linia.split('=')
        dades[clau] = valor

    print(f"Característiques del vídeo: {dades}")
   
#Funció main
def main():
    if len(sys.argv) < 2:
        print("Ús: python P2-CarmeCorbi.py [exercici]")
        return
    
    exercici = sys.argv[1]
    video_entrada = '/home/ccorbi/BigBuckBunny.mp4'
    

    #Exercici 1
    if exercici == '1':
        video_sortida = '/home/ccorbi/BigBuckBunny.mpeg'
        fitxer_info = '/home/ccorbi/infofitxer.txt'
        comanda = f'ffmpeg -i "{video_entrada}" -c:v mpeg2video -q:v 2 -an "{video_sortida}"'
        subprocess.run(comanda, shell=True)

        info(video_sortida,fitxer_info)
        
        print(f"Vídeo convertit a {video_sortida}")

    #Exercici 2
    elif exercici == '2':
        resolucio = '640:480'
        video_sortida = '/home/ccorbi/BigBuckBunny_resolucio.mp4'
        modificar_resolucio(video_entrada,video_sortida,resolucio)

    #Exercici 3
    elif exercici == '3':
        cromasubmostreig = 'yuv422p'
        video_sortida = '/home/ccorbi/BigBuckBunny_cromasubmostreig.mp4'
        modificar_cromasubmostreig(video_entrada, video_sortida, cromasubmostreig)

    #Exercici 4
    elif exercici == '4':
        obtenir_info_video(video_entrada)

    #Exercici 5
    elif exercici == '5':
        r = 120
        g = 25
        b = 255
        rgb = (r, g, b)

        print(f"RGB d'entrada: {rgb}")

        yuv = rgb_to_yuv(rgb) #Passa de RGB a YUV
        print(f"RGB a YUV: {yuv}")
        
        rgb_result = yuv_to_rgb(yuv) #Passa de YUV a RGB
        print(f"YUV a RGB: {rgb_result}")


   





          
    else:
        print("Exercici no vàlid. Proporcionar un número del 1 al 5")

if __name__ == "__main__":
    main()
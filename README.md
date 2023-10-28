# Sistemes de Codificació d'Àudio i Vídeo: Pràctica 2
**Instruccions per executar el fitxer**

Executeu el fitxer `P2-CarmeCorbi.py` especificant el número d'exercici com a argument. Per exemple, per executar l'Exercici 1, utilitzeu la següent comanda:
   ```python
   python3 P2-CarmeCorbi.py 1
   ```

## Exercici 1: Passar d'MP4 a MPEG i guardar la informació
El propòsit d'aquest exercici implica la conversió d'un vídeo del format MP4 al format MPEG i guardar la informació del vídeo en un fitxer d'informació.
Dins de la funció **main** es verifica si es selecciona adequadament aquest exercici. Primer de tot, es defineix el vídeo d'entrada que en el meu cas és el BigBuckBunny i també es defineix el nom del vídeo de sortida. També es declara el nom del fitxer de text on es guardarà la informació.

Seguidament, s'utilitza la comanda FFmpeg **ffmpeg -i "{video_entrada}" -c:v mpeg2video -q:v 2 -an "{video_sortida}"**, on -i video_entrada especifica el vídeo d'entrada, -c:v mpeg2video especifica el còdec de vídeo que s'utilitzarà per a la sortida (s'utilitza el còdec de vídeo MPEG-2), -q:v 2 estableix la qualitat del vídeo. Finalment, es crida a la funció info. He creat la funció **info** que utilitza ffmpeg per extreure la informació d'un fitxer de vídeo i guarda aquesta informació en un arxiu de text.

```python
# Executa l'exercici 1
python3 P2-CarmeCorbi.py 1
```
**Resultat de l'exercici 1:**

Fitxer infofitxer.txt:
![](https://github.com/caarmeecoorbii/SCAV_P2/blob/main/infofitxer.txt.png)

BigBuckBunny en format MPEG:

![](https://github.com/caarmeecoorbii/SCAV_P2/blob/main/resultat_exercici1.png)


## Exercici 2: Modificar la resolució del vídeo
El propòsit d'aquest exercici és crear una funció que modifiqui la resolució d'un vídeo utilitzant FFmpeg. He creat la funció **modificar_resolucio**, on els paràmetres d'entrada són el path del vídeo d'entrada, el path del vídeo de sortida i la nova resolució. Aquesta funció utilitza la comanda FFmpeg **ffmpeg -i "{video_entrada}" -vf "scale={resolucio}" -c:a copy "{video_sortida}** , on -i vídeo_entrada especifica el vídeo d'entrada, -vf scale=resolucio especifica un filtre de vídeo que canviarà la resolució del vídeo a la nova resolució indicada, -c:a copy manté la pista d'àudio del fitxer d'entrada sense canvis i la copia al fitxer de sortida.

Dins de la funció **main** es verifica si es selecciona adequadament aquest exercici. Primer de tot, defineixo la nova resolució (640:480) i el path del vídeo de sortida. Per últim, crido a la funció **modificar_resolució**.


```python
# Executa l'exercici 2
python3 P2-CarmeCorbi.py 2
```
**Resultat de l'exercici 2:**

Vídeo entrada:

![](https://github.com/caarmeecoorbii/SCAV_P2/blob/main/resolucio_video_entrada.png)

Vídeo sortida:

![](https://github.com/caarmeecoorbii/SCAV_P2/blob/main/resolucio_video_sortida.png)

## Exercici 3: Canviar el cromasubmostreig del vídeo
El propòsit d'aquest exercici és crear una funció que modifiqui el cromasubmostreig d'un vídeo utilitzant FFmpeg. He creat la funció **modificar_cromasubmostreig**, on els paràmetres d'entrada són el path del vídeo d'entrada, el path del vídeo de sortida i el nou valor de cromasubmostreig. Aquesta funció utilitza la comanda FFpmeg **ffmpeg -i "{video_entrada}" -vf "format={cromasubmostreig}" -c:a copy "{video_sortida}"**, on -i video_entrada especifica l'arxiu de vídeo d'entrada, -vf format=cromasubmostreig aplica una transformació al format de submostreig de croma del vídeo, -c:a copy copia l'àudio sense canvis al fitxer de sortida. 

Dins de la funció **main** es verifica si es selecciona adequadament aquest exercici. Primer de tot, defineixo el nou valor de submostreig de croma ('yuv422p') i la ruta del vídeo de sortida. Per últim, crido a la funció **modificar_cromasubmostreig**.




```python
# Executa l'exercici 3
python3 P2-CarmeCorbi.py 3
```
**Resultat de l'exercici 3:**

Submostreig de croma vídeo original:

![](https://github.com/caarmeecoorbii/SCAV_P2/blob/main/cromasubmostreig_original.png)

Submostreig de croma després d'aplicar l'exercici 3:

![](https://github.com/caarmeecoorbii/SCAV_P2/blob/main/resultat_exercici3.png)



## Exercici 4: Imprimir aspectes rellevants del vídeo
El propòsit d'aquest exercici és crear una funció per obtenir almenys 5 característiques d'un vídeo i imprimir-les per pantalla. He creat una funció **obtenir_info_video** on el paràmetre d'entrada és el path del vídeo d'entrada. Aquesta funció utilitza una comanda FFmpeg per analitzar l'arxiu de vídeo **'ffprobe', '-v', 'error','-select_streams', 'v:0','-show_entries', 'stream= codec_type,width,height,pix_fmt,sample_aspect_ratio,chroma_location,duration,bit_rate,color_range,color_space','-of', 'default=noprint_wrappers=1', video_entrada** on -show_entries especifica la informació que vull obtenir del vídeo. En aquest cas, he seleccionat el tipus de còdec, dimensions del vídeo, format de píxels, duració, relació d'aspecte, la ubicació del croma, la taxa de bits, el rang de colors i l'espai de colors. Per últim, s'imprimeixen les caràcterístiques per pantalla.

Dins de la funció **main** es verifica si es selecciona adequadament aquest exercici. Seguidament, es crida a la funció **obtenir_info_video**.


```python
# Executa l'exercici 4
python3 P2-CarmeCorbi.py 4
```
**Resultat de l'exercici 4:**

![](https://github.com/caarmeecoorbii/SCAV_P2/blob/main/resultat_exercici4.png)

## Exercici 5: Integració del script de la pràctica 1
El propòsit d'aquest exercici és aprendre com un script hereta funcionalitats d'un altre script. El que he fet és a dalt de tot del script posar aquesta línia de codi **from rgb_yuv import rgb_to_yuv, yuv_to_rgb**, on estic important dues funcions del script **rgb_yuv.py** que és el fitxer de la primera pràctica.

Dins de la funció **main** es verifica si es selecciona adequadament aquest exercici. Per últim, defineixo els paràmetres adequats i crido a les dues funcions **rgb_to_yuv** i **yuv_t_rgb**.


```python
# Executa l'exercici 5
python3 P2-CarmeCorbi.py 5
```
**Resultat de l'exercici 5:**

![](https://github.com/caarmeecoorbii/SCAV_P2/blob/main/resultat_exercici5.png)


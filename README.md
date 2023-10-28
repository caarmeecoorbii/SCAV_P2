# Sistemes de Codificació d'Àudio i Video: Pràctica 2
**Instruccions per executar el fitxer**

Executeu el fitxer `P2-CarmeCorbi.py` especificant el número d'exercici com a argument. Per exemple, per executar l'Exercici 1, utilitzeu la següent comanda:
   ```python
   python3 P2-CarmeCorbi.py 1
   ```

## Exercici 1: Passar de MP4 a MPEG i guardar la informació
El propòsit d'aquest exercici implica la conversió d'un vídeo del format MP4 al format MPEG i guardar la informació del vídeo en un fitxer d'informació.
Dins de la funció **main** es verifica si es selecciona adequadament aquest exercici. Primer de tot, es defineix el vídeo d'entrada que en el meu cas és el BigBuckBunny i també es defineix el nom del vídeo de sortida. També es declara el nom del fitxer de text on es guardarà la informació.

Seguidament, s'utilitza la comanda FFpmeg **ffmpeg -i "{video_entrada}" -c:v mpeg2video -q:v 2 -an "{video_sortida}"**, on -i video_entrada especifica el vídeo d'entrada, -c:v mpeg2video especifica el codec de vídeo que s'utilitzarà per a la sortida (s'utilitza el códec de vídeo MPEG-2), -q:v 2 estableix la qualitat del vídeo. Finalment, es crida a la funció info. He creat la funció **info** que utilitza ffmpeg per extreure la informació d'un fitxer de vídeo i guarda aquesta informació en un arxiu de text.

```python
# Executa l'exercici 1
python3 P2-CarmeCorbi.py 1
```
**Resultat de l'exercici 1:**

Fitxer infofitxer.txt:
![](https://github.com/caarmeecoorbii/SCAV_P2/blob/main/infofitxer.txt.png)

BigBuckBunny en format MPEG:

![](https://github.com/caarmeecoorbii/SCAV_P2/blob/main/resultat_exercici1.png)


## Exercici 2: Redimensionar i reduir la qualitat d'imatges
El propòsit d'aquest exercici és crear una funció que modifiqui la resolució d'un vídeo utilitzant FFmpeg. He creat la funció **modificar_resolucio**, on els paràmetres d'entrada són el path del vídeo d'entrada, el path del vídeo de sortida i la nova resolució. Aquesta funció utilitza la comanda FFpmeg **ffmpeg -i "{video_entrada}" -vf "scale={resolucio}" -c:a copy "{video_sortida}** , on -i vídeo_entrada especifica el video d'entrada, -vf scale=resolucio especifica un filtre de vídeo que canviarà la resolució del vídeo a la nova resolució indicada, -c:a copy manté la pista d'àudio del fitxer d'entrada sense canvis i la copia al fitxer de sortida.

Dins de la funció **main** es verifica si es selecciona adequadament aquest exercici. Primer de tot, definim la nova resolució (640:480) i el path del vídeo de sortida. Per últim, crido a la funció **modificar_resolució**.


```python
# Executa l'exercici 2
python3 P2-CarmeCorbi.py 2
```
**Resultat de l'exercici 2:**

Vídeo entrada:

![](https://github.com/caarmeecoorbii/SCAV_P2/blob/main/resolucio_video_entrada.png)

Vídeo sortida:

![](https://github.com/caarmeecoorbii/SCAV_P2/blob/main/resolucio_video_sortida.png)

## Exercici 3: Llegir bytes d'una imatge amb patró serpentina
El proposit d'aquest exercici és crear una funció que modifiqui el cromasubmostreig s'un vídeo utilitzant FFmeg.


```python
# Executa l'exercici 3
python3 P2-CarmeCorbi.py 3
```
**Resultat de l'exercici 3:**
![]()

## Exercici 4: Conversió d'imatges a blanc i negre i compressió extrema:
El proposit d'aquest exercici és crear una funció per obtenir almenys 5 caràcteristiques d'un vídeo i imprimir-les per pantalla.



```python
# Executa l'exercici 4
python3 P2-CarmeCorbi.py 4
```
**Resultat de l'exercici 4:**
![]()

## Exercici 5: Integració del script de la pràctica 1
El propòsit d'aquest exercici és aprendre com un script hereda funcionalitats d'un altre script.


```python
# Executa l'exercici 5
python3 P2-CarmeCorbi.py 5
```
**Resultat de l'exercici 5:**

![]()


# Proyecto: Sistema de Reconocimiento Facial con DeepFace

## Descripción

Este proyecto implementa un sistema de reconocimiento facial utilizando la librería DeepFace en Python.

El programa analiza una imagen ubicada en la carpeta `entrada` y la compara contra un conjunto de imágenes previamente registradas en la carpeta `dataset_jpg`. Cada persona registrada tiene su propia carpeta con varias fotografías de entrenamiento.

El sistema identifica a la persona detectada y muestra un mensaje personalizado dependiendo de quién sea reconocido:

- Carolina → Modo ejercicio
- Manuel → Luces cálidas
- Santi → Modo caricaturas

Si la persona no coincide con ninguna registrada, el sistema indicará que es una persona desconocida.

---

## Requisitos

- Python 3.10 o superior
- Git

---

## Instalación

1) Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd Computer-Vision

2) Crear entorno virtual

python3 -m venv .venv

3) Activar entorno virtual en macOS / Linux:

source .venv/bin/activate

3.1) Activar modo virtual en Windows

.venv\Scripts\activate

4) Instalar dependencias 

pip install -r requirements.txt


##Estructura del proyecto

dataset_jpg/ → Carpeta con las personas registradas (una carpeta por persona).

entrada/ → Carpeta donde se coloca la imagen a analizar.

main.py → Script principal que ejecuta el reconocimiento facial.

requirements.txt → Librerías necesarias para ejecutar el proyecto.

##Uso del programa

Colocar una imagen a analizar en:

entrada/prueba_real.jpg


##Ejecutar el programa:

python main.py


El sistema analizará la imagen, comparará los rostros con los registrados y mostrará en la terminal el resultado del reconocimiento junto con una acción personalizada.

#Notas

Todas las imágenes deben estar en formato JPG.

Cada persona registrada debe tener su propia carpeta dentro de dataset_jpg.

Se recomienda incluir varias fotos por persona para mejorar la precisión.

## Cómo ejecutar el proyecto desde cero

1. Clonar el repositorio:

git clone https://github.com/vgkarito/Computer-Vision.git

2. Entrar a la carpeta del proyecto:

cd Computer-Vision

3. Crear un entorno virtual:

python3 -m venv .venv

4. Activar el entorno virtual:

Mac/Linux:
source .venv/bin/activate

Windows:
.venv\Scripts\activate

5. Instalar dependencias:

pip install -r requirements.txt

6. Colocar una imagen en:

entrada/prueba_real.jpg

7. Ejecutar el programa:

python main.py


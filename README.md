# Web-App Pulmon capital 🌎

## Descripción:
Un aplicativo web desarrollado en `python3.12` y `Django5.1` para el Hackathon del ***Departamento Administrativo de Tecnologías de la Información y Comunicaciones - DATIC Alcaldía De Santiago de Cali***

## Reto:
Desarrollar piloto de ***solución tecnológica*** que se alimente de los datos sincrónicos de calidad del aire de sensores ambientales de la ciudad de Cali, y utilice analítica de datos para ***generar alertas y sugerencias*** para mitigar contaminación del aire en ***áreas críticas***.

## Objetivo
Mejorar la salud pública y la calidad del aire en las ciudades. ¿Cuál es el MVP que se espera entreguen los campistas? Aplicativo que mida en tiempo real el estado de calidad del aire y su impacto en la salud humana, de acuerdo con el Índice de Calidad del Aire (ICA), según la proximidad del usuario con los sensores de medición existentes en la ciudad de Cali.

## Primeros pasos

1. Crear un directorio e ingresar en el mismo
```bash
   mkdir proyecto
   cd proyecto
```

2. Clonar el repositorio
```bash
   git clone https://github.com/xarcraft/pulmon_capital.git
```
   
3. Crear un entorno virtual dentro del directorio a utilizar
```bash
   python -m venv .venv
```
   
4. Activar el entorno
```bash
   .\.venv\Scripts\activate
```

5. Deslplazarce al directorio del aplicativo
```bash
   cd pulmon_capital
```  

6. Instalar las dependencias
```bash
   pip install -r requirements.txt
```

Hasta este punto la aplicación deberia estar lista para levantar pero primero debemos asegurarnos de un par de cosas.


## Levantar la aplicación

>A partir de este punto ya debes de tener el entorno levantado y estar ubicado en la raiz del proyecto para poder que los comandos no te causen error.
Lo puedes comprobar por que al inicio del prompt te sale el nombre de tu entorno entre parentesis (.venv)


1. Corra el siguiente comando en la terminal:
```bash
python manage.py makemigrations
python manage.py migrate
```  

2. Cree el super usuario
En este paso se te pediran 3 datos basicos 
- usuario
- correo
- contraseña la cual deberas repetir para verificar
  
```bash
python manage.py createsuperuser
```

1. Levante la aplicación
```bash
python manage.py runserver
```
  
1. Acceda a la aplicación - `http://127.0.0.1:8000/`


## Uso del panel administrador

1.  Acceder al administrador - `http://127.0.0.1:8000/admin/`
    
2.  Ingresar con el super usuario previamente creado.

> **Nota:** Este panel esta diseñado para ingresar de manera manual los datos a divisar en el front del aplicativo ya que se trata de un proyecto de ejemplo y no de un proyecto real. 
Y al no tener acceso a la base de datos para realizar consultas de manera automatica, se debe de ingresar manualmente los mismos, sin embargo a tiempo futuro toda su lógica y uso puede ser sincronizada con la data proporcionada por los sensores en cuestión.



![imagen del front](https://github.com/xarcraft/pulmon_capital/assets/img/apariencia.png?raw=true)
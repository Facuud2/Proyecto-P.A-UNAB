# Proyecto-P.A-UNAB

## Descripción

Este proyecto fue desarrollado en Python utilizando las librerías **Scrapy** y **PyQt** para la asignatura de Programación Avanzada de la Tecnicatura en Programación de la Universidad Nacional de Almirante Brown (UNaB).

### Integrantes del Grupo

- **Nombre del Integrante 1**: _Facundo David Carrizo Lucero_
- **Nombre del Integrante 2**: _Camila Abigail Juan_
- **Nombre del Integrante 3**: _Milagros Videla_
- **Nombre del Integrante 4**: _Joaquin Palacio Feijoo_


## Historial de Cambios

Todas las versiones importantes y sus cambios correspondientes se documentan en este archivo.

### [Alpha] - 2024-06-03

- **Realizado:**
  - Primera reunion grupal para eleccion y definicion de temas.

### [v1.0.0] - 2024-06-04

- **Implementado:**
  - Sintetizacion de ideas 
  - Primera version del proyecto lado scraping.


### [v1.1.0] - 2024-06-05
- **Implementado:**
  - Modularizacion del proyecto. 
  - Primera version del proyecto lado scraping.
  - Implementacion del funcionamiento basico y conexion entre archivos json resultantes del scrapper y muestra en primer pantalla primitiva UI.

- **Optimizado:**
  - Optimizacion del codigo para mejor rendimiento.
  - Optimizacion legible del codigo

- **Solucionado:**
  - Solucionado problemas de rendimiento
  - Problemas de funcionamiento en determinados PC

 


*Nota*: Los cambios anteriores son solo una selección de las actualizaciones más importantes. Para ver todos los cambios, consulta el registro de cambios completo en [Historial de Cambios](#historial-de-cambios).

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal del proyecto.
- **ScraPy**: Framework para la extracción de datos de sitios web.
- **PyQt6**: Conjunto de herramientas para la creación de interfaces gráficas de usuario.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias:

```sh
pip install scrapy
pip install pyqt6
```

## Instrucciones de Uso - Basico

- Clonar el repositorio a tu propia pc para ejecutar el script **ScraPy**:
```sh
git clone https://github.com/tu-usuario/Proyecto-P.A-UNAB.git
```

- Navegar mediante CMD al directorio del proyecto _**Comparativer**_ :
```sh
cd Proyecto-P.A-UNAB
```

- Ejecutar el script:
```sh
python main.py
```

## Instrucciones de Uso - Avanzado

- Dentro de la carpeta del proyecto, puedes ejecutar el script del scraping individual:
```sh
scrapy crawl scrapper -o items.json
```


## Estructura del Proyecto

- `main.py`: Archivo principal que inicia la aplicación.
- `scrapperComparative/`: Carpeta contenedora de la funcion scraping.
    - `spiders/`: Carpeta contenedora de la spider ejecutante del script.
        - `spider.py`: Archivo spider encargado de ejecutar el script.
- `pyqt_ui/`: Contiene los archivos de la interfaz gráfica de PyQt.
  - `config/`: Contiene los archivos de configuracion de las ventanas del programa
  - `modules/`: Contiene todos los modulos funcionales del proyecto
  - `src/`: Contiene todos los recursos graficos del proyecto

## ¡Gracias por seguir nuestro proyecto!

¡Gracias por seguir nuestro proyecto y revisar nuestro historial de cambios! Si tienes alguna pregunta o sugerencia, no dudes en comunicarte con nosotros. ¡Saludos!

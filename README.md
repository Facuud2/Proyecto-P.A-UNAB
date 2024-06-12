# Proyecto-P.A-UNAB

## Descripción

Este proyecto fue desarrollado en Python utilizando las librerías **Scrapy** y **PyQt** para la asignatura de Programación Avanzada de la Tecnicatura en Programación de la Universidad Nacional de Almirante Brown (UNaB).

### Integrantes del Grupo

- **Facundo David Carrizo Lucero**
- **Camila Abigail Juan**
- **Milagros Videla**
- **Joaquín Palacio Feijoo**

## Historial de Cambios

Todas las versiones importantes y sus cambios correspondientes se documentan en este archivo.

### [Alpha] - 2024-06-03

- **Realizado:**
  - Primera reunión grupal para elección y definición de temas.

### [v1.0.0] - 2024-06-04

- **Implementado:**
  - Sintetización de ideas.
  - Primera versión del proyecto, lado scraping.

### [v1.1.0] - 2024-06-05

- **Implementado:**
  - Modularización del proyecto.
  - Primera versión del proyecto, lado scraping.
  - Implementación del funcionamiento básico y conexión entre archivos JSON resultantes del scraper, y muestra en primera pantalla primitiva UI.

- **Optimizado:**
  - Optimización del código para mejor rendimiento.
  - Mejor legibilidad del código.

- **Solucionado:**
  - Problemas de rendimiento.
  - Problemas de funcionamiento en determinados PC.

*Nota*: Los cambios anteriores son solo una selección de las actualizaciones más importantes. Para ver todos los cambios, consulta el registro de cambios completo en [Historial de Cambios](#historial-de-cambios).

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal del proyecto.
- **Scrapy**: Framework para la extracción de datos de sitios web.
- **PyQt6**: Conjunto de herramientas para la creación de interfaces gráficas de usuario.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las dependencias necesarias para su correcto funcionamiento. Puedes instalarlas ejecutando:

```sh
pip install -r requirements.txt
```

O bien, si prefieres instalarlas manualmente:

```sh
pip install scrapy
pip install pyqt6
```

## Instrucciones de Uso - Básico

- Clonar el repositorio:

```sh
git clone https://github.com/tu-usuario/Proyecto-P.A-UNAB.git
```

- Navegar al directorio del proyecto desde la terminal:
```sh
cd Proyecto-P.A-UNAB
```

- Ejecutar el programa:
```sh
python main.py
```

## Instrucciones de Uso - Avanzado

- Ejecutar el script de scraping individual de **Mercado Libre**:

```sh
scrapy crawl scrapper_ml -o items_ml.json
```

- Ejecutar el script de scraping individual de **eBay**:

```sh
scrapy crawl scrapper_ebay -o items_ebay.json
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

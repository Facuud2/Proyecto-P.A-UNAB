# Proyecto-P.A-UNAB

## Descripción

Este proyecto fue desarrollado en Python utilizando las librerías **Scrapy** y **PyQt** para la asignatura de Programación Avanzada de la Tecnicatura en Programación de la Universidad Nacional de Almirante Brown (UNaB).

### Integrantes del Grupo

- **Nombre del Integrante 1**: _Facundo David Carrizo Lucero_
- **Nombre del Integrante 2**: _Camila Abigail Juan_
- **Nombre del Integrante 3**: _Milagros Videla_
- **Nombre del Integrante 4**: _Joaquin Palacio Feijoo_

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal del proyecto.
- **ScraPy**: Framework para la extracción de datos de sitios web.
- **PyQt**: Conjunto de herramientas para la creación de interfaces gráficas de usuario.

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias:

```sh
pip install scrapy
pip install pyqt5
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

def config_window(self):
    """
    Configura la posición y el título de la ventana.

    Esta funcion configura el titulo como 'ScrapOps' y la ubicacion de la ventana en el centro de la pantalla.

    Parameters:
        self (QWidget): La ventana a configurar.

    Returns:
        None
    """

    # Establece el titulo de la ventana
    self.setWindowTitle('ScrapOps')

    # Establece la ubicacion de la ventana
    self.setGeometry(300, 500, 1024, 768)

    # Muestra la ventana
    self.show()

    # Toma la ubicacion de la pantalla
    screen_geometry = self.screen().geometry()

    # Toma la ubicacion de la ventana
    window_geometry = self.geometry()

    # Calcula la posicion del centro de la pantalla para la ventana
    x = (screen_geometry.width() - window_geometry.width()) // 2
    y = (screen_geometry.height() - window_geometry.height()) // 2

    # Mueve la ventana al centro de la pantalla
    self.move(x, y)

def config_window(self):
    self.setWindowTitle('ScrapOps')
    self.setGeometry(300, 500, 1024, 768)
    self.show()
    screen_geometry = self.screen().geometry()
    window_geometry = self.geometry()




    x = (screen_geometry.width() - window_geometry.width()) // 2
    y = (screen_geometry.height() - window_geometry.height()) // 2

    self.move(x, y)
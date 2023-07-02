import ctypes

SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, "C:\\Users\\user\\Desktop\\ии\\pyPomoshnik\\image.jpg", 3)
import ctypes
import random as r

контейнер = ["C:\\Users\\user\\Desktop\\ии\\pyPomoshnik\\картинки\\image.jpg", "C:\\Users\\user\\Desktop\\ии\\pyPomoshnik\\картинки\\image2.jpg", "C:\\Users\\user\\Desktop\\ии\\pyPomoshnik\\картинки\\image3.jpg", "C:\\Users\\user\\Desktop\\ии\\pyPomoshnik\\картинки\\image4.jpg"]

определение = r.choice(контейнер)
SPI_SETDESKWALLPAPER = 20
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, определение, 3)
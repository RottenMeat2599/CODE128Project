from barcode import Barcode

# Создаем объект
b = Barcode()

# Генерируем штрихкод
if b.generate("HI44444", "C:\\Users\\Retro\\Desktop\\barco.png"):
    print("SUCCESS!")
else:
    print("ERROR:", b.error())
import ctypes
import os


class Barcode:
    def __init__(self, dll_path=None):
        if dll_path is None:
            # Ищем DLL в той же папке, где скрипт
            dll_path = os.path.join(os.path.dirname(__file__), "code128.dll")

        self.dll = ctypes.CDLL(dll_path)

        # Настройка типов
        self.dll.CreateGenerator.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
        self.dll.CreateGenerator.restype = ctypes.c_void_p

        self.dll.GenerateBarcode.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
        self.dll.GenerateBarcode.restype = ctypes.c_bool

        self.dll.DestroyGenerator.argtypes = [ctypes.c_void_p]
        self.dll.DestroyGenerator.restype = None

        self.dll.GetLastError.argtypes = [ctypes.c_void_p]
        self.dll.GetLastError.restype = ctypes.c_char_p

        # Создаем генератор
        self._gen = self.dll.CreateGenerator(3, 100, 30)

    def generate(self, data, filename):
        """Создает штрихкод. Возвращает True если успешно."""
        return self.dll.GenerateBarcode(self._gen, data.encode(), filename.encode())

    def error(self):
        """Возвращает текст последней ошибки."""
        return self.dll.GetLastError(self._gen).decode()

    def __del__(self):
        """Уничтожает генератор при удалении объекта."""
        if hasattr(self, '_gen') and self._gen:
            self.dll.DestroyGenerator(self._gen)
class Validador():

    @staticmethod
    def esEntero(x: int, campo: str) -> int:
        if type(x) != int:
            raise ValueError("Error el campo " + campo + " debe ser un entero")
        return x

    @staticmethod
    def esEnteroPositivo(x: int, campo: str) -> int:
        if type(x) != int or x < 0:
            raise ValueError("Error el campo " + campo + " debe ser un entero positivo")
        return x

    @staticmethod
    def esStringNoVacia(x: str, campo: str) -> str:
        if type(x) != str or not x.strip():
            raise ValueError("Error el campo " + campo + " debe ser una cadena de texto no vacia")
        return x

    @staticmethod
    def esFloatPositivo(x: float, campo: str) -> float:
        if not isinstance(x, (int, float)) or x < 0:
            raise ValueError("Error el campo " + campo + " debe ser un numero flotante positivo")
        return x

    @staticmethod
    def esBooleano(x: bool, campo: str) -> bool:
        if not isinstance(x, bool):
            raise ValueError("Error el campo " + campo + " debe ser un booleano")
        return x

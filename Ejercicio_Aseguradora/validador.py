class Validador:

    @staticmethod
    def esEntero(x: int, campo: str) -> int:
        if not isinstance(x, int) or isinstance(x, bool):
            raise ValueError(f"Error el campo {campo} debe ser un entero")
        return x

    @staticmethod
    def esEnteroPositivo(x: int, campo: str) -> int:
        if not isinstance(x, int) or isinstance(x, bool) or x < 0:
            raise ValueError(f"Error el campo {campo} debe ser un entero positivo")
        return x

    @staticmethod
    def esStringNoVacia(x: str, campo: str) -> str:
        if not isinstance(x, str) or not x.strip():
            raise ValueError(f"Error el campo {campo} debe ser una cadena de texto no vacia")
        return x

    @staticmethod
    def esFloatPositivo(x: float, campo: str) -> float:
        if not isinstance(x, (int, float)) or isinstance(x, bool) or x < 0:
            raise ValueError(f"Error el campo {campo} debe ser un numero positivo")
        return float(x)

    @staticmethod
    def esBooleano(x: bool, campo: str) -> bool:
        if not isinstance(x, bool):
            raise ValueError(f"Error el campo {campo} debe ser un booleano")
        return x

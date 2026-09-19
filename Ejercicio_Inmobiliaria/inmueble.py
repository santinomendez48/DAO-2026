from abc import ABC, abstractmethod

class Inmueble(ABC):

    def __init__(self, codigo: int, propietario: str, superficie: int, alquiler_base: float):
        self.codigo = codigo
        self.propietario = propietario
        self.superficie = superficie
        self.alquiler_base = alquiler_base

    def __str__(self):
        return f"Código: {self.codigo} - Propietario: {self.propietario} - Superficie: {self.superficie} - Alquiler base: {self.alquiler_base}"

    @abstractmethod
    def alquiler(self) -> float:
        pass

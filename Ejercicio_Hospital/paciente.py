sintomas = ['corazon', 'pulmon', 'otros']

class Paciente:

    def __init__(self, nombre: str, sintoma: int, habitual: bool = False):
        self.nombre = nombre
        if sintoma not in [1, 2, 3]:
            raise ValueError("El síntoma ingresado no es válido")
        self.sintoma = sintoma
        self.habitual = habitual

    def __str__(self):
        return f"Paciente: {self.nombre} - Síntoma: {sintomas[self.sintoma - 1]} - Habitual: {self.habitual}"

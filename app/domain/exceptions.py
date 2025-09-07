# crea este archivo si no existe
class NotFoundError(Exception):
    """Se lanza cuando un agregado/entidad no existe."""
    pass

class ConflictError(Exception):
    """Se lanza cuando hay conflicto (duplicados, constraints, etc.)."""
    pass
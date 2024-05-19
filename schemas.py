from pydantic import BaseModel

class Course(BaseModel):
    nombre_del_curso: str
    descripcion: str
    id_profesor: int

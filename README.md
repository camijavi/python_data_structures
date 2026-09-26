# Contexto: Sistema de Gestión para la Feria Universitaria

La Universidad organizará una Feria Universitaria Anual, donde los estudiantes pueden participar en diferentes actividades como concursos de programación, trivias y competiciones de videojuegos. Debido a la gran cantidad de participantes, la universidad necesita un sistema sencillo que ayude a gestionar las inscripciones, los equipos de trabajo y la distribución de estudiantes en cada evento.

Para resolver este problema, se desarrollarán tres módulos:

### Módulo 1: Registro de Estudiantes (Set)

Este módulo se encarga de registrar a los estudiantes participantes. Se utiliza un **Set** para evitar registros duplicados y asegurar que cada estudiante aparezca una sola vez en el sistema.

### Módulo 2: Formación de Equipos (Tuple)

Algunas actividades requieren que los estudiantes participen en grupos. Este módulo utiliza una **Tuple** para almacenar los integrantes de un equipo, ya que una vez creado el equipo sus miembros no deben modificarse accidentalmente.

### Módulo 3: Gestión de Participantes por Evento (Dictionary)

Cada estudiante puede inscribirse en uno o varios eventos. Este módulo utiliza un **Dictionary** para relacionar cada evento con la lista de estudiantes inscritos, facilitando la consulta de participantes en cada actividad.

---

## Objetivo General

Implementar un sistema básico que permita:

- Registrar estudiantes sin duplicados.
- Organizar equipos para las competencias.
- Controlar qué estudiantes participan en cada evento.

De esta manera, la universidad podrá gestionar la feria de forma más eficiente y organizada utilizando las estructuras de datos **Set**, **Tuple** y **Dictionary** :D

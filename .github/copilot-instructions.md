# Spendly - Instrucciones para Agente IA

## Descripción del Proyecto
Spendly es una aplicación de control de gastos desarrollada con **Reflex** (frontend) y **FastAPI** (backend).

## Stack Tecnológico
- **Frontend**: Reflex (Python)
- **Backend**: FastAPI
- **Base de datos**: Por definir según necesidades
- **Lenguaje**: Python 3.11+

## Flujo de Trabajo Obligatorio

### 1. Proponer Plan Antes de Ejecutar
Antes de realizar cualquier tarea, el agente debe:
1. Presentar un plan detallado con tareas numeradas
2. Describir brevemente qué se implementará en cada tarea
3. Esperar confirmación del desarrollador antes de proceder

### 2. Ejecución Tarea por Tarea
- Ejecutar **una sola tarea** a la vez
- Al completar cada tarea, preguntar: "¿Está todo correcto? ¿Paso a la siguiente tarea?"
- No avanzar sin confirmación explícita del desarrollador

## Convenciones de Código (Obligatorias)

### Estilo PEP 8
- Seguir estrictamente las convenciones de PEP 8
- Usar **snake_case** para funciones, variables y métodos
- Usar **PascalCase** para clases
- Longitud máxima de línea: 88 caracteres (Black formatter)

### Type Hints
```python
def calcular_total(gastos: list[float]) -> float:
    """Obligatorio en todas las funciones."""
    return sum(gastos)
```

### Docstrings
Usar formato Google style en español:
```python
def registrar_gasto(monto: float, categoria: str) -> dict:
    """Registra un nuevo gasto en el sistema.
    
    Args:
        monto: Cantidad del gasto en la moneda base.
        categoria: Categoría a la que pertenece el gasto.
    
    Returns:
        Diccionario con los datos del gasto registrado.
    
    Raises:
        ValueError: Si el monto es negativo o cero.
    """
    pass
```

## Idioma
- **Código**: Español (nombres de variables, funciones, clases)
- **Comentarios y docstrings**: Español
- **UI y mensajes**: Español
- **Comunicación con desarrollador**: Español

## Licencia
MIT License - Todo el código debe cumplir con los términos de la licencia.

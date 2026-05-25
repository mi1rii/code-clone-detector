# DataBaseProject - Modelo Actual (Capas 1 y 2)

## 1) Estado actual
Este repositorio contiene el modelo actual de clasificacion de clones de codigo en Python.

El flujo final integra:
- Capa 1 lexica (tokenizacion, normalizacion, TF-IDF, similitudes por tokens y Baker simplificado).
- Capa 2 estructural (rasgos sintacticos de estilo AST reducido por par de snippets).
- Clasificador final Random Forest.

## 2) Notebook principal
- `Modelo_Actual_Capa1_Lexica.ipynb`

El notebook esta organizado por etapas:
1. Configuracion e imports
2. Dataset y reconstruccion de pares
3. Preprocesamiento
4. Capa 1 lexica
5. Capa 2 estructural y vector final
6. Split por `problem_id`
7. Entrenamiento
8. Evaluacion e interpretacion

## 3) Estructura de datos actual
- `pares_clones/T1`
- `pares_clones/T2`
- `pares_clones/T3`
- `pares_clones/T4`

Cada archivo `.py` contiene un par de snippets separados por bloques en blanco.

## 4) Requisitos
Python 3.10+ recomendado.

```bash
pip install pandas numpy scipy scikit-learn matplotlib jupyter
```

## 5) Ejecucion
Desde la raiz del repo:

```bash
cd DataBaseProject
jupyter notebook
```

Abrir `Modelo_Actual_Capa1_Lexica.ipynb` y ejecutar celdas en orden (`Restart & Run All`).

## 6) Notas tecnicas
- El split se hace por grupos con `GroupShuffleSplit` usando `problem_id` para evitar fuga de informacion.
- TF-IDF se ajusta con train y se aplica a val/test.
- El vector final combina capa lexica + capa estructural.
- El foco de analisis esta en `type_III` y `type_IV` por su mayor dificultad.

## 7) Siguiente iteracion
Con esta version estable, los siguientes incrementos propuestos son:
1. Capa de contexto
2. Capa de embeddings

# DataBaseProject - Modelo Actual (Capa 1 Lexica)

## 1) Estado de esta branch
Esta branch representa el **modelo actual** de clasificacion de clones de codigo en Python.

En esta version, la **capa 1 lexica** ya esta integrada en el flujo principal del modelo:
- tokenizacion y normalizacion de codigo,
- features lexicas clasicas (TF-IDF + similitudes de tokens),
- similitud tipo Baker (tokenizacion generalizada + matches contiguos).

No se usa narrativa historica ni comparaciones paralelas como flujo principal.

## 2) Notebook principal
- `Modelo_Actual_Capa1_Lexica.ipynb`

Este notebook contiene la narrativa completa del modelo actual:
1. Introduccion del modelo
2. Dataset y reconstruccion de snippets
3. Preprocesamiento
4. Capa lexica (incluye Baker de forma nativa)
5. Vector final de features del modelo
6. Split por `problem_id`
7. Entrenamiento del modelo
8. Evaluacion del modelo
9. Interpretacion
10. Siguiente capa (AST, contexto, embeddings)

## 3) Estructura de datos
- `clone_pairs_dataset_metadata.csv`
- `pares_clones/py/tipos_de_clones/T1`
- `pares_clones/py/tipos_de_clones/T2`
- `pares_clones/py/tipos_de_clones/T3`
- `pares_clones/py/tipos_de_clones/T4`

Cada archivo `.py` contiene pares de snippets.

## 4) Requisitos
Python 3.10+ recomendado.

```bash
pip install pandas numpy scipy scikit-learn matplotlib jupyter
```

## 5) Ejecucion
Desde raiz del repo:

```bash
cd DataBaseProject
jupyter notebook
```

Abrir `Modelo_Actual_Capa1_Lexica.ipynb` y ejecutar celdas en orden.

## 6) Notas tecnicas del modelo
- Se mantiene split por grupos con `GroupShuffleSplit` usando `problem_id`.
- El vectorizador TF-IDF se ajusta solo con train para evitar fuga de informacion.
- Baker forma parte de la capa lexica del modelo (no es bloque opcional aparte).

## 7) Continuidad del proyecto
Con esta capa 1 establecida, los siguientes incrementos son:
1. Capa AST
2. Capa de contexto
3. Capa de embeddings

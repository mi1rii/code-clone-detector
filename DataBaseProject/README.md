# DataBaseProject - Modelo Actual (Capas 1 y 2)

## 1) Estado de esta branch
Esta branch representa el **modelo actual** de clasificacion de clones de codigo en Python.

En esta version, el modelo integra:
- **Capa 1 lexica**:
- tokenizacion y normalizacion de codigo,
- features lexicas clasicas (TF-IDF + similitudes de tokens),
- similitud tipo Baker (tokenizacion generalizada + matches contiguos).
- **Capa 2 estructural (AST)**:
- rasgos sintacticos por snippet,
- rasgos diferenciales por par,
- similitudes estructurales entre snippets.

No se usa narrativa historica como flujo principal.

## 2) Notebook principal
- `Modelo_Actual_Capa1_Lexica.ipynb`

Este notebook contiene la narrativa completa del modelo actual:
1. Introduccion del modelo
2. Dataset y reconstruccion de snippets
3. Preprocesamiento
4. Capa lexica (incluye Baker de forma nativa)
5. Capa estructural AST y vector final de features
6. Split por `problem_id`
7. Entrenamiento y comparacion de versiones del modelo
8. Evaluacion comparativa
9. Interpretacion
10. Siguiente capa (contexto, embeddings)

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
- Baker forma parte de la capa lexica del modelo.
- AST forma parte de la capa estructural del modelo y se integra al vector final de features.

## 7) Continuidad del proyecto
Con capas 1 y 2 establecidas, los siguientes incrementos son:
1. Capa de contexto
2. Capa de embeddings

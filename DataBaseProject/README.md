# DataBaseProject - Guia de ejecucion y estructura

## 1) Que contiene este proyecto
Este proyecto contiene un dataset de pares de codigo para deteccion/clasificacion de clones en Python y un baseline en notebook con `DecisionTree` para clasificar tipos de clon (`type_I`, `type_II`, `type_III`, `type_IV`).

## 2) Estructura (solo `DataBaseProject`)

### Archivos de la raiz
- `Baseline_Colab_DecisionTree.ipynb`  
  Notebook principal del baseline. Flujo:
  - carga `clone_pairs_dataset_metadata.csv`
  - reconstruye pares `code_a`/`code_b` leyendo archivos de `pares_clones/...`
  - preprocesa codigo (quita comentarios, normaliza espacios, tokeniza)
  - construye features (TF-IDF + metricas de similitud)
  - hace split por `problem_id` (train/val/test)
  - entrena `DecisionTreeClassifier`
  - reporta metricas y matriz de confusion.

- `clone_pairs_dataset_metadata.csv`  
  Metadata del dataset (8400 filas):
  - columnas: `is_clone, clone_type, source_group, filename, file_path, problem_id, snippet_index_a, snippet_index_b`
  - distribucion actual: 2100 ejemplos por tipo (`type_I` a `type_IV`).

- `README.md`  
  Este documento.

### Carpeta de datos
- `pares_clones/py/tipos_de_clones/T1`
- `pares_clones/py/tipos_de_clones/T2`
- `pares_clones/py/tipos_de_clones/T3`
- `pares_clones/py/tipos_de_clones/T4`

Cada carpeta contiene archivos `.py` con **2 snippets** por archivo (separados por saltos de linea en blanco).  
Convencion de nombres: `T1_000001.py`, `T2_000001.py`, etc.

Nota: tambien existe `pares_clones/.DS_Store`, es un archivo de sistema y se puede ignorar.

### Carpeta `scripts`
- `scripts/reconstruir_clone_pairs_metadata.py`  
  Reconstruye `clone_pairs_dataset_metadata.csv` recorriendo `pares_clones/py/tipos_de_clones/T1..T4`.

- `scripts/generar_plagio_tipo1.py`  
  Genera ejemplos sinteticos `type_I` y actualiza metadata. Tambien puede limpiar sinteticos previos.

- `scripts/detectar_tipo2_en_false_semantic.py`  
  Detecta candidatos `type_II` desde metadata (por defecto `source_group=pares_t2`) usando comparacion de tokens normalizados. Puede copiar candidatos a `pares_clones/py/tipos_de_clones/T2_detectados`.

- `scripts/reorganizar_tipos_clones.py`  
  Valida/normaliza la estructura `pares_clones/py/tipos_de_clones/T1..T4` y puede renombrar secuencialmente archivos.

- `scripts/aumentar_t1_t2_desde_t3_t4.py`  
  Aumenta cantidad de ejemplos T1/T2 usando snippets de T3/T4 dentro de `pares_clones/py/tipos_de_clones` (insercion de comentarios y renombrado de variables).

- `scripts/reporte_false_semantic_tipo2.csv`  
  Reporte CSV generado por el script de deteccion de tipo II.

## 3) Requisitos
Recomendado Python 3.10+.

Instalacion de dependencias para el notebook:

```bash
pip install pandas numpy scipy scikit-learn matplotlib jupyter
```

## 4) Como correr el baseline (notebook)

### Opcion A: desde VS Code / Jupyter
1. Abrir `DataBaseProject/Baseline_Colab_DecisionTree.ipynb`.
2. Seleccionar kernel de Python con las dependencias instaladas.
3. Ejecutar todas las celdas en orden.

### Opcion B: levantar Jupyter desde terminal
Desde la raiz del repo:

```bash
cd DataBaseProject
jupyter notebook
```

Luego abrir `Baseline_Colab_DecisionTree.ipynb` y ejecutar todas las celdas.

## 5) Como ejecutar scripts
Desde la raiz del repo (`code-clone-detector`):

```bash
python DataBaseProject/scripts/reconstruir_clone_pairs_metadata.py
```

```bash
python DataBaseProject/scripts/generar_plagio_tipo1.py --help
python DataBaseProject/scripts/detectar_tipo2_en_false_semantic.py --help
python DataBaseProject/scripts/reorganizar_tipos_clones.py --help
python DataBaseProject/scripts/aumentar_t1_t2_desde_t3_t4.py --help
```

## 6) Importante sobre rutas/carpetas
En esta copia del proyecto los scripts y notebook funcionan sobre:
- `pares_clones/py/tipos_de_clones`
- `clone_pairs_dataset_metadata.csv`

Algunos scripts conservan compatibilidad hacia rutas legadas (`false_semantic_clones` / `true_semantic_clones`), pero ya no son requeridas para el flujo principal.

## 7) Resumen rapido
- Si tu objetivo es entrenar/probar el baseline: usa solo el notebook + metadata + `pares_clones`.
- Si tu objetivo es regenerar o reorganizar datasets: usa los scripts de `scripts/` y valida primero que existan las carpetas esperadas.

## 8) Analisis de resultados del notebook (ejecucion guardada)

### 8.1 Balanceo de datos
- Filas totales en metadata: `8400`.
- Solo clase positiva (`is_clone=1`): `8400`.
- Balance por tipo de clon:
  - `type_I`: `2100`
  - `type_II`: `2100`
  - `type_III`: `2100`
  - `type_IV`: `2100`

Conclusion: para Task tipo de clon (clasificar tipo de clon) el dataset esta perfectamente balanceado entre clases.

### 8.2 Split entrenamiento/validacion/prueba
El notebook hace split por grupos (`problem_id`) con `GroupShuffleSplit`.

Resultados reportados:
- `train`: `5880` filas (`1470` por clase)
- `val`: `1260` filas (`315` por clase)
- `test`: `1260` filas (`315` por clase)

Interpretacion:
- El split esta balanceado por clase.
- Al agrupar por `problem_id`, reduce riesgo de fuga de informacion entre train y test para pares relacionados.

### 8.3 Entrenamiento vs evaluacion (si esta bien separado)
Si, el flujo esta bien separado:
- El vectorizador TF-IDF se ajusta con `train` (fit en train).
- `val` y `test` solo usan transformacion y prediccion (sin reentrenar).
- Metricas se calculan aparte para `val` y `test`.

Conclusion: no se ve mezcla directa de datos de evaluacion dentro del entrenamiento.

### 8.4 Metricas reportadas (Task tipo de clon)
- Validacion:
  - `accuracy`: `0.85`
  - `f1_macro`: `0.8492`
- Prueba:
  - `accuracy`: `0.8587`
  - `f1_macro`: `0.8580`

Por clase en test:
- `type_I`: precision/recall/f1 muy alto (~`0.99`)
- `type_II`: tambien alto (~`0.97`)
- `type_III`: mas bajo (`f1 ~0.74`)
- `type_IV`: mas bajo (`f1 ~0.73`)

Interpretacion:
- El modelo distingue muy bien clones tipo I/II.
- La mayor confusion esta entre `type_III` y `type_IV`, algo esperable por similitud semantica/estructural.

### 8.5 Sobre el balanceo configurado (`undersample`)
Aunque la estrategia esta en `undersample`, en esta corrida no cambia nada:
- antes: `1470` por clase en train
- despues: `1470` por clase en train

Razon: ya estaba balanceado, por eso no recorta datos.

### 8.6 Limitaciones actuales del baseline
- Este dataset/flujo es solo Task tipo de clon (`is_clone=1`), no evalua deteccion binaria clon/no-clon.
- Es un baseline con `DecisionTree`; sirve para referencia inicial, pero no necesariamente es el mejor modelo posible.
- Conviene validar estabilidad repitiendo splits con distintas semillas o cross-validation por grupos.

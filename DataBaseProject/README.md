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

- `scripts/ejecutar_experimento_baker.py`  
  Ejecuta comparacion reproducible entre:
  - baseline lexico original
  - baseline lexico + bloque Baker
  Genera reportes en `reports/`.

### Carpeta `src` (nueva integracion modular)
- `src/baker_tokenizer.py`  
  Tokenizacion Python usando `tokenize` (stdlib), filtrando tokens no significativos.
- `src/baker_generalizer.py`  
  Generalizacion lexico-estructural estilo Baker:
  - identificadores -> `ID`
  - numeros -> `NUM`
  - strings -> `STR`
  - keywords/operadores/estructura se conservan.
- `src/baker_suffix_array.py`  
  Implementacion de suffix array (prefix doubling) + LCP (Kasai).
- `src/baker_similarity.py`  
  Extrae matches contiguos comunes sobre tokens generalizados y calcula:
  - `baker_similarity`
  - `baker_common_length`
  - `baker_longest_match`
  - `baker_num_matches`
  - `baker_coverage_a`
  - `baker_coverage_b`
- `src/baseline_pipeline.py`  
  Pipeline reutilizable para:
  - carga/limpieza/reconstruccion
  - preprocesamiento y tokenizacion
  - features baseline
  - features Baker
  - split por `problem_id`
  - entrenamiento/evaluacion.

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

Experimento comparativo baseline vs baseline+Baker:

```bash
python DataBaseProject/scripts/ejecutar_experimento_baker.py
```

Opcional (parametros):

```bash
python DataBaseProject/scripts/ejecutar_experimento_baker.py --seed 42 --estrategia-balanceo undersample --min-match-len 3
```

Tambien esta integrado **directamente en el notebook**:
- `Baseline_Colab_DecisionTree.ipynb` incluye un bloque final Baker inline
- ejecuta comparacion A/B y muestra tablas/reportes en celdas output
- no requiere guardar resultados en archivos para ver metricas

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

## 9) Extension Baker integrada (resultado actual)

### 9.1 Que se agrego
Se integro un bloque Baker modular sin eliminar features previas.  
La matriz final combina:
- Features baseline (13)
- Features Baker (6 nuevas)
- Total con Baker: 19 features.

### 9.2 Evaluacion A/B con mismo split por `problem_id`
Configuracion usada:
- `seed_split = 142`
- `estrategia_balanceo = undersample`
- `min_match_len = 3`

Resultados 4 clases (`type_I..type_IV`):
- Baseline:
  - `accuracy_test = 0.858730`
  - `f1_macro_test = 0.857996`
- Baseline + Baker:
  - `accuracy_test = 0.902381`
  - `f1_macro_test = 0.902341`

Mejora neta:
- `delta accuracy_test = +0.043651`
- `delta f1_macro_test = +0.044345`

### 9.3 Impacto por clase (TEST)
- `type_I`: `delta f1 = -0.001590`
- `type_II`: `delta f1 = +0.018926`
- `type_III`: `delta f1 = +0.080526`
- `type_IV`: `delta f1 = +0.079520`

Interpretacion:
- El bloque Baker ayuda especialmente en `type_III` y `type_IV`, que eran las clases mas dificiles en el baseline original.

### 9.4 Artefactos generados
- `reports/baseline_vs_baker_summary.csv`
- `reports/baseline_vs_baker_per_class.csv`
- `reports/features_baseline_plus_baker.csv` (dataset de features actualizado)
- `reports/baseline_vs_baker_raw_metrics.json`
- `reports/baseline_vs_baker_report.md`

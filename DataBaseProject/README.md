# DataBaseProject - Modelo Actual (Arquitectura Jerarquica)

## 1) Estado actual
Este repositorio contiene un sistema jerarquico de clasificacion de clones de codigo en Python.

El flujo final integra:
- Etapa 1: regla deterministica para `type_I` sobre codigo normalizado.
- Etapa 2: modelo Random Forest con features Baker para detectar `type_II` en los casos restantes.
- Etapa 3: modelo Random Forest con Baker + AST reducido para separar `type_III` y `type_IV`.

## 2) Notebook principal
- `Modelo_Actual_Capa1_Lexica.ipynb`

El notebook esta organizado por etapas:
1. Configuracion e imports
2. Dataset y reconstruccion de pares
3. Preprocesamiento
4. Capa 1 lexica
5. Capa 2 AST y funciones auxiliares
6. Split por `problem_id`
7. Entrenamiento jerarquico por etapas
8. Evaluacion de la arquitectura jerarquica

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

Opcional para acelerar distancia de secuencias:

```bash
pip install rapidfuzz
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
- El filtro de `type_I` es deterministico con firma canonica (sin comentarios/espacios/saltos) sobre codigo normalizado.
- La etapa `type_II` usa exclusivamente features Baker enriquecidas (ratio, distancia y cobertura).
- La etapa `type_III/type_IV` usa features Baker + AST reducido reforzado (diferencias relativas y absolutas).
- No se usan embeddings ni modelos externos nuevos.

## 7) Resultado esperado
Al ejecutar el notebook se generan:
1. Metricas globales de validacion y test.
2. Matriz de confusion de la arquitectura jerarquica.
3. Metricas por clase con foco en `type_III` y `type_IV`.
4. Importancia de features por etapa (`type_II` y `type_III/type_IV`).

# Trabalho Final de Inteligência Artificial

**Alunos:**

- Everton Luiz De Oliveira;
- Kauan Morinel Calheiro; e
- Kelli Maria Gutterres

## Descrição Parcial do Trabalho

O trabalho consiste na aplicação de métodos de aprendizado de máquina supervisionado para classificação de dados organizados em diferentes formatos, tabulares, texto e imagens. O principal objetivo é explorar diferentes técnicas, configurações e arquiteturas para avaliar quais delas permitem obter os melhores resultados.

## Bases de Dados Selecionadas

### Dados Tabulares

| **Nome da Base**         | Grape Quality                                            |
| ------------------------ | :------------------------------------------------------- |
| **Origem / Repositório** | [Kaggle - Grape Quality Dataset](https://www.kaggle.com/datasets/mrmars1010/grape-quality) |
| **Número de Entradas**   | 1.000                                                                                      |
| **Número de Atributos**  | 13                                                                                        |

A base **Grape Quality** reúne 1000 amostras de uvas com dados físico-químicos, ambientais e de origem. Cada registro inclui informações como variedade, teor de açúcar, acidez, peso do cacho e condições de cultivo, com o objetivo de classificar a qualidade da uva.

#### Atributos

| Atributo                | Tipo       |
| ----------------------- | ---------- |
| `sample_id`             | Numérico   |
| `variety`               | Categórico |
| `region`                | Categórico |
| `quality_score`         | Numérico   |
| `quality_category`      | Categórico |
| `sugar_content_brix`    | Numérico   |
| `acidity_ph`            | Numérico   |
| `cluster_weight_g`      | Numérico   |
| `berry_size_mm`         | Numérico   |
| `harvest_date`          | Categórico |
| `sun_exposure_hours`    | Numérico   |
| `soil_moisture_percent` | Numérico   |
| `rainfall_mm`           | Numérico   |

#### Rótulo (target)

**Campo:** `variety`

**Valores possíveis:**

- `Riesling`
- `Pinot Noir`
- `Sauvignon Blanc`
- `Merlot`
- `Zinfandel`
- `Chardonnay`
- `Syrah`
- `Cabernet Sauvignon`

---

### Dados Textuais

| **Nome da Base**         | 20 Newsgroups                                                                                                                  |
| ------------------------ | :----------------------------------------------------------------------------------------------------------------------------- |
| **Origem / Repositório** | [Scikit-learn Documentation - 20 Newsgroups](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html#sklearn.datasets.fetch_20newsgroups) |
| **Número de Entradas**   | 18.846                                                                                                                                                                 |
| **Número de Atributos**  | 3                                                                                                                                                                      |

A base **20 Newsgroups** contém 18.846 documentos de texto coletados de 20 grupos de notícias da internet. O objetivo é classificar os textos em uma das 20 categorias temáticas diferentes, envolvendo tópicos que vão desde esportes até política e tecnologia.

#### Atributos

| Atributo      | Tipo       |
| ------------- | ---------- |
| `text`        | Texto      |
| `target`      | Numérico   |
| `target_name` | Categórico |

#### Rótulo (target)

**Campo:** `target_name`

**Valores possíveis:**

- `rec.sport.hockey`
- `comp.sys.ibm.pc.hardware`
- `talk.politics.mideast`
- `comp.sys.mac.hardware`
- `sci.electronics`
- `talk.religion.misc`
- `sci.crypt`
- `sci.med`
- `alt.atheism`
- `rec.motorcycles`
- `rec.autos`
- `comp.windows.x`
- `comp.graphics`
- `sci.space`
- `talk.politics.guns`
- `misc.forsale`
- `rec.sport.baseball`
- `talk.politics.misc`
- `comp.os.ms-windows.misc`
- `soc.religion.christian`

---
<!-- TODO: -->
### Dados de Imagens Coloridas

**Nome da Base:**
**Origem / Repositório (link):**
**Número de Imagens:**
**Resolução / Formato:**

### Atributos

| Atributo      | Tipo  |
| ------------- | ----- |
| (ex.: review) | Texto |
| …             | …     |

**Rótulo (target):**

- Campo:
- Tipo:
- Valores possíveis:

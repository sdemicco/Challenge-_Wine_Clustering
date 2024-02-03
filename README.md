# Uncovering the Hidden Profiles in Wine Data


![portada](assets/wine_portada_img.png)

## 1. Objective
This project is focused on examining wines by conducting a detailed analysis of their features.

The dataset consists of the results of a chemical analysis of wines grown in the same region of Italy but derived from three different cultivars. The analysis determined the quantities of 13 components present in each of the three types of wines.

Patterns in the data will be sought to reveal valuable information and gain a deeper understanding of how their properties are related. The wine categories that can be used for classification will also be identified through the development of a clustering model.

<!-- Imagen redimensionada centrada con estilos en línea -->
<p align="center">
  <img src="assets/wine_properties_img.png" width="300" height="400" alt="portada">
</p>

## 1. Data exoloration

The dataset had good quality. It did not contain missing data, so there was no need to perform imputations or transformations. It also did not exhibit erroneous or atypical values. A correlation analysis between variables was conducted. Due to the nature of the data, the Spearman correlation coefficient was chosen, which does not assume linearity between variables or that the features follow a normal distribution. P-values were also calculated to determine statistically significant correlations.


The following results were obtained:


> ####  The content of Alcohol and Proline are positively correlated. As the alcohol content in a wine increases, the Proline content also increases.
> #### The hue is negatively correlated with malic acid and positively correlated with flavonoids. Wines with lower values of malic acid and higher values of flavonoids exhibit higher hues.
> #### Total_phenols is strongly correlated with Flavanoids and Proanthocyanins, which is expected since Flavanoids and Proanthocyanins are included in the total_phenols category.
> #### The color intensity is positively correlated with the alcohol content of the wine. There is also a negative correlation between the color intensity of the wine and its hue. Wines with more intense colors have lower hue.
> #### The OD280 is strongly correlated with flavonoid phenolic compounds. Also Wines with higher hues have a higher OD280 coefficient.

<!-- Imagen redimensionada centrada con estilos en línea -->
<p align="center">
  <img src="assets/correlations_img.png" width="850" height="350" alt="portada">
</p>


## 2. Clustering Analysis
## 3. Insights

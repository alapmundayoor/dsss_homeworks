import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import umap

# Load the dataset using pandas
csvpath ="C:\\NewPythonVS\\DSSS\\dsss_hw_5\\winequality-red.csv"
df = pd.read_csv(csvpath)

# Step 1: Plot the whole dataset (except 'quality' column)
# Choose suitable plots based on your dataset characteristics
# For example, pairplot or heatmap for correlations
# sns.pairplot(df.drop(columns=['quality']))
# plt.suptitle('Pairplot of Features (excluding quality)')
# plt.show()

# Step 2: Apply PCA, t-SNE, and UMAP to all remaining features
# Extract features and standardize them
X = df.drop(columns=['quality'])
X_standardized = (X - X.mean()) / X.std()

# PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_standardized)

# t-SNE
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X_standardized)

# UMAP
umap_model = umap.UMAP(n_components=2)
X_umap = umap_model.fit_transform(X_standardized)

# Plot the features for each method with color-coded quality
# Use a suitable colormap, such as 'viridis' or 'coolwarm'

# PCA Plot
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=df['quality'], cmap='viridis')
plt.title('PCA - Wine Quality')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar(label='Wine Quality')
plt.show()

# t-SNE Plot
plt.scatter(X_tsne[:, 0], X_tsne[:, 1], c=df['quality'], cmap='viridis')
plt.title('t-SNE - Wine Quality')
plt.xlabel('t-SNE Dimension 1')
plt.ylabel('t-SNE Dimension 2')
plt.colorbar(label='Wine Quality')
plt.show()

# UMAP Plot
plt.scatter(X_umap[:, 0], X_umap[:, 1], c=df['quality'], cmap='viridis')
plt.title('UMAP - Wine Quality')
plt.xlabel('UMAP Dimension 1')
plt.ylabel('UMAP Dimension 2')
plt.colorbar(label='Wine Quality')
plt.show()

# Step 3: Perform a statistical test (e.g., t-test or ANOVA) on your chosen feature
# Note: Replace 'feature_of_interest' with the feature you are interested in
# Use scipy.stats functions for the test

from scipy.stats import ttest_ind

feature_of_interest = 'alcohol'  # Replace with your chosen feature
high_quality = df[df['quality'] >= 7][feature_of_interest]
low_quality = df[df['quality'] < 7][feature_of_interest]

# Perform a t-test
t_stat, p_value = ttest_ind(high_quality, low_quality)

# Present your hypothesis, chosen test, and conclusions
print(f'Hypothesis: Wines with higher {feature_of_interest} are associated with higher quality.')
print(f'Test: Independent t-test comparing {feature_of_interest} for high and low-quality wines.')
print(f'Conclusions: The p-value is {p_value:.4f}. Based on this result, we {"reject" if p_value < 0.05 else "fail to reject"} the null hypothesis.')

# 4. Working with Data

## Importance of Data in ML
- Data is the foundation of machine learning. The quality and representation of data directly affect model performance.

## Types of Data
- **Numerical Data**: Quantitative values (e.g., age, price, temperature).
- **Categorical Data**: Qualitative values (e.g., color, country, product type).

## Working with Numerical Data
- **Feature Vectors**: Arrays of numbers representing input data.
- **Normalization**: Scaling values to a standard range (e.g., 0-1) to help models learn efficiently.
- **Binning**: Grouping continuous values into discrete bins.
- **Scrubbing**: Cleaning data by handling missing or incorrect values.
- **Polynomial Transforms**: Creating new features by raising existing features to a power.

## Working with Categorical Data
- **One-Hot Encoding**: Representing categories as binary vectors.
- **Feature Hashing**: Mapping categories to integers using a hash function.
- **Mean Encoding**: Replacing categories with the mean of the target variable for each category.
- **Feature Crosses**: Combining two or more features to capture interactions.

## Data Preparation Steps
1. Collect and inspect data.
2. Clean and preprocess (handle missing values, outliers).
3. Transform features (normalize, encode, cross, etc.).
4. Split into training, validation, and test sets.

## Example Use Cases
- Predicting house prices (numerical: size, age; categorical: location, type).
- Customer segmentation (categorical: region, product; numerical: purchase amount).

---
Next: 5. Datasets, Generalization, and Overfitting 
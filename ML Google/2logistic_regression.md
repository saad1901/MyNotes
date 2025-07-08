# 2. Logistic Regression

## What is Logistic Regression?
- Logistic regression is a supervised learning algorithm for classification tasks (predicting categories).
- It models the probability that an input belongs to a particular class using the logistic (sigmoid) function.
- Output is a value between 0 and 1, interpreted as a probability.

## Key Concepts
- **Sigmoid Function**: \( \sigma(z) = \frac{1}{1 + e^{-z}} \ )
- **Model Equation**: \( y = \sigma(wx + b) \)
- **Loss Function**: Binary cross-entropy (log loss) is commonly used:
  \( \text{Log Loss} = -[y \log(\hat{y}) + (1-y)\log(1-\hat{y})] \)
- **Thresholding**: If output > 0.5, predict class 1; else, class 0 (threshold can be adjusted).

## Steps in Logistic Regression
1. Initialize weights and bias.
2. Compute weighted sum of inputs, apply sigmoid to get probability.
3. Calculate loss (log loss) between predicted and actual labels.
4. Update weights and bias to minimize loss (using gradient descent).
5. Repeat steps 2-4 until loss is minimized.

## Example Use Cases
- Email spam detection (spam or not spam).
- Disease diagnosis (positive or negative).

## Visual Intuition
- The model fits an S-shaped curve to the data, separating classes.
- The output is the probability of belonging to the positive class.

---
Next: 3. Classification 
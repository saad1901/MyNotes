# 1. Linear Regression

## What is Linear Regression?
- Linear regression is a fundamental supervised learning algorithm for predicting a numeric value (regression task).
- It models the relationship between input features (x) and a continuous output (y) using a straight line:  
  \( y = wx + b \)

## Key Concepts
- **Model**: The line (or hyperplane) defined by weights (w) and bias (b).
- **Loss Function**: Measures how well the model predicts the target. Commonly, Mean Squared Error (MSE):
  \( \text{MSE} = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y}_i)^2 \)
- **Gradient Descent**: An optimization algorithm to minimize the loss by adjusting weights and bias.
- **Hyperparameters**: Settings like learning rate, batch size, number of iterations.

## Steps in Linear Regression
1. Initialize weights and bias.
2. Predict output for inputs using current weights and bias.
3. Calculate loss (error) between predictions and actual values.
4. Update weights and bias to reduce loss (using gradient descent).
5. Repeat steps 2-4 until loss is minimized.

## Example Use Cases
- Predicting house prices based on features (size, location, etc.).
- Estimating travel time based on distance and traffic.

## Visual Intuition
- The model tries to fit a line that best represents the trend in the data.
- The closer the points are to the line, the better the model.

---
Next: 2. Logistic Regression 
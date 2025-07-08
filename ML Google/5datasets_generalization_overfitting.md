# 5. Datasets, Generalization, and Overfitting

## Datasets in Machine Learning
- **Dataset**: Collection of data used to train and evaluate models.
- **Labels**: The correct answers for supervised learning.
- **Imbalanced Dataset**: When some classes are much more frequent than others.

## Data Splitting
- **Training Set**: Used to train the model.
- **Validation Set**: Used to tune hyperparameters and evaluate during training.
- **Test Set**: Used to assess final model performance.

## Generalization
- The ability of a model to perform well on new, unseen data.
- Good generalization means the model captures underlying patterns, not just memorizes training data.

## Overfitting
- When a model learns the training data too well, including noise and outliers, and performs poorly on new data.
- **Symptoms**: High accuracy on training set, low accuracy on validation/test set.
- **Causes**: Too complex model, not enough data, too many features.

## Preventing Overfitting
- **Regularization**: Techniques like L2 regularization add a penalty for large weights.
- **Simpler Models**: Use less complex models.
- **More Data**: Collect more training data.
- **Early Stopping**: Stop training when validation loss starts increasing.

## Interpreting Loss Curves
- Plot training and validation loss over epochs.
- If validation loss increases while training loss decreases, overfitting is likely.

## Example Use Cases
- Medical diagnosis: Avoid overfitting to rare cases.
- Fraud detection: Handle imbalanced datasets carefully.

---
Next: 6. Neural Networks 
# 3. Classification

## What is Classification?
- Classification is a supervised learning task where the goal is to assign inputs to one of several categories (classes).
- Can be binary (two classes) or multi-class (more than two classes).

## Key Concepts
- **Binary Classification**: Two possible classes (e.g., spam vs. not spam).
- **Multi-class Classification**: More than two classes (e.g., classifying types of animals).
- **Confusion Matrix**: Table showing true/false positives/negatives for predictions.
- **Metrics**:
  - **Accuracy**: Proportion of correct predictions.
  - **Precision**: Proportion of positive predictions that are correct.
  - **Recall**: Proportion of actual positives that are correctly predicted.
  - **F1 Score**: Harmonic mean of precision and recall.
  - **ROC/AUC**: Measures model's ability to distinguish between classes.

## Steps in Classification
1. Choose a model (e.g., logistic regression, decision tree, neural network).
2. Train the model on labeled data.
3. Predict class labels for new data.
4. Evaluate performance using metrics above.

## Example Use Cases
- Email spam detection.
- Image recognition (cat, dog, car, etc.).
- Disease diagnosis (positive, negative, unknown).

## Visual Intuition
- The model tries to find boundaries that separate different classes in the data.
- For binary, a line or curve; for multi-class, more complex boundaries.

---
Next: 4. Working with Data 
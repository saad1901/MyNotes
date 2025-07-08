# 6. Neural Networks

## What are Neural Networks?
- Neural networks are a class of machine learning models inspired by the human brain.
- They consist of layers of interconnected nodes (neurons) that transform input data to output predictions.

## Key Concepts
- **Perceptron**: The simplest neural network unit (single neuron).
- **Layers**:
  - **Input Layer**: Receives input data.
  - **Hidden Layers**: Intermediate layers that learn complex patterns.
  - **Output Layer**: Produces final prediction.
- **Activation Function**: Non-linear function applied at each neuron (e.g., ReLU, sigmoid, tanh).
- **Weights and Biases**: Parameters learned during training.
- **Backpropagation**: Algorithm for updating weights using gradients from the loss function.

## Training Neural Networks
1. Forward pass: Compute outputs layer by layer.
2. Compute loss: Measure error between prediction and actual value.
3. Backward pass: Use backpropagation to compute gradients.
4. Update weights: Adjust parameters to minimize loss.
5. Repeat for many epochs.

## Example Use Cases
- Image recognition (e.g., classifying handwritten digits).
- Natural language processing (e.g., sentiment analysis).

## Visual Intuition
- Data flows through layers, with each layer learning increasingly abstract features.
- Deep networks (many layers) can learn very complex patterns.

---
Next: 7. Embeddings 
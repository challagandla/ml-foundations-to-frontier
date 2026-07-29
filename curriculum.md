# Curriculum

Single source of truth for course scope and order. Status reflects what's actually built on disk right now, not the final plan -- update as modules get built.

**Progress: 5 / 45 modules fully built.**


## Phase 0 -- Foundations (modules 00-10)

- **00 · Orientation & How This Course Works** — DONE  
  How the HTML + notebook format works, how deep-dive sections work, how progress is tracked.
- **01 · Python I: Values, Variables & Control Flow** — DONE  
  Your first programming language: values and types, variables, expressions, and the if/while/for statements that steer a program.
- **02 · Python II: Functions & Data Structures** — DONE  
  Functions as reusable building blocks, plus Python's core containers -- lists, tuples, dicts, sets -- slicing, mutability, and comprehensions.
- **03 · Python III: Errors, Files, Classes & Modules** — DONE  
  Reading tracebacks, handling exceptions, working with files, and just enough object-oriented Python to read any ML library's API.
- **04 · Linear Algebra Essentials** — DONE  
  Vectors, matrices, dot products, norms, and matrix multiplication as geometric transformations.
- **05 · Calculus for ML** — stub  
  Derivatives, partial derivatives, gradients, the chain rule, and optimization as walking downhill.
- **06 · Probability & Statistics Essentials** — stub  
  Distributions, mean/variance/std, correlation vs. causation, Bayes' theorem intuition, sampling.
- **07 · Python for ML: NumPy & Vectorized Computing** — stub  
  Arrays, broadcasting, vectorized operations vs. loops, and why vectorization matters for ML.
- **08 · Python for ML: Pandas & Data Wrangling** — stub  
  DataFrames, cleaning, merging, groupby, and handling missing data.
- **09 · Data Visualization Basics** — stub  
  matplotlib/plotly fundamentals used as the visualization toolkit for the rest of the course.
- **10 · What is Machine Learning?** — stub  
  Supervised / unsupervised / reinforcement learning, the ML workflow, and an overfitting preview.

## Phase 1 -- Classical ML (modules 11-27)

- **11 · Linear Regression I: Simple Linear Regression** — stub  
  Fitting a line, the cost function (MSE), least squares vs. gradient descent, and residuals. The flagship module.
- **12 · Linear Regression II: Multiple Regression & Gradient Descent** — stub  
  Multiple features, the normal equation, gradient descent mechanics, and feature scaling.
- **13 · Regularization: Ridge, Lasso, Elastic Net** — stub  
  Why regularize, L1 vs. L2 geometrically, and the effect on bias and variance.
- **14 · Polynomial Regression, Feature Engineering & Bias-Variance Tradeoff** — stub  
  Nonlinear fits via feature transforms, and diagnosing underfit/overfit visually.
- **15 · Model Evaluation & Validation I** — stub  
  Train/test split, k-fold cross-validation, and regression metrics (MSE, RMSE, MAE, R^2).
- **16 · Logistic Regression & Classification Basics** — stub  
  Sigmoid, decision boundaries, and log-loss.
- **17 · Classification Metrics** — stub  
  Confusion matrix, precision/recall/F1, ROC/AUC, and class imbalance.
- **18 · k-Nearest Neighbors** — stub  
  Instance-based learning, distance metrics, and the curse of dimensionality.
- **19 · Decision Trees** — stub  
  Splitting criteria (Gini/entropy), overfitting a tree, and pruning.
- **20 · Ensemble Methods I: Bagging & Random Forests** — stub  
  Variance reduction via averaging, and feature importance.
- **21 · Ensemble Methods II: Boosting** — stub  
  AdaBoost, gradient boosting, and XGBoost/LightGBM concepts.
- **22 · Support Vector Machines** — stub  
  Margins and kernel-trick intuition, visually rather than by heavy derivation.
- **23 · Naive Bayes** — stub  
  Probabilistic classification and the conditional independence assumption.
- **24 · Unsupervised Learning I: Clustering** — stub  
  k-means, hierarchical clustering, DBSCAN, and choosing k.
- **25 · Unsupervised Learning II: Dimensionality Reduction** — stub  
  PCA (geometric intuition) and t-SNE/UMAP for visualization.
- **26 · Model Selection, Hyperparameter Tuning & the ML Workflow** — stub  
  Pipelines, grid/random search, and avoiding data leakage -- ties Phase 1 together.
- **27 · Classical ML Capstone Project** — stub  
  An end-to-end mini project applying the full Phase 1 toolkit to one dataset.

## Phase 2 -- Deep Learning (modules 28-38)

- **28 · Neural Network Fundamentals I: Perceptron & Feedforward Nets** — stub  
  Neurons, layers, and the forward pass.
- **29 · Neural Network Fundamentals II: Activations & Loss Functions** — stub  
  ReLU/sigmoid/softmax and cross-entropy.
- **30 · Backpropagation Deep Dive** — stub  
  The chain rule applied through a network via computational graphs.
- **31 · Training Neural Networks** — stub  
  Optimizers (SGD/Adam), regularization, batch norm, and dropout.
- **32 · Intro to a DL Framework (PyTorch)** — stub  
  Tensors, autograd, and a basic training loop.
- **33 · CNNs I: Convolutions & Pooling Intuition** — stub  
  A visual, filter-as-feature-detector intuition for convolutions and pooling.
- **34 · CNNs II: Architectures** — stub  
  LeNet -> AlexNet -> ResNet concepts, and transfer learning.
- **35 · Sequence Models I: RNNs, LSTMs, GRUs** — stub  
  Sequential data and the vanishing gradient problem.
- **36 · Sequence Models II: Embeddings & Language Modeling Basics** — stub  
  Word2Vec/embeddings and next-token prediction.
- **37 · Attention & the Transformer Architecture** — stub  
  Self-attention, multi-head attention, and positional encoding -- the bridge to Phase 3.
- **38 · Deep Learning Capstone Project** — stub  
  An end-to-end deep learning project applying the Phase 2 toolkit.

## Phase 3 -- Applied / LLM Track (modules 39-44)

- **39 · How LLMs Work** — stub  
  Pretraining, tokenization, and scaling laws, conceptually.
- **40 · Prompt Engineering** — stub  
  Patterns, few-shot prompting, and chain-of-thought.
- **41 · Fine-Tuning LLMs** — stub  
  Full fine-tuning vs. LoRA/PEFT concepts.
- **42 · Retrieval-Augmented Generation (RAG)** — stub  
  Embeddings, vector search, and retrieval pipelines.
- **43 · Evaluating LLM Systems** — stub  
  Benchmarks, human eval, LLM-as-judge, and hallucination detection.
- **44 · Course Capstone & Where to Go Next** — stub  
  Build a small LLM app/agent, wrap up the course, and plan further learning.

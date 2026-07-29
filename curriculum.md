# Curriculum

Single source of truth for course scope and order. Status reflects what's actually built on disk right now, not the final plan -- update as modules get built.

**Progress: 2 / 42 modules fully built.**


## Phase 0 -- Foundations (modules 00-07)

- **00 · Orientation & How This Course Works** — DONE  
  How the HTML + notebook format works, how deep-dive sections work, how progress is tracked.
- **01 · Linear Algebra Essentials** — DONE  
  Vectors, matrices, dot products, norms, and matrix multiplication as geometric transformations.
- **02 · Calculus for ML** — stub  
  Derivatives, partial derivatives, gradients, the chain rule, and optimization as walking downhill.
- **03 · Probability & Statistics Essentials** — stub  
  Distributions, mean/variance/std, correlation vs. causation, Bayes' theorem intuition, sampling.
- **04 · Python for ML: NumPy & Vectorized Computing** — stub  
  Arrays, broadcasting, vectorized operations vs. loops, and why vectorization matters for ML.
- **05 · Python for ML: Pandas & Data Wrangling** — stub  
  DataFrames, cleaning, merging, groupby, and handling missing data.
- **06 · Data Visualization Basics** — stub  
  matplotlib/plotly fundamentals used as the visualization toolkit for the rest of the course.
- **07 · What is Machine Learning?** — stub  
  Supervised / unsupervised / reinforcement learning, the ML workflow, and an overfitting preview.

## Phase 1 -- Classical ML (modules 08-24)

- **08 · Linear Regression I: Simple Linear Regression** — stub  
  Fitting a line, the cost function (MSE), least squares vs. gradient descent, and residuals. The flagship module.
- **09 · Linear Regression II: Multiple Regression & Gradient Descent** — stub  
  Multiple features, the normal equation, gradient descent mechanics, and feature scaling.
- **10 · Regularization: Ridge, Lasso, Elastic Net** — stub  
  Why regularize, L1 vs. L2 geometrically, and the effect on bias and variance.
- **11 · Polynomial Regression, Feature Engineering & Bias-Variance Tradeoff** — stub  
  Nonlinear fits via feature transforms, and diagnosing underfit/overfit visually.
- **12 · Model Evaluation & Validation I** — stub  
  Train/test split, k-fold cross-validation, and regression metrics (MSE, RMSE, MAE, R^2).
- **13 · Logistic Regression & Classification Basics** — stub  
  Sigmoid, decision boundaries, and log-loss.
- **14 · Classification Metrics** — stub  
  Confusion matrix, precision/recall/F1, ROC/AUC, and class imbalance.
- **15 · k-Nearest Neighbors** — stub  
  Instance-based learning, distance metrics, and the curse of dimensionality.
- **16 · Decision Trees** — stub  
  Splitting criteria (Gini/entropy), overfitting a tree, and pruning.
- **17 · Ensemble Methods I: Bagging & Random Forests** — stub  
  Variance reduction via averaging, and feature importance.
- **18 · Ensemble Methods II: Boosting** — stub  
  AdaBoost, gradient boosting, and XGBoost/LightGBM concepts.
- **19 · Support Vector Machines** — stub  
  Margins and kernel-trick intuition, visually rather than by heavy derivation.
- **20 · Naive Bayes** — stub  
  Probabilistic classification and the conditional independence assumption.
- **21 · Unsupervised Learning I: Clustering** — stub  
  k-means, hierarchical clustering, DBSCAN, and choosing k.
- **22 · Unsupervised Learning II: Dimensionality Reduction** — stub  
  PCA (geometric intuition) and t-SNE/UMAP for visualization.
- **23 · Model Selection, Hyperparameter Tuning & the ML Workflow** — stub  
  Pipelines, grid/random search, and avoiding data leakage -- ties Phase 1 together.
- **24 · Classical ML Capstone Project** — stub  
  An end-to-end mini project applying the full Phase 1 toolkit to one dataset.

## Phase 2 -- Deep Learning (modules 25-35)

- **25 · Neural Network Fundamentals I: Perceptron & Feedforward Nets** — stub  
  Neurons, layers, and the forward pass.
- **26 · Neural Network Fundamentals II: Activations & Loss Functions** — stub  
  ReLU/sigmoid/softmax and cross-entropy.
- **27 · Backpropagation Deep Dive** — stub  
  The chain rule applied through a network via computational graphs.
- **28 · Training Neural Networks** — stub  
  Optimizers (SGD/Adam), regularization, batch norm, and dropout.
- **29 · Intro to a DL Framework (PyTorch)** — stub  
  Tensors, autograd, and a basic training loop.
- **30 · CNNs I: Convolutions & Pooling Intuition** — stub  
  A visual, filter-as-feature-detector intuition for convolutions and pooling.
- **31 · CNNs II: Architectures** — stub  
  LeNet -> AlexNet -> ResNet concepts, and transfer learning.
- **32 · Sequence Models I: RNNs, LSTMs, GRUs** — stub  
  Sequential data and the vanishing gradient problem.
- **33 · Sequence Models II: Embeddings & Language Modeling Basics** — stub  
  Word2Vec/embeddings and next-token prediction.
- **34 · Attention & the Transformer Architecture** — stub  
  Self-attention, multi-head attention, and positional encoding -- the bridge to Phase 3.
- **35 · Deep Learning Capstone Project** — stub  
  An end-to-end deep learning project applying the Phase 2 toolkit.

## Phase 3 -- Applied / LLM Track (modules 36-41)

- **36 · How LLMs Work** — stub  
  Pretraining, tokenization, and scaling laws, conceptually.
- **37 · Prompt Engineering** — stub  
  Patterns, few-shot prompting, and chain-of-thought.
- **38 · Fine-Tuning LLMs** — stub  
  Full fine-tuning vs. LoRA/PEFT concepts.
- **39 · Retrieval-Augmented Generation (RAG)** — stub  
  Embeddings, vector search, and retrieval pipelines.
- **40 · Evaluating LLM Systems** — stub  
  Benchmarks, human eval, LLM-as-judge, and hallucination detection.
- **41 · Course Capstone & Where to Go Next** — stub  
  Build a small LLM app/agent, wrap up the course, and plan further learning.

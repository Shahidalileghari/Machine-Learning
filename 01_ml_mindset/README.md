# 01 — Machine Learning Mindset

## What is machine learning?
Machine learning (ML) is a way to build systems that infer patterns from examples and use those patterns to make predictions or decisions on new examples.

In conventional programming, a developer writes explicit rules. In supervised ML, we provide examples containing inputs and known targets; a learning algorithm adjusts a model so its predictions align with those examples under a chosen objective.

### Core vocabulary
- **Sample / instance:** one example, often one row.
- **Feature:** an input variable used by a model.
- **Label / target:** the outcome we want to predict.
- **Model:** a parameterized function mapping inputs to predictions.
- **Training:** using data and an objective to fit model parameters.
- **Inference:** using the fitted model to predict on new inputs.
- **Generalization:** performance on data not used to fit the model.
- **Loss function:** a numeric penalty measuring prediction error during learning.
- **Hyperparameter:** a configuration chosen outside the model's ordinary fitting process.
- **Baseline:** a simple reference model that a more complex approach must beat.

## Main learning settings
- **Supervised learning:** examples have targets. Regression predicts numeric values; classification predicts categories.
- **Unsupervised learning:** no target labels are supplied; methods explore structure such as clusters or lower-dimensional representations.
- **Reinforcement learning:** an agent learns through actions and rewards in an environment. This course only introduces it conceptually.

## A useful mental model
Data + representation + objective + learning algorithm → fitted model → predictions.

ML is not automatically the right solution. If a stable rule is simple, transparent, and reliable, ordinary software may be better. ML needs representative data, measurable goals, and a plan for evaluating mistakes.

# 11 — Capstone: End-to-End Tabular ML

## Project goal
Build a reproducible model that predicts a clearly defined numeric or categorical target using a public, non-sensitive educational dataset or synthetic data.

## Deliverables
1. `problem_statement.md` — objective, intended user, and non-goals.
2. `data_dictionary.md` — source, row/column meanings, collection context, missingness, and limitations.
3. `notebook.ipynb` or scripts — data inspection, split, baseline, pipeline, cross-validation, evaluation.
4. `model_card.md` — intended use, evaluation, limitations, risks, and maintenance assumptions.
5. `README.md` — setup and one-command reproduction instructions.

## Workflow
1. Define target and prediction moment.
2. Inspect data and create a data dictionary.
3. Split data before fitting transformations.
4. Establish a baseline.
5. Build a preprocessing + model pipeline.
6. Select metrics based on error costs.
7. Compare models with cross-validation.
8. Evaluate once on the held-out test set.
9. Inspect errors and limitations.
10. Document what the model must not be used for.

## Evaluation rubric (100 points)
- Problem framing and data understanding: 15
- Correct splitting and leakage prevention: 20
- Baseline and model comparison: 15
- Metric choice and interpretation: 15
- Reproducibility and code quality: 15
- Limitations, fairness, and model card: 20

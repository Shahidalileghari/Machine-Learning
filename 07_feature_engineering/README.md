# 07 — Feature Engineering

Feature engineering turns raw fields into representations that make the target relationship easier for a model to learn.

Examples:
- Extract month or weekday from a timestamp when meaningful.
- Combine dimensions into a ratio when the denominator is valid.
- Group rare categories only with a documented rationale.
- Transform skewed numeric variables when useful.
- Use domain knowledge to define features available at prediction time.

Avoid target leakage, future information, and features that encode protected or sensitive attributes without a legitimate, carefully reviewed purpose. Feature importance is not causality.

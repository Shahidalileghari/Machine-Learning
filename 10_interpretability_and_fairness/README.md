# 10 — Interpretability, Fairness, and Responsible Use

A model score does not tell the whole story. Ask:
- What population does the dataset represent?
- Who is missing or underrepresented?
- Which errors are most harmful, and to whom?
- Are features proxies for sensitive attributes?
- Can a user contest or correct an output?
- Is the model being used within the context it was evaluated for?

Interpretability tools describe aspects of model behavior, but explanations can be incomplete or misleading. Correlation, feature importance, and SHAP-style attributions do not establish causality. Fairness is context-specific and may involve trade-offs between metrics; it cannot be reduced to one universal number.

Never deploy a classroom model for hiring, credit, health, policing, or other consequential decisions without appropriate domain expertise, legal review, representative evaluation, governance, and human oversight.

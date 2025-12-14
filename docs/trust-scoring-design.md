# Trust Scoring Design

Each dataset is evaluated daily across four dimensions:

1. Freshness
2. Volume Stability
3. Schema Stability
4. Downstream Business Impact

Scores range from 0 to 100 for each dimension.

---

## Final Trust Score

The final score is a weighted average of all dimensions.

Explainability was prioritized over predictive accuracy to ensure adoption by non-technical users.

---

## Trust Status Mapping

- 80–100: Green (Safe to use)
- 50–79: Amber (Use with caution)
- Below 50: Red (High risk)

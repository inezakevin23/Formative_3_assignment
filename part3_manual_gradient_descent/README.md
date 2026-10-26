## Part 3: Gradient Descent Manual Calculation

- Handwritten calculations: [Part3_Manual_Calculations.pdf](part3_manual_gradient_descent/Part3_Manual_Calculations.pdf)
- Learning rate: α = 0.01 (not given in the assignment)
- b is treated as a 2×1 vector (one bias per data point)
- Who wrote what:
  - Chain-rule derivation and Iteration 1: Andrew Thon Riem Alier
  - Iteration 2: Kevin Ineza
  - Iteration 3: Umutoni Kenia
  - Cost check, summary table and trend: Andrew Thon Riem Alier

| Iteration | m₁ | m₂ | b₁ | b₂ | Cost J |
|---|---|---|---|---|---|
| 0 | −1.0000 | 2.0000 | 1.0000 | 1.0000 | 61.0000 |
| 1 | −1.4500 | 0.8700 | 0.9900 | 0.8900 | 6.5033 |
| 2 | −1.3331 | 1.1765 | 1.0185 | 0.9121 | 2.4974 |
| 3 | −1.3690 | 1.0956 | 1.0364 | 0.8987 | 2.1645 |

**Trend:** the cost falls at every update, so m and b move in a direction that reduces the error.

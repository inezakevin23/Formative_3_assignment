# Formative 3: Probability Distributions, Bayesian Probability, and Gradient Descent

> **Presentation guide**  
> **Team number:** 6  
> **Repository:** https://github.com/inezakevin23/Formative_3_assignment
> **Notebook:** https://colab.research.google.com/drive/1q88I37Xj-F9AVMH-3wUX8Sg3-novkW52?usp=sharing


## Project overview

1. **Gaussian mixture modelling with Expectation-Maximization (EM):** estimate the parameters of two overlapping Gaussian distributions when the observations do not have class labels.
2. **Bayes' theorem on IMDb reviews:** calculate the probability that a review is positive, given that it contains a selected keyword.
3. **Gradient descent for linear regression:** derive and calculate gradients, update parameters over three iterations, verify derivatives numerically with SciPy, and visualize the parameter and cost changes.

## Setup and run instructions

### Option A — Google Colab

1. Open the final notebook in Google Colab.
2. Upload the required datasets
3. Check the data paths in the setup cells.
4. Choose **Runtime → Run all**.
5. Confirm that all cells finish without errors and that the tables and plots appear.

## Part 1 — Gaussian mixture model using EM (Kevin Ineza)

### Goal

The height observations are treated as a mixture of two Gaussian populations, without giving the algorithm a label for each observation. EM alternates between estimating how likely each observation is to belong to each component and updating the component parameters.

- **E-step:** calculate each observation's responsibility (soft membership probability) for each Gaussian component.
- **M-step:** update each component's mean, variance, and mixture weight using those responsibilities.
- **Log-likelihood:** track how well a set of statistical parameters explains observed data. it also tell us the algorithm has successfully converged to a local maximum.
- **Soft assignment:** an observation can have a probability for each component; it is not forced into a group merely because it falls on one side of the overall mean.

### Why not split the data at the global mean?

No, because the two populations are mixed together in a continuous space, their bell curves overlap significantly, which means shorter parents and taller children fall into the same height range. Drawing a hard line at the global mean creates a hard threshold that forces a data point entirely into one group or another. Instead we will use EM algorithm which calculates the posterior probability of each observation and preserve uncertainty when the distributions overlap.

## 5. Part 2 — Bayes' theorem on IMDb reviews (Andrew alier)

The implementation calculates **P(Positive | keyword)** for every selected word.

### Dataset and keyword choices

The reported run used 50,000 reviews: 25,000 positive and 25,000 negative.
Positive keywords: `superb`, `outstanding`, `wonderful`, `excellent`  
Negative keywords: `worst`, `waste`, `awful`, `terrible`

### Results to discuss

#### Positive keywords

## keyword P(Pos) P(kw|Pos) P(kw) P(Pos|kw) check #reviews

superb 0.5000 0.0410 0.0240 0.8557 0.8557 1199
outstanding 0.5000 0.0247 0.0149 0.8318 0.8318 743
wonderful 0.5000 0.0902 0.0555 0.8120 0.8120 2777
excellent 0.5000 0.1146 0.0710 0.8073 0.8073 3549

#### Negative keywords

## keyword P(Pos) P(kw|Pos) P(kw) P(Pos|kw) check #reviews

worst 0.5000 0.0164 0.0886 0.0924 0.0924 4428
waste 0.5000 0.0070 0.0507 0.0687 0.0687 2533
awful 0.5000 0.0112 0.0575 0.0977 0.0977 2875
terrible 0.5000 0.0152 0.0539 0.1413 0.1413 2696

## Part 3: Gradient Descent Manual Calculation

- Handwritten calculations: part3_manual_gradient_descent/Part3_Manual_Calculations.pdf
- Learning rate: α = 0.01 (not given in the assignment)
- b is treated as a 2×1 vector (one bias per data point)
- Who wrote what:
  - Chain-rule derivation and Iteration 1: Andrew Thon Riem Alier
  - Iteration 2: Kevin Ineza
  - Iteration 3: Umutoni Kenia
  - Cost check, summary table and trend: Andrew Thon Riem Alier

| Iteration | m₁      | m₂     | b₁     | b₂     | Cost J  |
| --------- | ------- | ------ | ------ | ------ | ------- |
| 0         | −1.0000 | 2.0000 | 1.0000 | 1.0000 | 61.0000 |
| 1         | −1.4500 | 0.8700 | 0.9900 | 0.8900 | 6.5033  |
| 2         | −1.3331 | 1.1765 | 1.0185 | 0.9121 | 2.4974  |
| 3         | −1.3690 | 1.0956 | 1.0364 | 0.8987 | 2.1645  |

**Trend:** the cost falls at every update, so m and b move in a direction that reduces the error.

## Parts 4 coded gradient descent (kenia Umutoni)

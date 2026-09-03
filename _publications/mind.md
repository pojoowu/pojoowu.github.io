---
title: "MIND: Monge Inception Distance for Generative Models Evaluation"
collection: publications
category: manuscripts
permalink: /publication/mind
excerpt: ''
date: 2026-05-07
venue: 'arXiv preprint'
paperurl: '/files/2605.06797v1.pdf'
arxivurl: 'https://arxiv.org/abs/2605.06797'
posterurl: '/files/MIND_poster.pdf'
header:
  teaser: 'mind.jpeg'
authors: 'Quentin Berthet, Yu-Han Wu, Clément Crepy, Romuald Elie, Klaus Greff, Michael E. Sander'
summary: 'A sliced-Wasserstein alternative to FID: more sample-efficient, faster, and more robust.'
figure: /images/papers/mind.png
figure_caption: "Left: MIND during a diffusion model training run on ImageNet-64 (log scale), illustrating how MIND with 5k samples can replace FID with 50k, with a larger range. Right: correlation with the number of training steps, better for MIND with 1k or 5k samples than for FID with 50k."
highlights:
  - "**Problem.** FID needs tens of thousands of samples and can be fooled by matching moments."
  - "**Approach.** A sliced Wasserstein distance between Inception features, computed by sorting one-dimensional projections, with no high-dimensional means or covariances to estimate."
  - "**Result.** An order of magnitude more sample-efficient, two orders of magnitude faster, more robust; 5k samples match FID at 50k."
related:
  - optimal-stopping-ldm
bibtex: |
  @misc{berthet2026mind,
    title={{MIND}: Monge Inception Distance for Generative Models Evaluation},
    author={Berthet, Quentin and Wu, Yu-Han and Crepy, Cl{\'e}ment and Elie, Romuald and Greff, Klaus and Sander, Michael E.},
    year={2026},
    eprint={2605.06797},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
  }
citation: 'Quentin Berthet, Yu-Han Wu, Clément Crepy, Romuald Elie, Klaus Greff and Michael E. Sander (2026). MIND: Monge Inception Distance for Generative Models Evaluation. arXiv:2605.06797.'
---
### Abstract
We propose the Monge Inception Distance $\texttt{MIND}$, a metric for evaluating generative models that addresses key limitations of the widely adopted Fréchet Inception Distance (FID). $\texttt{MIND}$ metric leverages the sliced Wasserstein distance to compare distributions by averaging one-dimensional optimal transport distances, efficiently computed via sorting. This approach circumvents the estimation of high-dimensional means and covariance matrices, which underlie FID's poor sample complexity and vulnerability to adversarial attacks. We empirically demonstrate three primary advantages: (i) it is more sample-efficient by one order of magnitude, (ii) it is faster to compute by two orders of magnitude, (iii) it is more robust to adversarial attacks such as moment-matching. We show that $\texttt{MIND}$ with 5k samples can replace the evaluation performance of FID with 50k samples, providing high correlation with this standard benchmark and superior discriminative performance. We further demonstrate that even smaller sample sizes (e.g., 1k or 2k) remain highly informative for rapid model iteration.

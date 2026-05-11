---
title: "MIND: Monge Inception Distance for Generative Models Evaluation"
collection: publications
category: manuscripts
permalink: /publication/mind
excerpt: ''
date: 2026-05-07
venue: 'arXiv'
paperurl: 'http://pojoowu.github.io/files/2605.06797v1.pdf'
citation: 'Quentin Berther, Yu-Han Wu, Clément Crepy, Romuald Elie, Klaus Greff & Michael Eli Sander (2026). MIND: Monge Inception Distance for Generative Models Evaluation. arXiv:2605.06797.'
---
### Abstract
![mind](http://pojoowu.github.io/images/mind.jpeg)
We propose the Monge Inception Distance $\texttt{MIND}$, a metric for evaluating generative models that addresses key limitations of the widely adopted Fréchet Inception Distance (FID). $\texttt{MIND}$ metric leverages the sliced Wasserstein distance to compare distributions by averaging one-dimensional optimal transport distances, efficiently computed via sorting. This approach circumvents the estimation of high-dimensional means and covariance matrices, which underlie FID's poor sample complexity and vulnerability to adversarial attacks. We empirically demonstrate three primary advantages: (i) it is more sample-efficient by one order of magnitude, (ii) it is faster to compute by two orders of magnitude, (iii) it is more robust to adversarial attacks such as moment-matching. We show that $\texttt{MIND}$ with 5k samples can replace the evaluation performance of FID with 50k samples, providing high correlation with this standard benchmark and superior discriminative performance. We further demonstrate that even smaller sample sizes (e.g., 1k or 2k) remain highly informative for rapid model iteration.

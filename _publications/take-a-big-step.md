---
title: "Taking a Big Step: Large Learning Rates in Denoising Score Matching Prevent Memorization"
collection: publications
category: manuscripts
permalink: /publication/take-a-big-step
excerpt: ''
date: 2025-02-05
venue: 'arXiv:2502.03435'
paperurl: 'http://pojoowu.github.io/files/2502.03435v1.pdf'
citation: 'Wu, Y. H., Marion, P., Biau, G., & Boyer, C. (2025). Taking a Big Step: Large Learning Rates in Denoising Score Matching Prevent Memorization. arXiv preprint arXiv:2502.03435.'
---

Denoising score matching plays a pivotal role in the performance of diffusion-based generative models. However, the empirical optimal score–the exact solution to the denoising score matching–leads to memorization, where generated samples replicate the training data. Yet, in practice, only a moderate degree of memorization is observed, even without explicit regularization. In this paper, we investigate this phenomenon by uncovering an implicit regularization mechanism driven by large learning rates. Specifically, we show that in the small-noise regime, the empirical optimal score exhibits high irregularity. We then prove that, when trained by stochastic gradient descent with a large enough learning rate, neural networks cannot stably converge to a local minimum with arbitrarily small excess risk. Consequently, the learned score cannot be arbitrarily close to the empirical optimal score, thereby mitigating memorization. To make the analysis tractable, we consider one-dimensional data and two-layer neural networks. Experiments validate the crucial role of the learning rate in preventing memorization, even beyond the one-dimensional setting

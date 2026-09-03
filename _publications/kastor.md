---
title: "Kastor: An efficient fine-tuning strategy for generative emulation of PDE simulation"
collection: publications
category: manuscripts
permalink: /publication/kastor
excerpt: ''
date: 2026-08-05
venue: 'arXiv preprint'
paperurl: '/files/kastor.pdf'
arxivurl: 'https://arxiv.org/abs/2608.06107'
authors: 'Guillaume Couairon, Alexis Jacq, Yu-Han Wu, Renu Singh, Yana Hasson, Quentin Berthet, Romuald Elie'
summary: 'Fine-tunes a deterministic physics foundation model into a fast, accurate generative PDE emulator.'
selected: true
figure: /images/papers/kastor.png
figure_caption: "Average relative reduction of forecasting error (fCRPS skill score) between our models and the baseline fine-tuning methodology from Walrus (higher is better). Models trained with our methodology reduce forecasting error by 42.9% on average across datasets and physical variables."
highlights:
  - "**Problem.** Autoregressive ML emulators of PDEs accumulate error over long horizons and miss the stochasticity of physical systems."
  - "**Approach.** Adapt a deterministic physics foundation model into a generative surrogate with two-stage inference, mean-prediction regularization and spatial gradient matching."
  - "**Result.** 42.9% average reduction in forecasting error over the Walrus fine-tuning baseline on The Well, better on 8 of 10 datasets."
related:
  - diffusion-gemma
bibtex: |
  @misc{couairon2026kastor,
    title={Kastor: An efficient fine-tuning strategy for generative emulation of {PDE} simulations},
    author={Couairon, Guillaume and Jacq, Alexis and Wu, Yu-Han and Singh, Renu and Hasson, Yana and Berthet, Quentin and Elie, Romuald},
    year={2026},
    eprint={2608.06107},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
  }
citation: 'Guillaume Couairon, Alexis Jacq, Yu-Han Wu, Renu Singh, Yana Hasson, Quentin Berthet and Romuald Elie (2026) Kastor: An efficient fine-tuning strategy for generative emulation of PDE simulations. arXiv:2608.06107.'
---
### Abstract
Machine learning offers a promising avenue to accelerate physical simulations by replacing computationally expensive traditional Partial Differential Equation (PDE) solvers with fast, differentiable surrogate models. However, standard auto-regressive ML emulators often suffer from error accumulation over long horizons and struggle to capture the stochasticity of complex physical systems. In this paper, we propose Kastor, a comprehensive methodology to adapt a deterministic physics foundation model into a highly efficient and accurate generative surrogate. First, we introduce a two-stage inference scheme that combines a large-stride causal auto-regressive model with a non-causal temporal super-resolution network, significantly reducing error accumulation while minimizing computational cost. Second, we present Mean prediction regularization (MPR), a novel training objective that constrains the generative model to predict the deterministic distribution mean under null noise conditioning. This regularization dramatically improves the performance and stability of both Functional Generative Networks (FGN) and diffusion-based emulators. Finally, we demonstrate that incorporating spatial gradient matching improves the accuracy and physical fidelity of the simulations as measured by power spectrum density. Extensive evaluations on diverse simulation datasets of the benchmark The Well show that with these components, our model outperforms competing methods in forecasting accuracy, spectral consistency, and computational efficiency. Our model achieves a 42.9% average reduction in forecasting compared to our reference based on the Walrus finetuning methodology, and outperforms Walrus for 8 out of 10 datasets on variance-normalized RMSE (VRMSE).

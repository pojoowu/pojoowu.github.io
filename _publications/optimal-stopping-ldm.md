---
title: "Optimal Stopping in Latent Diffusion Model"
collection: publications
category: manuscripts
permalink: /publication/optimal-stopping-ldm
excerpt: ''
date: 2025-10-10
venue: 'ICML 2026'
badges:
  - 'Oral at the PriGM workshop, EurIPS 2025'
paperurl: '/files/2510.08409v1.pdf'
arxivurl: 'https://arxiv.org/abs/2510.08409'
slidesurl: '/files/PriGM2025_slides_optimal_stopping_LDM.pdf'
posterurl: '/files/poster_optimal_stopping_LDM.pdf'
authors: 'Yu-Han Wu, Quentin Berthet, Gérard Biau, Claire Boyer, Romuald Elie, Pierre Marion'
summary: 'Why the last denoising steps of a latent diffusion model can hurt, and when to stop.'
selected: true
figure: /images/papers/optimal-stopping-ldm.png
figure_caption: "Left: FID-30k of a latent diffusion model on CelebA-HQ, with latent shape 64 × 64 × 3. Right: FID-30k of a standard diffusion model trained in pixel space on CelebA64. The latent model gets worse over its last steps; the pixel-space model does not."
highlights:
  - "**Problem.** The last steps of latent diffusion can degrade samples, which does not happen in pixel-space diffusion."
  - "**Approach.** A Gaussian model with linear autoencoders that links latent dimension, the constraints of score matching and the stopping time."
  - "**Result.** Low-dimensional latents call for earlier stopping, high-dimensional ones for later; stopping time is a key hyperparameter of latent diffusion."
related:
  - mind
  - understanding-diffusion
bibtex: |
  @inproceedings{wu2026optimal,
    title={Optimal Stopping in Latent Diffusion Models},
    author={Wu, Yu-Han and Berthet, Quentin and Biau, G{\'e}rard and Boyer, Claire and Elie, Romuald and Marion, Pierre},
    booktitle={International Conference on Machine Learning ({ICML})},
    year={2026}
  }
citation: 'Yu-Han Wu, Quentin Berthet, Gérard Biau, Claire Boyer, Romuald Elie & Pierre Marion (2025). Optimal Stopping in Latent Diffusion Model. arXiv preprint arXiv:2510.08409.'
---
### Abstract
We identify and analyze a surprising phenomenon of Latent Diffusion Models (LDMs) where the final steps of the diffusion can degrade sample quality. In contrast to conventional arguments that justify early stopping for numerical stability, this phenomenon is intrinsic to the dimensionality reduction in LDMs. We provide a principled explanation by analyzing the interaction between latent dimension and stopping time. Under a Gaussian framework with linear autoencoders, we characterize the conditions under which early stopping is needed to minimize the distance between generated and target distributions. More precisely, we show that lower-dimensional representations benefit from earlier termination, whereas higher-dimensional latent spaces require later stopping time. We further establish that the latent dimension interplays with other hyperparameters of the problem such as constraints in the parameters of score matching. Experiments on synthetic and real datasets illustrate these properties, underlining that early stopping can improve generative quality. Together, our results offer a theoretical foundation for understanding how the latent dimension influences the sample quality, and highlight stopping time as a key hyperparameter in LDMs.

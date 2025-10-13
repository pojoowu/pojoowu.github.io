---
title: "Optimal Stopping in Latent Diffusion Model"
collection: publications
category: manuscripts
permalink: /publication/optimal-stopping-ldm
excerpt: ''
date: 2025-10-10
venue: 'arxiv'
paperurl: 'http://pojoowu.github.io/files/2309.01213v3.pdf'
citation: 'Yu-Han Wu, Quentin Berthet, Gérard Biau, Claire Boyer, Romuald Elie & Pierre Marion (2025). Optimal Stopping in Latent Diffusion Model. arXiv preprint arXiv:2510.08409.'
---

We identify and analyze a surprising phenomenon of Latent Diffusion Models (LDMs) where the final steps of the diffusion can degrade sample quality. In contrast to conventional arguments that justify early stopping for numerical stability, this phenomenon is intrinsic to the dimensionality reduction in LDMs. We provide a principled explanation by analyzing the interaction between latent dimension and stopping time. Under a Gaussian framework with linear autoencoders, we characterize the conditions under which early stopping is needed to minimize the distance between generated and target distributions. More precisely, we show that lower-dimensional representations benefit from earlier termination, whereas higher-dimensional latent spaces require later stopping time. We further establish that the latent dimension interplays with other hyperparameters of the problem such as constraints in the parameters of score matching. Experiments on synthetic and real datasets illustrate these properties, underlining that early stopping can improve generative quality. Together, our results offer a theoretical foundation for understanding how the latent dimension influences the sample quality, and highlight stopping time as a key hyperparameter in LDMs.

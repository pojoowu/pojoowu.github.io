---
title: "Understanding diffusion models requires rethinking (again) generalization"
collection: publications
category: manuscripts
permalink: /publication/understanding-diffusion
excerpt: ''
date: 2026-05-07
venue: 'arXiv preprint'
paperurl: '/files/Position_paper___memorization_diffusion_arXiv.pdf'
arxivurl: 'https://arxiv.org/abs/2605.06077'
header:
  teaser: 'understanding.png'
authors: 'Pierre Marion*, Yu-Han Wu* (* equal contribution)'
summary: 'Generalization in diffusion models needs new theory: what is learned before memorization?'
selected: true
figure: /images/papers/understanding-diffusion.png
figure_caption: "Predicted versus actual evolution of training metrics. Left: based on the literature, we expected the train and test loss to decrease together until the memorization time, at which point the model overfits, and distributional distances to track the loss. Right: actual experiment. The double descent in sliced Wasserstein distance and FID, present for both train and test, is unexpected."
highlights:
  - "**Problem.** In diffusion models memorization and generalization are incompatible, so the supervised-learning theory of generalization does not transfer."
  - "**Approach.** Survey the three families of explanations and run controlled CIFAR-10 sweeps over dataset size, model size, batch size and learning rate."
  - "**Position.** Why models do not memorize is largely settled by early stopping and the linear scaling of memorization time; what is learned before memorization is the open question."
blogurl: /blog/rethinking-generalization-in-diffusion-models/
related:
  - take-a-big-step
  - optimal-stopping-ldm
bibtex: |
  @misc{marion2026understanding,
    title={Understanding diffusion models requires rethinking (again) generalization},
    author={Marion, Pierre and Wu, Yu-Han},
    year={2026},
    eprint={2605.06077},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
  }
citation: 'Pierre Marion and Yu-Han Wu (2026) Understanding diffusion models requires rethinking (again) generalization. arXiv:2605.06077.'
---
### Abstract
This position paper argues that understanding generalization in diffusion models requires fundamentally new theoretical frameworks that go beyond both classical statistical learning theory and the benign overfitting paradigm developed for supervised learning. In diffusion models, unlike in supervised learning, memorization of training data and generalization to novel samples are incompatible: a model that has fully memorized its training set generates copies rather than novel data. Several theoretical explanations for why practical diffusion models nevertheless generalize have been proposed, based on capacity limitations, implicit regularization from optimization, or architectural inductive biases, but their interactions remain unclear. We argue that the field should pivot from explaining why the diffusion models do not memorize to investigating what the model actually learns during pre-memorization phase. To highlight our stance, we conduct empirical study of diffusion models trained on CIFAR-10, and we distill the findings into concrete open questions that we believe are key to improve understanding of generalization in diffusion models.

---
title: "Understanding diffusion models requires rethinking (again) generalization"
collection: publications
category: manuscripts
permalink: /publication/understanding-diffusion
excerpt: ''
date: 2026-05-07
venue: 'arXiv'
paperurl: 'http://pojoowu.github.io/files/2309.01213v3.pdf'
citation: 'Pierre Marion and Yu-Han Wu (2026) Understanding diffusion models requires rethinking (again) generalization arXiv:'
---
### Abstract
This position paper argues that understanding generalization in diffusion models requires fundamentally new theoretical frameworks that go beyond both classical statistical learning theory and the benign overfitting paradigm developed for supervised learning. In diffusion models, unlike in supervised learning, memorization of training data and generalization to novel samples are incompatible: a model that has fully memorized its training set generates copies rather than novel data. Several theoretical explanations for why practical diffusion models nevertheless generalize have been proposed, based on capacity limitations, implicit regularization from optimization, or architectural inductive biases, but their interactions remain unclear. We argue that the field should pivot from explaining why the diffusion models do not memorize to investigating what the model actually learns during pre-memorization phase. To highlight our stance, we conduct empirical study of diffusion models trained on CIFAR-10, and we distill the findings into concrete open questions that we believe are key to improve understanding of generalization in diffusion models.

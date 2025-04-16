---
title: "Implicit regularization of deep residual networks towards neural ODEs"
collection: publications
category: manuscripts
permalink: /publication/implicit-reg-resnet
excerpt: ''
date: 2023-01-01
venue: 'ICLR2024'
paperurl: 'http://pojoowu.github.io/files/2208.13513v2.pdf'
citation: 'Marion, P., Wu, Y. H., Sander, M. E., & Biau, G. (2023). Implicit regularization of deep residual networks towards neural ODEs. arXiv preprint arXiv:2309.01213.'
---

Residual neural networks are state-of-the-art deep learning models. Their continuous-depth analog, neural ordinary differential equations (ODEs), are also widely used. Despite their success, the link between the discrete and continuous models still lacks a solid mathematical foundation. In this article, we take a step in this direction by establishing an implicit regularization of deep residual networks towards neural ODEs, for nonlinear networks trained with gradient flow. We prove that if the network is initialized as a discretization of a neural ODE, then such a discretization holds throughout training. Our results are valid for a finite training time, and also as the training time tends to infinity provided that the network satisfies a Polyak-Łojasiewicz condition. Importantly, this condition holds for a family of residual networks where the residuals are two-layer perceptrons with an overparameterization in width that is only linear, and implies the convergence of gradient flow to a global minimum. Numerical experiments illustrate our results.

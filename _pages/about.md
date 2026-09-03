---
permalink: /
title: "About"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

I am a PhD student at [LPSM](https://www.lpsm.paris/), [Sorbonne University](https://www.sorbonne-universite.fr/), and [Google DeepMind](https://deepmind.google/), working on **diffusion models** and **machine learning theory**.

<dl class="facts">
  <dt>Advisors</dt>
  <dd><a href="https://perso.lpsm.paris/~biau/">Gérard Biau</a>, <a href="https://www.imo.universite-paris-saclay.fr/~claire.boyer/">Claire Boyer</a> and <a href="https://pierremarion23.github.io/">Pierre Marion</a></dd>
  <dt>At Google DeepMind</dt>
  <dd><a href="https://q-berthet.github.io/">Quentin Berthet</a> and <a href="https://www.linkedin.com/in/romuald-elie-b9bb817b/">Romuald Elie</a></dd>
</dl>

<div class="chips" aria-label="Research interests">
  <span class="chips__label">Research interests</span>
  <span class="chip">Diffusion models</span>
  <span class="chip">Regularization</span>
  <span class="chip">ML for science</span>
</div>

## Research focus

<div class="focus-grid">
  <article class="focus-card">
    <div class="focus-card__icon"><i class="fas fa-wave-square" aria-hidden="true"></i></div>
    <h3 class="focus-card__title">Generalization in diffusion models</h3>
    <p class="focus-card__text">Why diffusion models produce novel samples rather than copies of their training data, and how optimization shapes this.</p>
    <p class="focus-card__links"><a href="/publication/take-a-big-step">Taking a Big Step</a> · <a href="/publication/understanding-diffusion">Rethinking generalization</a></p>
  </article>
  <article class="focus-card">
    <div class="focus-card__icon"><i class="fas fa-sliders" aria-hidden="true"></i></div>
    <h3 class="focus-card__title">Sampling and evaluation</h3>
    <p class="focus-card__text">When to stop the reverse process in latent diffusion models, and how to measure sample quality reliably.</p>
    <p class="focus-card__links"><a href="/publication/optimal-stopping-ldm">Optimal Stopping</a> · <a href="/publication/mind">MIND</a></p>
  </article>
  <article class="focus-card">
    <div class="focus-card__icon"><i class="fas fa-flask" aria-hidden="true"></i></div>
    <h3 class="focus-card__title">Generative models for science and language</h3>
    <p class="focus-card__text">Generative emulators for PDE simulations, and discrete-diffusion language models.</p>
    <p class="focus-card__links"><a href="/publication/kastor">Kastor</a> · <a href="/publication/diffusion-gemma">DiffusionGemma</a></p>
  </article>
  <article class="focus-card">
    <div class="focus-card__icon"><i class="fas fa-bezier-curve" aria-hidden="true"></i></div>
    <h3 class="focus-card__title">Implicit regularization in deep learning</h3>
    <p class="focus-card__text">How gradient descent biases deep residual networks toward neural ODEs.</p>
    <p class="focus-card__links"><a href="/publication/implicit-reg-resnet">ResNets and neural ODEs</a></p>
  </article>
</div>

## Selected publications

{% for post in site.publications reversed %}{% if post.selected %}{% include publication-item.html compact=true %}{% endif %}{% endfor %}

<p class="more"><a href="/publications/">All publications</a></p>

## News

{% include news-list.html limit=5 %}

<p class="more"><a href="/news/">All news</a></p>

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
  <a class="chip" href="/publications/#topics=diffusion">Diffusion models</a>
  <a class="chip" href="/publications/#topics=regularization">Regularization</a>
  <a class="chip" href="/publications/#topics=applications">ML for science</a>
</div>

## Research focus

{% comment %}
  Each card links to the publications page with the combination of topic
  filters that best matches it (filters intersect; ids in _data/topics.yml).
  The "All N papers" counts are computed from the papers' `topics` with the
  same combinations, so they stay in step with the filtered page.
{% endcomment %}
{% assign n_gen = 0 %}{% assign n_samp = 0 %}{% assign n_app = 0 %}{% assign n_reg = 0 %}
{% for p in site.publications %}
  {% if p.topics contains 'diffusion' and p.topics contains 'theory' %}{% assign n_gen = n_gen | plus: 1 %}{% endif %}
  {% if p.topics contains 'diffusion' and p.topics contains 'sampling' %}{% assign n_samp = n_samp | plus: 1 %}{% endif %}
  {% if p.topics contains 'diffusion' and p.topics contains 'applications' %}{% assign n_app = n_app | plus: 1 %}{% endif %}
  {% if p.topics contains 'regularization' %}{% assign n_reg = n_reg | plus: 1 %}{% endif %}
{% endfor %}

<div class="focus-grid">
  <article class="focus-card">
    <div class="focus-card__icon"><i class="fas fa-wave-square" aria-hidden="true"></i></div>
    <h3 class="focus-card__title"><a href="/publications/#topics=diffusion,theory">Generalization in diffusion models</a></h3>
    <p class="focus-card__text">Why diffusion models produce novel samples rather than copies of their training data, and how optimization shapes this.</p>
    <p class="focus-card__links"><a href="/publication/take-a-big-step">Taking a Big Step</a> · <a href="/publication/understanding-diffusion">Rethinking generalization</a></p>
    <a class="focus-card__more" href="/publications/#topics=diffusion,theory">All {{ n_gen }} papers <i class="fas fa-arrow-right-long" aria-hidden="true"></i></a>
  </article>
  <article class="focus-card">
    <div class="focus-card__icon"><i class="fas fa-sliders" aria-hidden="true"></i></div>
    <h3 class="focus-card__title"><a href="/publications/#topics=diffusion,sampling">Sampling and evaluation</a></h3>
    <p class="focus-card__text">When to stop the reverse process in latent diffusion models, and how to measure sample quality reliably.</p>
    <p class="focus-card__links"><a href="/publication/optimal-stopping-ldm">Optimal Stopping</a> · <a href="/publication/mind">MIND</a></p>
    <a class="focus-card__more" href="/publications/#topics=diffusion,sampling">All {{ n_samp }} papers <i class="fas fa-arrow-right-long" aria-hidden="true"></i></a>
  </article>
  <article class="focus-card">
    <div class="focus-card__icon"><i class="fas fa-flask" aria-hidden="true"></i></div>
    <h3 class="focus-card__title"><a href="/publications/#topics=diffusion,applications">Generative models for science and language</a></h3>
    <p class="focus-card__text">Generative emulators for PDE simulations, and discrete-diffusion language models.</p>
    <p class="focus-card__links"><a href="/publication/kastor">Kastor</a> · <a href="/publication/diffusion-gemma">DiffusionGemma</a></p>
    <a class="focus-card__more" href="/publications/#topics=diffusion,applications">All {{ n_app }} papers <i class="fas fa-arrow-right-long" aria-hidden="true"></i></a>
  </article>
  <article class="focus-card">
    <div class="focus-card__icon"><i class="fas fa-bezier-curve" aria-hidden="true"></i></div>
    <h3 class="focus-card__title"><a href="/publications/#topics=regularization">Implicit regularization in deep learning</a></h3>
    <p class="focus-card__text">How gradient descent biases deep residual networks toward neural ODEs, and how large learning rates regularize score matching.</p>
    <p class="focus-card__links"><a href="/publication/implicit-reg-resnet">ResNets and neural ODEs</a> · <a href="/publication/take-a-big-step">Taking a Big Step</a></p>
    <a class="focus-card__more" href="/publications/#topics=regularization">All {{ n_reg }} papers <i class="fas fa-arrow-right-long" aria-hidden="true"></i></a>
  </article>
</div>

## Selected publications

{% for post in site.publications reversed %}{% if post.selected %}{% include publication-item.html compact=true %}{% endif %}{% endfor %}

<p class="more"><a href="/publications/">All publications</a></p>

## News

{% include news-list.html limit=5 %}

<p class="more"><a href="/news/">All news</a></p>

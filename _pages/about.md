---
permalink: /
title: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Hi, I am Yu-Han (吳雨翰). I have been a PhD student in [LPSM](https://www.lpsm.paris/) at [Sorbonne University](https://www.sorbonne-universite.fr/) since September 2024, supervised by [Gérard Biau](https://perso.lpsm.paris/~biau/), [Claire Boyer](https://www.imo.universite-paris-saclay.fr/~claire.boyer/) and [Pierre Marion](https://pierremarion23.github.io/). I am also part of the co-advised PhD student program at Google DeepMind, co-advised by Quentin Berthet and Romuald Elie.

<div class="chips" aria-label="Research interests">
  <span class="chips__label">Research interests</span>
  <span class="chip">Diffusion models</span>
  <span class="chip">Regularization</span>
  <span class="chip">ML for science</span>
</div>

## News

{% include news-list.html limit=5 %}

<p class="more"><a href="/news/">All news</a></p>

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

## Brief curriculum vitae

<ul class="timeline">
  <li><span class="timeline__date">2024 –</span> Sorbonne University and Google DeepMind, co-advised PhD student</li>
  <li><span class="timeline__date">2020 – 2024</span> Ecole Normale Supérieure</li>
  <li><span class="timeline__date">2022 – 2023</span> University Paris-Saclay, Master degree (Mathematics of Randomness)</li>
  <li><span class="timeline__date">2018 – 2020</span> Lycée Louis-le-Grand, preparatory classes</li>
</ul>

## Internships

<ul class="timeline">
  <li><span class="timeline__date">2024</span> Sorbonne University, Research Internship</li>
  <li><span class="timeline__date">2023</span> Owkin, Research Internship</li>
  <li><span class="timeline__date">2023</span> Sorbonne University, Research Internship</li>
  <li><span class="timeline__date">2022</span> Caltech, Research Internship</li>
</ul>

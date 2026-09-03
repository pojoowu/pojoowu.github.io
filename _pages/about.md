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

<ul class="focus">
  <li><span class="focus__topic">Memorization and generalization in diffusion models</span>
      <span class="focus__links"><a href="/publication/take-a-big-step">Taking a Big Step</a> · <a href="/publication/understanding-diffusion">Rethinking generalization</a></span></li>
  <li><span class="focus__topic">Sampling in latent diffusion models</span>
      <span class="focus__links"><a href="/publication/optimal-stopping-ldm">Optimal Stopping</a></span></li>
  <li><span class="focus__topic">Evaluating generative models</span>
      <span class="focus__links"><a href="/publication/mind">MIND</a></span></li>
  <li><span class="focus__topic">Generative models for science and language</span>
      <span class="focus__links"><a href="/publication/kastor">Kastor</a> · <a href="/publication/diffusion-gemma">DiffusionGemma</a></span></li>
  <li><span class="focus__topic">Implicit regularization in deep learning</span>
      <span class="focus__links"><a href="/publication/implicit-reg-resnet">ResNets and neural ODEs</a></span></li>
</ul>

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

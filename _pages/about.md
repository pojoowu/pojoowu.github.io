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

## Research focus

{% comment %} Cards come from _data/focus.yml; papers, counts and filter links are derived from the papers' topics. {% endcomment %}
{% include focus-cards.html %}

## Selected publications

{% for post in site.publications reversed %}{% if post.selected %}{% include publication-item.html compact=true %}{% endif %}{% endfor %}

<p class="more"><a href="/publications/">All publications</a></p>

## News

{% include news-list.html limit=5 %}

<p class="more"><a href="/news/">All news</a></p>

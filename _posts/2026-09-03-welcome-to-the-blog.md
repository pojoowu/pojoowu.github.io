---
title: "Welcome to the blog"
date: 2026-09-03
categories:
  - blog
tags:
  - meta
excerpt: "A place for longer notes on diffusion models, regularization and machine learning for science, alongside the papers and talks elsewhere on this site."
---

This blog is where I will put notes that do not fit in a paper: longer explanations of ideas from my research on diffusion models, regularization and machine learning for science, reading notes, and the occasional write-up of a talk.

Posts support mathematics. A denoising objective can be written inline as $$\mathbb{E}\,\lVert s_\theta(x_t, t) - \nabla_{x_t} \log p_t(x_t)\rVert^2$$ or displayed:

$$
\mathrm{d}x_t = -\tfrac{1}{2}\beta(t)\,x_t\,\mathrm{d}t + \sqrt{\beta(t)}\,\mathrm{d}W_t .
$$

They also support code:

```python
def denoise(x_t, t, model):
    return x_t + (1 - alpha(t)) * model(x_t, t)
```

New posts appear here and in the [RSS feed](/feed.xml).

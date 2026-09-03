---
title: "DiffusionGemma"
collection: publications
category: manuscripts
permalink: /publication/diffusion-gemma
excerpt: ''
date: 2026-07-31
venue: 'arXiv preprint'
paperurl: '/files/diffusiongemma.pdf'
arxivurl: 'https://arxiv.org/abs/2608.00146'
authors: 'DiffusionGemma Team, Google DeepMind'
summary: 'An open-weight discrete-diffusion language model fine-tuned from Gemma 4.'
figure: /images/papers/diffusion-gemma.png
figure_caption: "Pareto plot of quality versus output decoding speed comparing DiffusionGemma to the Gemma 4 model family and other diffusion models. Quality and output speed are calculated as the average across GPQA-Diamond and LiveCodeBench-v6 for all models."
highlights:
  - "**Problem.** Autoregressive LLMs decode one token at a time, a sequential bottleneck for generation speed."
  - "**Approach.** Fine-tune Gemma 4 into a block-diffusion model that refines 256 tokens in parallel: supervised denoising, then reinforcement learning with sampler distillation, using under 10% of the base model's training tokens."
  - "**Result.** About 1,500 output tokens per second on a single H100, a new speed-capability Pareto frontier, while keeping thinking mode, multimodal inputs and long context."
related:
  - kastor
bibtex: |
  @misc{diffusiongemma2026,
    title={{DiffusionGemma} Technical Report},
    author={{DiffusionGemma Team}},
    year={2026},
    eprint={2608.00146},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
  }
citation: 'DiffusionGemma Team (2026). DiffusionGemma Technical Report. arXiv:2608.00146.'
---
### Abstract
We introduce DiffusionGemma, an experimental open-weight language model that uses discrete diffusion to generate text at exceptionally high speed. Rather than decoding one token at a time, DiffusionGemma iteratively refines blocks of 256 tokens in parallel, avoiding the sequential decoding bottleneck of conventional autoregressive (AR) large language models. Instead of training from scratch, we obtain DiffusionGemma by fine-tuning the mixture-of-experts Gemma 4 model with 3.8B activated and 25.2B total parameters. Our compute-efficient two-stage training pipeline uses fewer than 10% of the starting AR model’s total training token budget. The first stage uses supervised fine-tuning to teach bidirectional denoising, while the second stage combines reinforcement learning with sampler distillation to jointly improve generation quality and inference efficiency. DiffusionGemma establishes a new Pareto frontier for the trade-off between generation speed and model capability. Averaged across our full evaluation suite, it generates around 20 tokens per forward pass and achieves roughly 1,500 output tokens per second on a single NVIDIA H100 GPU, which is substantially faster than AR models even with state-ofthe-art speculative decoding. DiffusionGemma also retains the starting model’s support for thinking mode, multimodal inputs, and long contexts. Despite diffusion fine-tuning, it remains capable of AR generation with only minor performance degradation, suggesting a path toward hybrid diffusion-AR decoding.

---
title: "Understanding diffusion models requires rethinking (again) generalization"
date: 2026-09-03
categories:
  - blog
tags:
  - diffusion models
  - generalization
  - memorization
excerpt: "We argue that the field should pivot from explaining why the diffusion models do not memorize to investigating what the model actually learns during pre-memorization phase."
header:
  teaser: understanding.png
---

<p class="post-note">A condensed version of our position paper with Pierre Marion. The text below is taken from the paper and shortened; the figures are the paper's. References and full details are in the paper.</p>

<p class="pub__actions">
  <a class="pub__pill" href="/files/Position_paper___memorization_diffusion_arXiv.pdf"><i class="fas fa-file-lines" aria-hidden="true"></i>Paper</a>
  <a class="pub__pill" href="https://arxiv.org/abs/2605.06077"><i class="ai ai-arxiv" aria-hidden="true"></i>arXiv</a>
  <a class="pub__pill pub__pill--ghost" href="/publication/understanding-diffusion">Publication page</a>
</p>

## Why generative models are different

The situation in generative models, and in particular diffusion models, is fundamentally different. Diffusion models are trained by denoising score matching, in which the empirical risk is an expectation over Gaussian noise added to each training sample. Because this noise is continuous, the training loss cannot be driven to zero; instead, the global minimum of the empirical score matching loss corresponds to the score function of the noised empirical measure, i.e., a mixture of Gaussians centered at the training points. Sampling from it produces near-exact copies of the training data. In other words, unlike in supervised learning where interpolation and generalization can coexist, reaching the global minimum of the empirical risk in denoising score matching is fundamentally detrimental. Yet practical diffusion models clearly generate diverse, novel samples, implying that some form of regularization prevents full memorization.

Several concurrent theoretical explanations have been proposed for this regularization, falling broadly into three families: (i) capacity limitations of the network architecture relative to the dataset size, (ii) implicit regularization from the optimization dynamics, and (iii) inductive biases of the architecture. Each captures an important facet of the phenomenon, but their interactions remain poorly understood.

We use *novelty* to refer to the model's ability to produce samples that are not copies of training data (i.e., the absence of memorization), and *fidelity* to refer to the quality and distributional accuracy of the generated samples with respect to the true data distribution. A model that generates pure noise has perfect novelty but zero fidelity; a model that copies training examples has high fidelity but no novelty. What we informally call generalization in diffusion models is the simultaneous achievement of both novelty and fidelity.

## Position

<blockquote class="callout">
We argue that understanding generalization in diffusion models requires going beyond both classical statistical learning theory and the benign overfitting paradigm that reshaped our understanding of supervised learning. We contend that the question of why diffusion models do not memorize in large-scale applications is largely resolved: early stopping, combined with the linear scaling of memorization time with dataset size. The deeper and most pressing question in the theoretical analysis of diffusion models is what is actually learned during the pre-memorization phase, and how novelty and fidelity jointly emerge from the interplay between optimization, architecture, and data geometry.
</blockquote>

## Empirical study of the memorization transition

We perform empirical studies on CIFAR-10 with U-Net architectures to support our proposed view. We conduct careful hyperparameter sweeps over dataset size, model size, batch size, and learning rate while tracking multiple metrics throughout training. This intermediate-scale study is positioned between the Gaussian data of theoretical analyses and the large-scale experiments of practical systems.

<figure class="post-figure">
  <img src="/images/blog/rethinking-generalization/fig6.png" alt="Generated samples at different training stages and dataset sizes" loading="lazy">
  <figcaption><strong>Figure 6:</strong> Generated samples at different training stages and dataset sizes, with the same randomness for each row. (a) During the generalization phase with $N = 2048$, the model produces diverse images, though quality is limited by the small dataset. (b) After memorization with $N = 2048$, the model generates near-copies of training data. (c) During the generalization phase with $N = 16{,}384$, the model produces more diverse, higher-quality samples, illustrating the benefit of larger training sets.</figcaption>
</figure>

We track the following quantities during training, computed on train and test splits: (i) denoising score matching loss; (ii) memorization score: the ratio of generated samples with maximum cosine similarity to the training data exceeding 0.6 in a self-supervised feature space; (iii) sliced Wasserstein distance between 2,000 generated samples and the reference split (train or test) in the Inception feature spaces; (iv) FID.

For each configuration, we examine: (i) the memorization time $\tau_{\mathrm{mem}}$. This is defined as the time when the test loss begins diverging from the training loss, which is known to be associated with the onset of memorization. We stress that $\tau < \tau_{\mathrm{mem}}$ implies novelty (generated samples are not copies of training data) but does not automatically imply high fidelity; (ii) the memorization rate, i.e., the slope of the memorization score once in the memorization phase; and (iii) the best fidelity achieved during training, measured by the minimum sliced Wasserstein distance attained before memorization takes hold.

## Predictions versus reality: unexpected phenomena

<figure class="post-figure">
  <img src="/images/blog/rethinking-generalization/fig1.png" alt="Predicted versus actual evolution of training metrics" loading="lazy">
  <figcaption><strong>Figure 1:</strong> Predicted versus actual evolution of training metrics. <strong>Left:</strong> based on the literature, we expected the train and test loss to decrease together until $\tau_{\mathrm{mem}}$, at which point the model overfits, and distributional distances to track the loss. <strong>Right:</strong> actual experiment ($N = 2048$, $P = 92\mathrm{M}$, $B = 16$, $\eta = 10^{-4}$). The double descent in sliced Wasserstein distance and FID (bottom), present for both train and test, is unexpected.</figcaption>
</figure>

We had predicted the behavior sketched in Figure 1a: the train and test losses would decrease together until $\tau_{\mathrm{mem}}$, at which point the model would begin overfitting and the memorization score would rise. Distances in distribution space (sliced Wasserstein, FID) would follow a similar trend to the loss, decreasing during the generalization phase and increasing once memorization begins. The actual experiment (Figure 1b) reveals two striking deviations from this prediction.

**The train-test gap is uninformative about generative behavior.** Throughout training, we observe little to no difference between the train and test distributional distances (sliced Wasserstein, FID). Since the train and test splits are both drawn from the same distribution and are themselves close in distribution space, the triangle inequality implies that the distributional distance from generated samples to either split should be nearly identical. The important implication is that none of the standard metrics we tracked correctly disentangles novelty from fidelity: distributional distances behave identically whether evaluated against the training or test set, even as the model transitions from producing novel images to producing copies. This suggests that the classical supervised-learning notion of generalization, measured by a train-test performance gap either in score or distribution space, is insufficient for understanding generative model quality.

**Double descent in distributional distance, for both train and test.** Most unexpectedly, we observe a double descent in distribution space (bottom panels of Figure 1b). Crucially, this double descent occurs for distances measured against both the training and the test sets, ruling out explanations in terms of classical double descent or benign overfitting, which would manifest as a divergence between train and test metrics. Instead, this phenomenon appears driven purely by optimization dynamics: during an intermediate phase, the model reaches a state where it has low training loss yet generates a distribution that is far from the target. The mechanism underlying this double descent is thus an open question.

## The roles of dataset size and model size

For clearer visualization across different settings, we plot metrics against the normalized training step

$$
T = \tau \cdot \frac{N_{\min}}{N} \cdot \frac{B}{B_{\min}} \cdot \frac{\eta}{\eta_{\min}},
$$

where $N_{\min} = 2048$, $B_{\min} = 16$, and $\eta_{\min} = 10^{-5}$ are the smallest values in each sweep. This rescaling accounts for the fact that larger datasets require more training steps, while larger batch sizes and learning rates process more information per step.

<figure class="post-figure">
  <img src="/images/blog/rethinking-generalization/fig2.png" alt="Effect of dataset size on training metrics" loading="lazy">
  <figcaption><strong>Figure 2:</strong> Effect of dataset size on training metrics (normalized step). Larger datasets delay memorization onset, reduce memorization rate, and improve peak fidelity.</figcaption>
</figure>

**Effect of dataset size (Figure 2).** When increasing the dataset size, we observe three effects. First, the normalized curves collapse before memorization, confirming that training time to memorization grows proportionally to the number of training samples. Second, the memorization rate (slope of the memorization score in the memorization phase) diminishes with larger $N$, which is intuitive: it is harder to memorize a larger dataset. Third, larger datasets lead to better fidelity, as measured by the minimum sliced Wasserstein distance achieved during training.

<figure class="post-figure">
  <img src="/images/blog/rethinking-generalization/fig3.png" alt="Effect of model size on training metrics" loading="lazy">
  <figcaption><strong>Figure 3:</strong> Effect of model size on training metrics. Larger models exhibit faster memorization onset, and peak fidelity is improved by increased capacity.</figcaption>
</figure>

**Effect of model size (Figure 3).** When increasing the model size, we observe two effects: larger models begin memorizing sooner, which is reasonably intuitive by analogy with dataset size, and there is an improvement in peak fidelity for larger models, both for train and test splits.

We highlight that the two sweeps play slightly different roles. Increasing the dataset size delays memorization and improve fidelity, whereas increasing the model size accelerates memorization while also improving fidelity. This suggests that the classical statistical perspective, where generalization is governed by some ratio of model capacity to sample size, is insufficient to explain the phenomena observed here. The model's trajectory through parameter space, shaped by optimization dynamics, appears to play a role that cannot be reduced to a simple capacity argument.

## Optimization hyperparameters shape fidelity

<figure class="post-figure">
  <img src="/images/blog/rethinking-generalization/fig4.png" alt="Effect of batch size on training metrics" loading="lazy">
  <figcaption><strong>Figure 4:</strong> Effect of batch size on training metrics (normalized step). Smaller batch sizes improve peak fidelity while leaving the memorization onset and rate largely unchanged.</figcaption>
</figure>

**Effect of batch size (Figure 4).** When increasing the batch size, we observe three effects. First, the raw memorization onset time scales inversely with batch size, meaning that the normalized curves collapse. Second, the memorization rate is essentially unaffected by batch size. This is somewhat surprising, as one might expect that smaller batch sizes, which introduce more stochasticity, would slow down memorization. Third, smaller batch sizes achieve better peak fidelity. This resonates with the minimum stability literature, where smaller batches are known to bias SGD toward flatter minima. However, the improved fidelity here manifests during training and not at convergence, a regime that is not directly addressed by the minimum stability framework.

<figure class="post-figure">
  <img src="/images/blog/rethinking-generalization/fig5.png" alt="Effect of learning rate on training metrics" loading="lazy">
  <figcaption><strong>Figure 5:</strong> Effect of learning rate on training metrics (normalized step). Larger learning rates delay the normalized memorization onset and improve peak fidelity.</figcaption>
</figure>

**Effect of learning rate (Figure 5).** When increasing the learning rate, we observe two notable effects. First, the normalized training time increases with larger learning rates. This is consistent with the edge-of-stability phenomenon: beyond a certain learning rate, increasing $\eta$ no longer proportionally accelerates training. Second, larger learning rates lead to better peak fidelity. Again, however, this improvement manifests along the training trajectory rather than at convergence, suggesting that the implicit regularization from the learning rate operates differently from what the minimum stability framework predicts.

## What is known

1. **The memorization transition is observable and systematic.** By carefully calibrating the dataset size, we can reliably observe the transition from a novelty phase to a memorization phase. This transition is gradual, with a well-defined onset $\tau_{\mathrm{mem}}$ and a monotonically increasing memorization score thereafter.
2. **Memorization onset scales linearly with dataset size.** This explains why memorization is rarely observed in practical large-scale training: the required training time simply exceeds any reasonable budget. In our view, this largely resolves the question of why practical diffusion models do not memorize. The community should shift its focus from explaining the absence of memorization to understanding what the model learns during the pre-memorization phase and how fidelity emerges.
3. **Model size and dataset size play different roles in the training dynamics.** The fidelity is improved both by increasing the dataset size and model size. On the contrary, memorization is delayed by increasing the dataset size but fastened by increasing the model size.
4. **Optimization hyperparameters improve fidelity before the memorization transition.** Both smaller batch sizes and larger learning rates lead to better peak fidelity, as measured by the minimum distributional distance achieved before memorization. These effects echo predictions from the minimum stability literature but manifest along the training trajectory rather than at convergence.

## Open questions

1. **What metrics adequately capture novelty, fidelity, and their interaction?** Standard distributional metrics (FID, sliced Wasserstein) fail to distinguish between a model that generalizes and one that memorizes, since both are evaluated against reference sets that are close in distribution space. A fundamental challenge is to develop metrics that are sensitive to copy-vs-generalize distinction, robust to the curse of dimensionality in image space, and ideally with known relationships to classical statistical divergences.
2. **How does implicit regularization operate along the training trajectory?** The minimum stability framework characterizes the solution at convergence, but our findings suggest that the key regularization effects of learning rate and batch size manifest along the trajectory of optimization. This calls for a new theory of implicit regularization that describes the properties of intermediate iterates of SGD applied to the score matching objective.
3. **How does the geometry of the data distribution shape generalization?** Understanding how properties of the data distribution, in particular its manifold structure and regularity, interact with the optimization dynamics and architecture to shape generalization is central to connecting theory and practice.

Beyond diffusion models, the theory of generalization in deep generative models requires a fundamentally different conceptual framework from the one that has been so successful for supervised learning. In supervised learning, the training loss is a direct proxy for the quantity of interest (prediction accuracy), and the generalization gap is the natural object of study. In generative modeling, the training loss (score matching) is at best an indirect proxy for sample quality, and the classical generalization gap, both in loss space and distribution space, carries little information about the model's generative behavior.

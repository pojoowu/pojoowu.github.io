---
title: "Designing enzymes for new-to-nature chemistry and non-natural substrates with AlphaProtein Novo"
collection: publications
category: manuscripts
permalink: /publication/alphaprotein-novo
excerpt: ''
date: 2026-10-05
venue: 'bioRxiv preprint'
topics: [diffusion, applications]
short: AlphaProtein Novo
paperurl: '/files/alphaprotein-novo.pdf'
biorxivurl: 'https://www.biorxiv.org/content/10.64898/2026.10.01.756017v1'
codeurl: 'https://github.com/google-deepmind/alphaprotein-novo'
authors: 'Zachary Wu*, Josh Abramson*, Thomas Frerix*, Alexander E. Chu*, Ruijie K. Zhang*, Luca Schulz*, Amy E. Danson*, Tristan O. C. Kwan*, Li Kevin Wenliang*, Jacob Kelly*, Zi-Qi Li, Rosalia G. Schneider, Ashok Thillaisundaram, Harshnira Patani, Vinicius F. Zambaldi, Sukhdeep Singh, David La, Masy Domecillo, Ariane N. Mora, Julia C. Reisenbauer, Yu Zhang, Eliseo Papa, Akvilė Žemgulytė, Yu-Han Wu, Augustin Žídek, Jiaxin Shi, Grace Margand, Naila Assem, Kate Stephen, Charlie Emrich, Peng Liu, Lucy Colwell, Demis Hassabis, Rob Fergus, Frances H. Arnold, Pushmeet Kohli, Jue Wang (* equal contribution)'
summary: 'A generative diffusion and structure-prediction pipeline for de novo enzyme design on challenging reactions.'
figure: /images/papers/alphaprotein-novo.png
figure_caption: "Using AlphaProtein Novo to design enzymes for new-to-nature reactions. (A) Schematic of the design pipeline. (B–D) Regioselective nitrene transferases for piperidine synthesis: reaction scheme, structure of GDM_NT_121, and hit rates versus natural diversity screening. (E–H) Serine esterases for DEHP hydrolysis: reaction scheme, structure of GDM_DEHP_376, hit rates across design rounds, and activity across temperatures and acetonitrile concentrations."
highlights:
  - "**Problem.** Traditional enzyme engineering relies on natural starting points that are hard to find for new-to-nature reactions and non-natural substrates."
  - "**Approach.** AlphaProtein Novo (AP Novo) co-generates protein backbones and sequences around catalytic motifs via diffusion, then filters candidates with mechanism-inspired AlphaFold 3 metrics and sequence-ensemble scoring."
  - "**Result.** Outperforms natural sequence screening on regioselective piperidine synthesis (99:1 r.r., 94% e.e.) and DEHP plasticizer degradation (active at 90 °C and in 75% acetonitrile), with state-of-the-art de novo efficiency on model reactions."
related:
  - kastor
  - diffusion-gemma
bibtex: |
  @article{wu2026alphaprotein,
    title={Designing enzymes for new-to-nature chemistry and non-natural substrates with {AlphaProtein Novo}},
    author={Wu, Zachary and Abramson, Josh and Frerix, Thomas and Chu, Alexander E. and Zhang, Ruijie K. and Schulz, Luca and Danson, Amy E. and Kwan, Tristan O. C. and Wenliang, Li Kevin and Kelly, Jacob and Li, Zi-Qi and Schneider, Rosalia G. and Thillaisundaram, Ashok and Patani, Harshnira and Zambaldi, Vinicius F. and Singh, Sukhdeep and La, David and Domecillo, Masy and Mora, Ariane N. and Reisenbauer, Julia C. and Zhang, Yu and Papa, Eliseo and {\v{Z}}emgulyt{\.e}, Akvil{\.e} and Wu, Yu-Han and {\v{Z}}{\'\i}dek, Augustin and Shi, Jiaxin and Margand, Grace and Assem, Naila and Stephen, Kate and Emrich, Charlie and Liu, Peng and Colwell, Lucy and Hassabis, Demis and Fergus, Rob and Arnold, Frances H. and Kohli, Pushmeet and Wang, Jue},
    journal={bioRxiv},
    year={2026},
    elocation-id={2026.10.01.756017},
    doi={10.64898/2026.10.01.756017},
    url={https://www.biorxiv.org/content/10.64898/2026.10.01.756017v1}
  }
citation: 'Zachary Wu, Josh Abramson, Thomas Frerix, Alexander E. Chu, Ruijie K. Zhang, Luca Schulz, Amy E. Danson, Tristan O. C. Kwan, Li Kevin Wenliang, Jacob Kelly, Zi-Qi Li, Rosalia G. Schneider, Ashok Thillaisundaram, Harshnira Patani, Vinicius F. Zambaldi, Sukhdeep Singh, David La, Masy Domecillo, Ariane N. Mora, Julia C. Reisenbauer, Yu Zhang, Eliseo Papa, Akvilė Žemgulytė, Yu-Han Wu, Augustin Žídek, Jiaxin Shi, Grace Margand, Naila Assem, Kate Stephen, Charlie Emrich, Peng Liu, Lucy Colwell, Demis Hassabis, Rob Fergus, Frances H. Arnold, Pushmeet Kohli and Jue Wang (2026). Designing enzymes for new-to-nature chemistry and non-natural substrates with AlphaProtein Novo. bioRxiv, 2026.10.01.756017.'
---
### Abstract
Creating highly active enzymes for arbitrary reactions is a transformative goal for the molecular sciences. Traditional protein engineering is constrained by a reliance on existing natural starting points, which are often challenging to discover. *De novo* design offers the potential to overcome this by creating enzymes from first principles, but has yet to achieve practically relevant catalytic properties. Here we present AlphaProtein Novo (AP Novo), a machine-learning pipeline that demonstrates, for the first time, that *de novo* enzyme design can outperform natural sequence mining in addressing challenging chemistry. We used AP Novo to design new-to-nature nitrene transferases to synthesise the pharmacophore piperidine with unprecedented product selectivity, and to create enzymes that degrade the environmental toxin DEHP under conditions that denature natural enzymes. We also obtained state-of-the-art catalytic efficiencies on two well-studied model reactions, and through iterative design and analysis found that key enablers of success were mechanism-inspired metrics based on AlphaFold 3 predictions and sequence-ensemble-based scoring of designed backbones. Our results show that *de novo* design has become a powerful complement to natural enzyme diversity for discovering catalysts for a range of applications.

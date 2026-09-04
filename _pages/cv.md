---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

{% comment %}
  Academic CV. Education, experience and skills come from _data/cv.yml;
  publications, talks and distinctions come from the collections. The same
  page is printed to files/yu-han-wu-cv.pdf by .github/scripts/cv-pdf.js using
  the print styles in _sass/layout/_cv.scss, where the header below is shown
  and the site chrome is hidden.
{% endcomment %}

<div class="cv">

<header class="cv__head">
  <div class="cv__identity">
    <p class="cv__name">{{ site.author.name }}{% if site.author.name_native %} <span class="cv__name-native" lang="zh-Hant">{{ site.author.name_native }}</span>{% endif %}</p>
    <p class="cv__tag">PhD student in diffusion models and machine learning theory</p>
    <p class="cv__tag cv__tag--muted">LPSM, Sorbonne University &middot; Google DeepMind &middot; Paris, France</p>
  </div>
  <ul class="cv__contact">
    <li><a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a></li>
    <li><a href="https://yh-wu.com">yh-wu.com</a></li>
    <li><a href="https://github.com/{{ site.author.github }}">github.com/{{ site.author.github }}</a></li>
    {% if site.author.googlescholar %}<li><a href="{{ site.author.googlescholar }}">Google Scholar</a></li>{% endif %}
  </ul>
</header>

<p class="cv__download"><a class="pub__pill" href="{{ base_path }}{{ site.author.cv_pdf }}"><i class="fas fa-file-arrow-down" aria-hidden="true"></i>Download PDF</a></p>

<section class="cv__section">
  <h2 id="education">Education</h2>
  {% include cv-entries.html items=site.data.cv.education %}
</section>

<section class="cv__section">
  <h2 id="publications">Publications</h2>
  {% assign papers = site.publications | reverse %}
  {% assign has_pre = false %}{% for p in papers %}{% if p.venue contains "arXiv" or p.venue contains "reprint" %}{% assign has_pre = true %}{% endif %}{% endfor %}
  <h3 class="cv__sub">Conference and journal papers</h3>
  <ol class="cv__pubs">
    {%- for p in papers %}{% unless p.venue contains "arXiv" or p.venue contains "reprint" %}
    <li>
      {% assign post = p %}{% include pub-vars.html %}{{ pub_citation | replace: "Yu-Han Wu", "<strong>Yu-Han Wu</strong>" }}
      {%- if p.award %} <span class="cv__flag">{{ p.award }}</span>{% endif %}
      {%- if p.badges %}{% for b in p.badges %} <span class="cv__flag">{{ b }}</span>{% endfor %}{% endif %}
      <a class="cv__pub-link" href="{{ base_path }}{{ p.url }}">page</a>
    </li>
    {%- endunless %}{% endfor %}
  </ol>
  {% if has_pre %}
  <h3 class="cv__sub">Preprints</h3>
  <ol class="cv__pubs">
    {%- for p in papers %}{% if p.venue contains "arXiv" or p.venue contains "reprint" %}
    <li>
      {% assign post = p %}{% include pub-vars.html %}{{ pub_citation | replace: "Yu-Han Wu", "<strong>Yu-Han Wu</strong>" }}
      <a class="cv__pub-link" href="{{ base_path }}{{ p.url }}">page</a>
    </li>
    {%- endif %}{% endfor %}
  </ol>
  {% endif %}
</section>

<section class="cv__section">
  <h2 id="talks">Talks and posters</h2>
  <ul class="cv__entries">
    {%- for t in site.talks reversed %}
    <li class="cv__entry">
      <div class="cv__body">
        <span class="cv__what">{{ t.type | default: "Talk" }} at {{ t.title }}</span>
        <span class="cv__where">{{ t.venue }}{% if t.location %}, {{ t.location }}{% endif %}</span>
      </div>
      <div class="cv__when">{{ t.date | date: "%b %Y" }}</div>
    </li>
    {%- endfor %}
  </ul>
</section>

<section class="cv__section">
  <h2 id="distinctions">Distinctions</h2>
  <ul class="cv__entries">
    {%- for p in papers %}
      {%- if p.award %}
    <li class="cv__entry">
      <div class="cv__body"><span class="cv__what">{{ p.award }}, {{ p.venue }}</span><span class="cv__where">{{ p.title }}</span></div>
      <div class="cv__when">{{ p.date | date: "%Y" }}</div>
    </li>
      {%- endif %}
      {%- for b in p.badges %}
    <li class="cv__entry">
      <div class="cv__body"><span class="cv__what">{{ b }}</span><span class="cv__where">{{ p.title }}</span></div>
      <div class="cv__when">{{ p.date | date: "%Y" }}</div>
    </li>
      {%- endfor %}
    {%- endfor %}
  </ul>
</section>

<section class="cv__section">
  <h2 id="experience">Research experience</h2>
  {% include cv-entries.html items=site.data.cv.experience %}
</section>

<section class="cv__section">
  <h2 id="skills">Skills</h2>
  <ul class="cv__skills">
    {%- for s in site.data.cv.skills %}
    <li><span class="cv__skill-label">{{ s.label }}</span> {{ s.items }}</li>
    {%- endfor %}
  </ul>
</section>

</div>

---
layout: page
permalink: /ja/publications/
title: publications
nav: true
nav_order: 2
lang: ja
---

{% include bib_search.liquid %}
{% include publication_view_toggle.liquid %}

<div id="pub-view-year" class="pub-view" role="tabpanel" aria-labelledby="pub-view-tab-year">
  {% include publications_by_year.liquid %}
</div>

<div id="pub-view-category" class="pub-view d-none" role="tabpanel" aria-labelledby="pub-view-tab-category" hidden>
  {% include publications_by_category.liquid %}
</div>

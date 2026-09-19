"""Generate both complete static CV pages. Run: python3 generate.py."""
from pathlib import Path
import json
from html import escape
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent
CONTENT = json.loads((ROOT / "content.json").read_text())
ARROW = '<span aria-hidden="true">↗</span>'
ICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#214bc4"/><text x="7" y="44" font-family="Arial,sans-serif" font-size="36" font-weight="700" fill="white">Ld</text></svg>'

def link(url, text, c, cls="text-link"):
    return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener noreferrer">{text} {ARROW}<span class="sr-only"> ({c["external"]})</span></a>'

for lang, c in CONTENT.items():
    base = "../" if lang == "en" else "./"
    path = ROOT / "dist" / ("en/index.html" if lang == "en" else "index.html")
    nav = "".join(f'<a href="#{id}">{text}</a>' for id,text in zip(["projects", "education", "skills", "contact"], c["nav"]))
    language_items = []
    for code, href, label in [("fr", "index.html", "FR"), ("en", "en/index.html", "EN")]:
        current = ' aria-current="page"' if code == lang else ''
        language_items.append(f'<a href="{base}{href}" lang="{code}" hreflang="{code}"{current}>{label}</a>')
    language_links = "".join(language_items)
    projects = "".join(f'''
      <article class="project-row" aria-labelledby="project-{p['number']}">
        <span class="project-number">{p['number']}</span>
        <div class="project-heading"><p class="eyebrow">{p['category']}</p><h3 id="project-{p['number']}">{p['title']}</h3><p class="tech">{p['stack']}</p></div>
        <div class="project-copy"><p>{p['description']}</p><p class="muted">{p['detail']}</p>{link(p['url'],c['source'],c) if 'url' in p else '<p class="project-note">'+p['note']+'</p>'}</div>
      </article>''' for p in c['projects'])
    education = "".join(f'''
      <article class="education-row"><p class="date">{e['date']}</p><div><h3>{e['degree']}</h3><p class="institution">{e['place']}</p><p class="muted">{e['detail']}</p>{'<p class="education-note">'+e['note']+'</p>' if e.get('note') else ''}</div></article>''' for e in c['education'])
    skills = "".join(f'<div><dt>{title}</dt><dd>{value}</dd></div>' for title,value in c['skills'])
    qnotes = "".join(f'<div><dt>{title}</dt><dd>{value}</dd></div>' for title,value in c['qNotes'])
    html = f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{escape(c['description'],quote=True)}">
  <meta name="theme-color" content="#fafbfc">
  <meta name="color-scheme" content="light dark">
  <meta property="og:title" content="{escape(c['title'],quote=True)}">
  <meta property="og:description" content="{escape(c['description'],quote=True)}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="{'fr_FR' if lang == 'fr' else 'en_GB'}">
  <meta property="og:locale:alternate" content="{'en_GB' if lang == 'fr' else 'fr_FR'}">
  <title>{c['title']}</title>
  <link rel="alternate" hreflang="fr" href="{base}index.html">
  <link rel="alternate" hreflang="en" href="{base}en/index.html">
  <link rel="alternate" hreflang="x-default" href="{base}index.html">
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,{quote(ICON)}">
  <script>try{{const t=localStorage.getItem('lyes-theme')||localStorage.getItem('lyes-original-theme');if(t==='dark'||t==='light')document.documentElement.dataset.theme=t;}}catch(e){{}}</script>
  <link rel="stylesheet" href="{base}assets/style.css">
  <script defer src="{base}assets/script.js"></script>
</head>
<body id="top">
  <a class="skip-link" href="#main">{c['skip']}</a>
  <header class="site-header wrap">
    <a class="wordmark" href="#top" aria-label="Lyes Djemaa">Ld<span aria-hidden="true">.</span></a>
    <nav class="main-nav" aria-label="{c['navLabel']}">{nav}</nav>
    <div class="header-controls">
      <nav class="language-switch" aria-label="{c['languageLabel']}">{language_links}</nav>
      <button class="theme-toggle" type="button" aria-label="{c['themeLabel']}" aria-pressed="false" data-light="{c['themeLight']}" data-dark="{c['themeDark']}" hidden><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="12" r="8"/><path d="M12 4a8 8 0 0 1 0 16Z" fill="currentColor"/></svg><span>{c['themeDark']}</span></button>
    </div>
  </header>
  <main id="main">
    <section class="hero wrap" aria-labelledby="name">
      <div class="hero-kicker"><p class="eyebrow">{c['folio']}</p><p class="eyebrow">Paris, France</p></div>
      <div class="hero-main">
        <h1 id="name">Lyes<br>Djemaa<span class="name-period">.</span></h1>
        <div class="hero-profile"><h2>{c['role']}</h2><p>{c['intro']}</p><a class="cv-link" href="{base}assets/{c['pdfFile']}" download>{c['download']}<span aria-hidden="true">↓</span><small>{c['pdf']}</small></a></div>
      </div>
      <div class="hero-bottom"><div class="availability"><p class="eyebrow">{c['availabilityLabel']}</p><p class="availability-date">{c['availability']}</p><p class="availability-detail">{c['duration']}</p></div><div class="social-links">{link('https://github.com/LYuuss','GitHub',c)}{link('https://www.linkedin.com/in/lyesdjm','LinkedIn',c)}<a class="text-link" href="mailto:lyesdjemaa2901@hotmail.com">Email {ARROW}</a></div></div>
    </section>

    <section class="section wrap" id="projects" aria-labelledby="projects-title">
      <div class="section-heading"><div class="section-label"><span>01</span><h2 id="projects-title">{c['workTitle']}</h2></div><p>{c['workNote']}</p></div>
      <article class="featured-project" aria-labelledby="qchain-title">
        <div class="featured-title"><p class="eyebrow">{c['qCategory']}</p><h3 id="qchain-title">QChain</h3><p class="tech">Python · Flask · Docker</p>{link('https://github.com/LYuuss/Q-CHAIN',c['source'],c)}</div>
        <div class="featured-copy"><p>{c['qDescription']}</p><p>{c['qDetail']}</p></div>
        <dl class="project-facts" aria-label="{c['qNotesLabel']}">{qnotes}</dl>
      </article>
      <div class="project-list">{projects}</div>
      <p class="exploration"><span>{c['explorationLabel']}</span>{c['exploration']}</p>
    </section>

    <section class="section wrap split-section" id="education" aria-labelledby="education-title">
      <div class="section-intro"><div class="section-label"><span>02</span><h2 id="education-title">{c['educationTitle']}</h2></div><p class="section-caption">{c['educationIntro']}</p></div>
      <div class="education-list">{education}<aside class="experience"><p class="eyebrow">{c['experienceLabel']}</p><h3>{c['experienceTitle']}</h3><p class="date">{c['experienceDate']}</p><p class="muted">{c['experience']}</p></aside></div>
    </section>

    <section class="section wrap split-section" id="skills" aria-labelledby="skills-title">
      <div class="section-intro"><div class="section-label"><span>03</span><h2 id="skills-title">{c['skillsTitle']}</h2></div><p class="section-caption">{c['skillsIntro']}</p></div>
      <div><dl class="skills-list">{skills}</dl><div class="languages"><p class="eyebrow">{c['languagesLabel']}</p><p>{c['languages']}</p><p class="language-score">TOEIC <strong>900<span>/990</span></strong></p></div></div>
    </section>

    <section class="contact-section" id="contact" aria-labelledby="contact-title"><div class="wrap contact-inner"><div><p class="eyebrow">04 / Contact</p><h2 id="contact-title">{c['contactTitle']}</h2><p class="contact-copy">{c['contactCopy']}</p></div><div class="contact-details"><a class="contact-email" href="mailto:lyesdjemaa2901@hotmail.com"><span>{c['contactLabel']} {ARROW}</span><span>lyesdjemaa2901<wbr>@hotmail.com</span></a><a class="phone" href="tel:+33761137883"><span>{c['phoneLabel']}</span>+33 7 61 13 78 83</a><div class="social-links">{link('https://github.com/LYuuss','GitHub',c)}{link('https://www.linkedin.com/in/lyesdjm','LinkedIn',c)}</div></div></div></section>
  </main>
  <footer class="wrap footer"><p>© <span id="year">2026</span> Lyes Djemaa</p><div><button type="button" class="print-button" hidden>{c['print']}</button><a href="#top">{c['top']} <span aria-hidden="true">↑</span></a></div></footer>
</body>
</html>
'''
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(html)
    print(f"Generated {path.relative_to(ROOT)}")

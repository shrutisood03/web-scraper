# Adaptive Web Scraping & Change Detection on Modern Pricing Pages

## Overview

Modern SaaS pricing pages appear simple to users, but are implemented as dynamic,
JavaScript-heavy web applications that frequently change without notice.

This project explores a key question:

> Why is scraping a website once often misleading, even when scraping works?

Rather than focusing only on data extraction, this project studies how modern web
pages are rendered, how their content evolves over time, and why browser-based
scraping is often necessary for accuracy.

---

## What This Project Does

- Scrapes publicly accessible pricing and feature pages
- Compares static HTTP scraping with browser-based scraping
- Stores timestamped snapshots of rendered content
- Highlights how page content changes silently over time
- Documents how modern websites defend against automation
- Respects ethical and legal scraping boundaries

---

## Why Pricing Pages?

Pricing pages are ideal case studies because:

- No public APIs exist
- Content is business-critical yet unstable
- Pages rely heavily on JavaScript rendering
- Small wording changes can alter meaning significantly

This makes them a realistic and high-value scraping challenge.

---

## Project Structure

```
adaptive-web-scraper/
├── scraping.py
├── requirements.txt
├── case_study_analysis.md
├── data/
│ └── output.json
├── scraping_basics/
│ ├── web_rendering_and_scraping.md
│ └── security_and_ethics.md
└── README.md

```

---

## Key Takeaway

Scraping modern websites is no longer about copying HTML.
It is about understanding how systems render content, defend themselves,
and change silently over time.

This project treats scraping as a **systems problem**, not a scripting task.

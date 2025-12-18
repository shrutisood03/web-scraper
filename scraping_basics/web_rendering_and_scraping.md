# Web Rendering & Scraping Behavior

## Static vs JavaScript-Rendered Pages

A common assumption is that requesting a web page returns all visible content.
This is no longer true for most modern websites.

### Static Pages
- HTML response contains all meaningful content
- Content is immediately visible in "View Page Source"
- Can be scraped using simple HTTP requests

### JavaScript-Rendered Pages
- Initial HTML is incomplete or empty
- Content is injected after JavaScript execution
- Visible text appears only in the final DOM
- Static scraping tools often fail

---

## Why Static Scraping Breaks

When using basic HTTP tools:
- The server returns placeholder HTML
- Data containers exist but are empty
- Meaningful content is loaded later via JavaScript

This explains why tools like `requests` or `curl` may return valid responses
but still fail to extract useful data.

---

## Role of the Browser

Modern websites behave like applications rather than documents.

A real browser:
- Executes JavaScript
- Performs internal API calls
- Applies client-side logic
- Builds the final DOM shown to users

Browser-based tools allow scrapers to observe the same page state
that a human user sees.

---

## Why Scraping Once Is Insufficient

Even after successful rendering:
- Pricing copy may change silently
- Features may be reordered or reworded
- A/B testing may alter visible content
- Localization or personalization may apply

This project captures multiple snapshots to demonstrate how
web content evolves over time.

---

## Key Insight

Scraping success does not guarantee data reliability.
Understanding rendering behavior is essential before trusting extracted data.

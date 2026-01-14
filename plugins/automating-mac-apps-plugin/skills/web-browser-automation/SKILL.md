---
name: web-browser-automation
description: Comprehensive macOS browser automation using PyXA, Playwright, Selenium, and Puppeteer for desktop web testing, scraping, and workflow automation. Use when automating Chrome, Edge, Brave, Arc browsers, building cross-browser testing suites, web scraping, or browser workflow automation.
---

# macOS Web Browser Automation Guide

## Table of Contents
1. [Overview](#overview)
2. [Browser Compatibility Matrix](#browser-compatibility-matrix)
3. [PyXA Integration](#pyxa-integration)
4. [Playwright Automation](#playwright-automation)
5. [Selenium WebDriver](#selenium-webdriver)
6. [Puppeteer Node.js](#puppeteer-nodejs)
7. [Comprehensive Automation Workflows](#comprehensive-automation-workflows)
   - [Workflow 1: Multi-Browser Tab Management](#workflow-1-multi-browser-tab-management)
   - [Workflow 2: Automated Research and Data Collection](#workflow-2-automated-research-and-data-collection)
   - [Workflow 3: Cross-Browser Testing Suite](#workflow-3-cross-browser-testing-suite)
   - [Workflow 4: Web Scraping and Data Extraction](#workflow-4-web-scraping-and-data-extraction)
8. [Brief Automation Patterns](#brief-automation-patterns)
9. [Advanced Techniques](#advanced-techniques)
10. [Troubleshooting and Validation](#troubleshooting-and-validation)
11. [Security Considerations](#security-considerations)
12. [Performance Optimization](#performance-optimization)
13. [Integration Examples](#integration-examples)

## Overview

This guide covers comprehensive web browser automation on macOS desktop, focusing on automation (not testing). We cover four major automation frameworks with practical examples for real-world scenarios.

**PyXA Installation:** To use PyXA examples in this skill, see the installation instructions in `automating-mac-apps` skill (PyXA Installation section).

### Primary Automation Tools

- **PyXA**: macOS-native Python wrapper with direct browser integration
- **Playwright**: Cross-platform framework with Python bindings for modern web automation
- **Selenium**: Industry-standard automation with ChromeDriver integration
- **Puppeteer**: Node.js framework for Chrome/Chromium automation

### Tool Selection Guide

| Tool | Primary Use | Key Advantages |
|------|-------------|----------------|
| **PyXA** | macOS-native control | Direct OS integration, Arc spaces |
| **Playwright** | Cross-browser testing | Auto-waiting, mobile emulation |
| **Selenium** | Legacy enterprise | Mature ecosystem, wide language support |
| **Puppeteer** | Headless Chrome | Fast execution, PDF generation |

See `references/browser-compatibility-matrix.md` for detailed browser support.

## Getting Started

1. **Choose your framework** based on your needs (see Tool Selection Guide above)
2. **Install dependencies** for your chosen framework
3. **Follow framework-specific guides** linked below
4. **Review workflows** for common automation patterns

## Framework Guides

### PyXA Browser Integration
- **Best for**: macOS-native browser control with Arc spaces support
- **Installation**: `pip install PyXA`
- **Guide**: `references/pyxa-integration.md`

### Playwright Automation
- **Best for**: Cross-browser testing with auto-waiting
- **Installation**: `pip install playwright && playwright install`
- **Guide**: `references/playwright-automation.md`

### Selenium WebDriver
- **Best for**: Legacy enterprise automation
- **Installation**: `pip install selenium`
- **Guide**: `references/selenium-webdriver.md`

### Puppeteer Node.js
- **Best for**: Headless Chrome with PDF generation
- **Installation**: `npm install puppeteer`
- **Guide**: `references/puppeteer-automation.md`

## Automation Workflows

Complete workflow examples for common automation scenarios:

### Multi-Browser Tab Management
**Guide**: `references/workflows.md#workflow-1-multi-browser-tab-management`

### Automated Research and Data Collection
**Guide**: `references/workflows.md#workflow-2-automated-research-and-data-collection`

### Cross-Browser Testing Suite
**Guide**: `references/workflows.md#workflow-3-cross-browser-testing-suite`

### Web Scraping and Data Extraction
**Guide**: `references/workflows.md#workflow-4-web-scraping-and-data-extraction`

## Brief Automation Patterns

### Browser Launch and Profile Management
```python
# PyXA approach for Chrome
chrome = PyXA.Application("Google Chrome")
chrome.new_window("https://example.com")
```

### Tab Organization and Grouping
```python
# PyXA tab filtering
tabs = chrome.windows()[0].tabs()
work_tabs = [tab for tab in tabs if "meeting" in tab.title().lower()]
for tab in work_tabs:
    tab.close()
```

### JavaScript Injection for Content Extraction
```python
# PyXA JavaScript execution
content = tab.execute_javascript("document.body.innerText")
links = tab.execute_javascript("Array.from(document.querySelectorAll('a')).map(a => a.href)")
```

### Cross-Browser Synchronization
```python
# PyXA multi-browser control
browsers = [PyXA.Application("Google Chrome"), PyXA.Application("Microsoft Edge")]
for browser in browsers:
    browser.new_tab("https://shared-resource.com")
```

### Form Filling and Interaction
```python
# Playwright auto-waiting
page.fill("#username", "user@example.com")
page.click("text=Submit")  # Auto-waits for element
```

### Screenshot and Content Capture
```javascript
// Puppeteer screenshot
await page.screenshot({ path: 'capture.png', fullPage: true });
await page.pdf({ path: 'page.pdf', format: 'A4' });
```

### Basic Playwright Usage

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    title = page.title()
    print(f"Page title: {title}")
    browser.close()
```

### Advanced Playwright Features

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch with options
    browser = p.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )

    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    )

    page = context.new_page()

    # Auto-waiting interactions
    page.goto("https://example.com")
    page.click("text=Get Started")  # Auto-waits for element
    page.fill("#search-input", "automation")
    page.press("#search-input", "Enter")

    # Handle dynamic content
    page.wait_for_selector(".results")
    results = page.query_selector_all(".result-item")

    for result in results:
        title = result.query_selector("h3").text_content()
        print(f"Result: {title}")

    browser.close()
```

## Additional Resources

### Advanced Techniques
- **Network Interception**: `references/playwright-automation.md#network-interception`
- **Parallel Browser Automation**: `references/selenium-webdriver.md#parallel-testing`
- **Performance Monitoring**: `references/puppeteer-automation.md#performance-monitoring`
- **Browser Context Management**: `references/selenium-webdriver.md#browser-contexts-and-pages`

### Troubleshooting
- **Element Not Found Errors**: Common solutions across frameworks
- **Stale Element References**: Handling dynamic content
- **Browser Detection**: Avoiding automation detection
- **Network Timeout Issues**: Timeout configuration

### Security Considerations
- **Credential Management**: Secure storage of login credentials
- **Certificate Handling**: SSL/TLS certificate validation
- **Sandbox and Isolation**: Running automation in isolated environments
- **Data Sanitization**: Cleaning extracted data

### Performance Optimization
- **Browser Configuration**: Disabling unnecessary features
- **Network Optimization**: Blocking unwanted resources
- **Parallel Execution**: Running tests concurrently
- **Resource Pooling**: Managing browser instances efficiently

## Integration Examples

### Database Integration
Store scraped data in SQLite or other databases for later analysis.

### API Integration
Submit automation results to REST APIs for reporting and monitoring.

### File System Integration
Organize screenshots and reports by date, domain, and test type.

---

## Complete Reference Guides

For comprehensive documentation on each framework:

- **PyXA**: `references/pyxa-integration.md` - macOS-native browser control
- **Playwright**: `references/playwright-automation.md` - Cross-browser testing
- **Selenium**: `references/selenium-webdriver.md` - Enterprise automation
- **Puppeteer**: `references/puppeteer-automation.md` - Node.js Chrome automation

**Workflow Examples**: `references/workflows.md` - Complete automation scenarios

This guide provides a high-level overview with links to detailed framework documentation for specific implementation needs.

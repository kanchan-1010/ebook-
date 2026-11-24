# MASTER PROJECT MAP: "DEAR 2027, I'M READY."
> **Author & Creator:** Kanchan Pathare  
> **Target Audience:** Indian Youth (Ages 18–35: Students, Job Seekers, Young Working Professionals)  
> **GitHub Repository:** [kanchan-1010/ebook-](https://github.com/kanchan-1010/ebook-)  
> **Workspace Path:** `c:\Users\Asus\Downloads\ebook\`  

---

## 🗺️ 1. High-Level Ecosystem Architecture

```mermaid
flowchart TD
    subgraph Hub["Master Portal & Access Layer"]
        A["index.html (Master Portal)"]
        B["start_preview.bat (One-Click Local Preview)"]
        C["GitHub Pages (Live Worldwide Hosting)"]
    end

    subgraph Product["Core Deliverables & Products"]
        D["dear_2027_master_planner_52pages.pdf<br/>(1.9 MB Print/Digital Journal)"]
        E["life_reset_dashboard.html<br/>(Interactive 5-Pillar Web App)"]
        F["dear_2027_master_planner_52pages.html<br/>(HTML Source & Web View)"]
    end

    subgraph Pipeline["Build & Automation Pipeline"]
        G["02_COMPLETE_PLANNER_CONTENT_52_PAGES.md<br/>(Full Text Manuscript)"]
        H["generate_master_planner_html.py<br/>(HTML Compiler)"]
        I["export_planner_to_pdf.py<br/>(Headless Chrome/Edge PDF Exporter)"]
    end

    subgraph Strategy["Research, Design & Sales Engine"]
        J["01_MARKET_RESEARCH_AND_STRATEGY.md<br/>(Audience & Psychology)"]
        K["03_DESIGN_SYSTEM_AND_PAGE_PROMPTS.md<br/>(Brand Style & Canva Prompts)"]
        L["04_QUALITY_ASSURANCE_AND_COMPLIANCE.md<br/>(2027 Calendar & QA Audit)"]
        M["05_MARKETING_AND_SALES_LAUNCH_PLAYBOOK.md<br/>(SuperProfile & Reel Scripts)"]
    end

    Hub --> Product
    G --> H --> F --> I --> D
    Strategy --> Product
    Hub --> Strategy
```

---

## 📂 2. Master Repository File Map

| File / Directory | Category | Size / Format | Primary Function & Role |
|---|---|---|---|
| [index.html](index.html) | **User Portal** | ~11 KB (HTML5) | Central dashboard connecting the web app, PDF downloads, and strategic guides. |
| [life_reset_dashboard.html](life_reset_dashboard.html) | **Interactive App** | ~58 KB (HTML/JS) | 5-pillar client-side web application with local storage persistence. |
| [dear_2027_master_planner_52pages.pdf](dear_2027_master_planner_52pages.pdf) | **Commercial Product** | 1.9 MB (PDF) | Publication-grade A4 PDF formatted with 22mm binding edge margins. |
| [dear_2027_master_planner_52pages.html](dear_2027_master_planner_52pages.html) | **Web Journal** | ~200 KB (HTML/CSS) | Complete 52-page styled journal view with sample data & print controls. |
| [generate_master_planner_html.py](generate_master_planner_html.py) | **Compiler** | ~81 KB (Python) | Parses the markdown manuscript and compiles the 52-page HTML document. |
| [export_planner_to_pdf.py](export_planner_to_pdf.py) | **Exporter** | ~1.7 KB (Python) | Headless browser automation script to render and print A4 PDF. |
| [start_preview.bat](start_preview.bat) | **Launcher** | Batch Script | One-click Windows runner to launch local HTTP server and browser. |
| [start_server.py](start_server.py) | **Server** | ~1.2 KB (Python) | Zero-dependency local development server with auto-port discovery. |
| [00_QUICKSTART_AND_EXECUTION_GUIDE.md](00_QUICKSTART_AND_EXECUTION_GUIDE.md) | **Handbook** | ~4.5 KB (Markdown) | 90-day implementation cadence and detailed instructions. |
| [01_MARKET_RESEARCH_AND_STRATEGY.md](01_MARKET_RESEARCH_AND_STRATEGY.md) | **Strategy** | ~18 KB (Markdown) | Indian youth market analysis, buyer personas (Rohan & Priya), and positioning. |
| [02_COMPLETE_PLANNER_CONTENT_52_PAGES.md](02_COMPLETE_PLANNER_CONTENT_52_PAGES.md) | **Manuscript** | ~43 KB (Markdown) | Verbatim source text for every single page from Page 1 to Page 52. |
| [03_DESIGN_SYSTEM_AND_PAGE_PROMPTS.md](03_DESIGN_SYSTEM_AND_PAGE_PROMPTS.md) | **Design** | ~22 KB (Markdown) | Color palette, typography hierarchy, and 52 individual Canva prompts. |
| [04_QUALITY_ASSURANCE_AND_COMPLIANCE.md](04_QUALITY_ASSURANCE_AND_COMPLIANCE.md) | **QA & Legal** | ~8 KB (Markdown) | 2027 calendar verification, Indian financial/medical disclaimers. |
| [05_MARKETING_AND_SALES_LAUNCH_PLAYBOOK.md](05_MARKETING_AND_SALES_LAUNCH_PLAYBOOK.md) | **Marketing** | ~16 KB (Markdown) | SuperProfile listing copy, 10 reel scripts, 5 carousels, break-even matrix. |
| [.github/workflows/deploy-pages.yml](.github/workflows/deploy-pages.yml) | **DevOps** | YAML | Automated GitHub Pages CI/CD workflow triggered on `main` push. |
| [requirements.txt](requirements.txt) | **Environment** | Text | Python dependency documentation for optional headless automation. |
| [README.md](README.md) | **Documentation** | ~5 KB (Markdown) | Public repository front page and navigation index. |

---

## 🏛️ 3. The 5 Core Life Reset Pillars

```mermaid
graph LR
    P1["1. Mental & Social Boundaries<br/>• Family Script Generator<br/>• Digital Sunset at 9:30 PM"] 
    P2["2. Indian Wealth & Safety (₹)<br/>• 50/30/20 Salary Allocator<br/>• 48-Hour Impulse Spend Pause<br/>• 6-Month Emergency Runway"]
    P3["3. Physical Vitality<br/>• 1.3g/kg Indian Protein Stacks<br/>• 8,000 Steps Tracker<br/>• Morning Balcony Sunlight"]
    P4["4. Career Moat<br/>• 90-Min Focus Deep Work<br/>• Anti-AI Automation Skills<br/>• Daily Proof of Work"]
    P5["5. 24h Urban Rhythm<br/>• Commute-Friendly Shutdown<br/>• Metro/Traffic Sanity Checklist<br/>• Consistent Sleep Cadence"]

    P1 --- P2 --- P3 --- P4 --- P5
```

---

## 📖 4. 52-Page Master Journal Page Map

```mermaid
flowchart TD
    subgraph Part1["Section 1: Foundations & Reflections (Pages 1–8)"]
        S1["Page 1: Front Cover<br/>Page 2: Imprint & Disclaimers<br/>Page 3: Author Welcome Letter<br/>Page 4: 2026 Brutal Truth Reflection<br/>Page 5: The Unsubscribe Ritual<br/>Page 6: 8-Spoke Wheel of Life<br/>Page 7: 2027 Non-Negotiables Contract<br/>Page 8: Vision Board & Word of the Year"]
    end

    subgraph Part2["Section 2: 5-Pillar Master Blueprints (Pages 9–13)"]
        S2["Page 9: Pillar 1 Blueprint (Mind & Boundaries)<br/>Page 10: Pillar 2 Blueprint (Indian Wealth & SIPs)<br/>Page 11: Pillar 3 Blueprint (High-Protein Fuel)<br/>Page 12: Pillar 4 Blueprint (Career Moat & Deep Work)<br/>Page 13: Pillar 5 Blueprint (24h Urban Rhythm)"]
    end

    subgraph Part3["Section 3: 12 Dated Monthly Spreads (Pages 14–37)"]
        S3["January to December 2027<br/>Each Month has 2 Pages:<br/>• Left Page: Calendar Grid + Priority Top 3 + Habit Grid<br/>• Right Page: Monthly Financial Allocator + Energy Audit"]
    end

    subgraph Part4["Section 4: Quarterly Audits & Emergency Reset (Pages 38–45)"]
        S4["Pages 38, 40, 42, 44: Q1, Q2, Q3, Q4 Deep Audits<br/>Pages 39, 41, 43, 45: 7-Day Life Reset Protocol & Emergency Slump Recovery"]
    end

    subgraph Part5["Section 5: Toolkits, Index & Back Cover (Pages 46–52)"]
        S5["Page 46: High-Protein Indian Food Database<br/>Page 47: 50/30/20 Budgeting Worksheets<br/>Page 48: 30-Day Digital Detox Tracker<br/>Page 49: Reading & Upskilling Log<br/>Page 50: Letters to Future Self<br/>Page 51: 2027 Year-End Celebration Review<br/>Page 52: Back Cover & Author Notes"]
    end

    Part1 --> Part2 --> Part3 --> Part4 --> Part5
```

---

## 💰 5. Commercial Funnel & Launch Architecture

```mermaid
flowchart LR
    Traffic["Top of Funnel (Traffic)<br/>• 10 Instagram Reels<br/>• 5 Educational Carousels<br/>• LinkedIn Career Posts"]
    LeadMagnet["Middle of Funnel<br/>• Free Web Dashboard<br/>• Family Script Generator<br/>• Salary Allocator Calculator"]
    Product["Bottom of Funnel (Offer)<br/>• 52-Page Master PDF Journal<br/>• ₹299 / ₹499 Price Point<br/>• Hosted on SuperProfile"]

    Traffic --> LeadMagnet --> Product
```

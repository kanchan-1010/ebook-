import re
import os
import html

def build_planner():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    md_path = os.path.join(base_dir, '02_COMPLETE_PLANNER_CONTENT_52_PAGES.md')
    out_path = os.path.join(base_dir, 'dear_2027_master_planner_52pages.html')

    with open(md_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # Split into pages
    parts = re.split(r'##\s+\[PAGE\s+(\d+)\]', raw_text)
    pages = {}
    for i in range(1, len(parts), 2):
        page_num = int(parts[i])
        page_content = parts[i+1].strip()
        pages[page_num] = page_content

    print(f"Extracted {len(pages)} pages.")

    # Helper to parse page lines into a structured dict or render HTML
    def parse_page(content):
        lines = [l.strip() for l in content.split('\n') if l.strip()]
        title = lines[0] if lines else ""
        body = lines[1:] if len(lines) > 1 else []
        return title, body

    html_pages = []

    for page_num in range(1, 53):
        content = pages.get(page_num, "")
        title_line, body_lines = parse_page(content)
        page_html = render_single_page(page_num, title_line, body_lines, content)
        html_pages.append(page_html)

    full_html = HTML_TEMPLATE.format(pages_content="\n".join(html_pages))

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"Master planner compiled successfully to {out_path} ({len(full_html)} bytes)")

def render_single_page(num, title_raw, lines, raw):
    # Determine section context
    if num in [1]:
        section = "COVER"
    elif num in [2, 3, 4, 5]:
        section = "ORIENTATION"
    elif 6 <= num <= 11:
        section = "SECTION 1: GOODBYE, 2026"
    elif 12 <= num <= 19:
        section = "SECTION 2: HELLO, 2027"
    elif 20 <= num <= 30:
        section = "SECTION 3: MY LIFE RESET"
    elif 31 <= num <= 42:
        section = "SECTION 4: 2027 MONTHLY JOURNEY"
    elif 43 <= num <= 51:
        section = "SECTION 5: PROGRESS & RESILIENCE"
    else:
        section = "BACK COVER"

    # Specific Page Layout Renderers
    if num == 1:
        return render_cover(raw)
    elif num == 2:
        return render_copyright(raw)
    elif num == 3:
        return render_toc(raw)
    elif num == 4:
        return render_welcome(raw)
    elif num == 5:
        return render_how_to_use(raw)
    elif num in [6, 12, 20, 43]:
        return render_section_divider(num, title_raw, raw, section)
    elif num == 11:
        return render_wheel_of_life(raw, num, section)
    elif num == 15:
        return render_vision_board(raw, num, section)
    elif num == 24:
        return render_financial_page(raw, num, section)
    elif num == 29:
        return render_habit_tracker(raw, num, section)
    elif num == 30:
        return render_recovery_plan(raw, num, section)
    elif 31 <= num <= 42:
        return render_monthly_spread(num, title_raw, raw, section)
    elif num == 48:
        return render_jar_of_wins(raw, num, section)
    elif num == 51:
        return render_closing(raw, num, section)
    elif num == 52:
        return render_back_cover(raw)
    else:
        return render_standard_worksheet(num, title_raw, raw, section)

def render_chintu(icon, tag, text):
    return f"""
    <div class="chintu-card">
        <div class="chintu-avatar">
            <span class="chintu-icon">{icon}</span>
            <span class="chintu-name">CHINTU</span>
        </div>
        <div class="chintu-bubble">
            <span class="chintu-title">🦉 {tag}</span>
            <p class="chintu-text">{text}</p>
        </div>
    </div>
    """

def get_chintu_month_tip(month_name):
    tips = {
        "January": ("❄️", "CHINTU'S JAN WARNING", "January motivation is peak danger. Don't buy ₹6,000 running shoes and plan 4:30 AM wakeups on Day 1. Start by not snoozing 5 times!"),
        "February": ("🍫", "CHINTU'S 28-DAY HACK", "February has only 28 days! That's a built-in discount on habit tracking. 22 days ticked = 80% legend status."),
        "March": ("📊", "CHINTU'S TAX ADVICE", "Tax saving deadline alert! Please don't panic-call your CA cousin on March 31 at 11:45 PM asking where to dump ₹50,000."),
        "April": ("🌱", "CHINTU'S Q2 CPR", "Q1 is over. If your New Year goals went into a coma, don't bury them—give them gentle CPR today. Reset is completely free!"),
        "May": ("🥭", "CHINTU'S HEAT PROTOCOL", "It's 42°C in India. Hydrate or perish. Aamras counts as mental wellness, but keep your 3-liter water bottle closer."),
        "June": ("🌧️", "CHINTU'S MID-YEAR AUDIT", "Half of 2027 is officially over! Stop panicking. You're alive, you're learning, and tea tastes better in monsoon."),
        "July": ("☕", "CHINTU'S MONSOON MOAT", "Raining outside? Best excuse to stay in, make ginger cutting chai, and put in 90 minutes of undisturbed deep focus."),
        "August": ("🇮🇳", "CHINTU'S FREEDOM CALL", "Independence Day month: Officially declare independence from unsolicited career advice at family dinner tables!"),
        "September": ("🎯", "CHINTU'S SPRINT ALERT", "Don't say 'I will start fresh in 2028'. You still have 120 full days in 2027. The best comeback begins right now."),
        "October": ("🪔", "CHINTU'S FESTIVE SURVIVAL", "Festive sales are here! Eat sweets, pass on the Soan Papdi box, but protect your UPI PIN from midnight flash sales."),
        "November": ("🧣", "CHINTU'S BLANKET STRUGGLE", "Winter mornings: The blanket has 10,000 Newton gravitational pull. Count 3-2-1, stand up, and claim the day."),
        "December": ("🎉", "CHINTU'S FINAL LAP", "Look at you! You made it to December 2027! Don't write off this month—finish with quiet pride and extra cookies.")
    }
    return tips.get(month_name, ("🦉", "CHINTU'S MONTHLY NUDGE", "One day at a time. Progress over perfection every single day!"))

def render_cover(raw):
    return """
    <div class="page cover-page" id="page-1">
        <div class="botanical-corner top-left">┌</div>
        <div class="botanical-corner top-right">┐</div>
        <div class="botanical-corner bottom-left">└</div>
        <div class="botanical-corner bottom-right">┘</div>
        <div class="cover-inner-border">
            <div class="cover-tag">2027 DATED ANNUAL EDITION • NORDIC SLATE ARCHITECTURAL SERIES</div>
            <h1 class="cover-title">Dear 2027,<br><em>I'm Ready.</em></h1>
            <div class="gold-flourish">━━━━━ ✦ ━━━━━</div>
            <h2 class="cover-subtitle">A Complete Life Reset & Goal-Setting Journal</h2>
            <p class="cover-tagline">"Create a life that feels right for you, not just a life that looks perfect on paper."</p>
            <div class="cover-author-box">
                <span class="by-text">BY</span>
                <span class="author-name">Kanchan Pathare</span>
            </div>
            <div class="cover-pills">
                <span class="pill">Mindful Focus</span>
                <span class="pill">Indian Financial Clarity (₹)</span>
                <span class="pill">Habit Mastery</span>
            </div>
        </div>
        <div class="page-footer">Page 1 of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_copyright(raw):
    return """
    <div class="page doc-page" id="page-2">
        <div class="page-header">
            <span class="header-section">PUBLISHING INFORMATION & COMPLIANCE</span>
            <span class="header-num">02</span>
        </div>
        <div class="content-box">
            <h2 class="page-title">Copyright, Permissions & Disclaimers</h2>
            <div class="accent-line"></div>
            
            <div class="card bg-cream">
                <h3>© Copyright & Personal License Notice</h3>
                <p><strong>Published Digitally by Kanchan Pathare</strong><br>
                © 2026–2027 Kanchan Pathare. All rights reserved.</p>
                <p>No part of this publication may be reproduced, distributed, resold, or transmitted in any form or by any means—electronic, mechanical, photocopying, recording, or otherwise—without the prior written permission of the author.</p>
                <p><em>Personal Use License:</em> This digital file is licensed exclusively for individual, personal use by the original purchaser. Sharing this file via public cloud drives, WhatsApp groups, Telegram channels, or unauthorized websites is strictly prohibited and subject to legal action under the Indian Copyright Act.</p>
            </div>

            <div class="card bg-rose">
                <h3>⚖️ Financial Planning Disclaimer</h3>
                <p>The financial tracking sheets, budgeting models (such as the 50/30/20 guideline), and savings frameworks contained in this journal are designed solely for personal organizational, goal-setting, and educational purposes. The author is not a SEBI-registered investment advisor or certified financial planner. Consult a qualified wealth advisor before executing major financial decisions.</p>
            </div>

            <div class="card bg-lavender">
                <h3>🌿 Mental Wellness & Self-Care Disclaimer</h3>
                <p>The reflective exercises, journal prompts, and habit coaching frameworks provided in this journal are self-development tools designed to foster mindfulness, peace, and clarity. They do not constitute formal psychological therapy, medical diagnosis, psychiatric intervention, or clinical counseling. If you are experiencing severe depression, clinical anxiety, or acute burnout, please consult a certified healthcare professional.</p>
            </div>
            
            <div class="signature-block">
                <div class="script-author">Kanchan Pathare</div>
                <div class="sub-author">Author & Independent Creator • India</div>
            </div>
        </div>
        <div class="page-footer">Page 2 of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_toc(raw):
    return """
    <div class="page doc-page" id="page-3">
        <div class="page-header">
            <span class="header-section">ORIENTATION & NAVIGATION</span>
            <span class="header-num">03</span>
        </div>
        <div class="content-box">
            <h2 class="page-title">Table of Contents & Navigational Guide</h2>
            <p class="section-intro">This journal is arranged into 5 progressive phases designed to guide you from gentle release to intentional action.</p>
            <div class="accent-line"></div>

            <div class="toc-grid">
                <div class="toc-card">
                    <span class="toc-badge">ORIENTATION</span>
                    <h4>Welcome & Foundation (Pages 4–5)</h4>
                    <ul>
                        <li><span class="p-num">Page 4:</span> Welcome Letter from Kanchan Pathare</li>
                        <li><span class="p-num">Page 5:</span> How to Experience This Journal for Sustainable Growth</li>
                    </ul>
                </div>

                <div class="toc-card">
                    <span class="toc-badge sage">PHASE 1</span>
                    <h4>Section 1: Goodbye, 2026 — The Honest Reflection (Pages 6–11)</h4>
                    <ul>
                        <li><span class="p-num">Page 7:</span> My 2026 Unfiltered Reflection</li>
                        <li><span class="p-num">Page 8:</span> My 2026 Wall of Triumphs (Big & Quiet Wins)</li>
                        <li><span class="p-num">Page 9:</span> Hard Lessons & Unexpected Blessings</li>
                        <li><span class="p-num">Page 10:</span> The Release Ritual: Things I Am Leaving Behind</li>
                        <li><span class="p-num">Page 11:</span> The 8-Spoke Wheel of Life Assessment</li>
                    </ul>
                </div>

                <div class="toc-card">
                    <span class="toc-badge rose">PHASE 2</span>
                    <h4>Section 2: Hello, 2027 — Vision, Values & Direction (Pages 12–19)</h4>
                    <ul>
                        <li><span class="p-num">Page 13:</span> Letter to My Future Self (Read Dec 31, 2027)</li>
                        <li><span class="p-num">Page 14:</span> Word of the Year & Core Personal Values</li>
                        <li><span class="p-num">Page 15:</span> Aesthetic 4-Box Vision Board Canvas</li>
                        <li><span class="p-num">Page 16:</span> Designing My "Felt-Right" Dream Tuesday</li>
                        <li><span class="p-num">Page 17:</span> The Priorities Filter & "Polite No" Matrix</li>
                        <li><span class="p-num">Page 18:</span> My Top 5 Core Goals with Meaningful Whys</li>
                        <li><span class="p-num">Page 19:</span> The Reverse Goal Action Engine</li>
                    </ul>
                </div>

                <div class="toc-card">
                    <span class="toc-badge lavender">PHASE 3</span>
                    <h4>Section 3: My Life Reset — Sustainable Everyday Systems (Pages 20–30)</h4>
                    <ul>
                        <li><span class="p-num">Pages 21–23:</span> Health, Career Milestones & Skill Roadmap</li>
                        <li><span class="p-num">Page 24:</span> Financial Freedom & Indian 50/30/20 Savings (₹)</li>
                        <li><span class="p-num">Pages 25–28:</span> Boundaries Scripts, Digital Wellness & Routines</li>
                        <li><span class="p-num">Page 29:</span> The 365-Day Micro-Habit Tracker Master</li>
                        <li><span class="p-num">Page 30:</span> The "Bad-Day Recovery Plan" (Emergency Reset)</li>
                    </ul>
                </div>

                <div class="toc-card">
                    <span class="toc-badge gold">PHASE 4 & 5</span>
                    <h4>Section 4 & 5: Monthly Journey & Resilience Archive (Pages 31–52)</h4>
                    <ul>
                        <li><span class="p-num">Pages 31–42:</span> 12 Dated Monthly Focus Spreads (Jan–Dec 2027)</li>
                        <li><span class="p-num">Pages 44–47:</span> Quarterly Reviews (Q1, Midyear Deep Reset, Q3, Q4)</li>
                        <li><span class="p-num">Pages 48–50:</span> Jar of Micro-Wins, Setback Log & Year-End Reflection</li>
                        <li><span class="p-num">Pages 51–52:</span> Closing Blessing & Back Cover</li>
                    </ul>
                </div>
            </div>
        </div>
        <div class="page-footer">Page 3 of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_welcome(raw):
    return """
    <div class="page doc-page" id="page-4">
        <div class="page-header">
            <span class="header-section">WELCOME & ORIENTATION</span>
            <span class="header-num">04</span>
        </div>
        <div class="content-box">
            <div class="chapter-tag">A LETTER FROM THE AUTHOR</div>
            <h2 class="page-title serif-italic">Dear Reader, Take a Gentle Breath.</h2>
            <div class="accent-line"></div>

            <div class="letter-body">
                <p class="lead-quote">"Welcome to a fresh beginning. If you are holding this journal right now, chances are you are tired of running a race with no finish line."</p>
                
                <p>In our fast-moving Indian society, we are constantly conditioned to hustle harder, compare ourselves to distant cousins, classmates, and LinkedIn peers, and chase benchmarks that often belong to someone else. We are taught that rest must be earned, that busyness equals self-worth, and that pausing is a sign of falling behind.</p>

                <p>I created <em>Dear 2027, I'm Ready</em> because I needed a sanctuary—a quiet, grounded, unhurried space where planning does not feel like punishment. You do not need to wake up at 5:00 AM if your body is exhausted. You do not need to overhaul your entire personality by the second week of January. What you truly need is clarity, self-compassion, and gentle, practical systems that hold you when life gets overwhelming.</p>

                <p>This journal is your permission slip to slow down, listen to what your life is telling you, and build habits that honor your energy. May 2027 be the year you stop waiting for 'someday'. May you build a life that feels peaceful on the inside, not just impressive on the outside.</p>

                <p class="warm-closing">Warmly and with deep belief in your journey,</p>
                <div class="author-sign-wrap">
                    <div class="author-sign">Kanchan Pathare</div>
                    <div class="author-title">Author, <em>Dear 2027, I'm Ready</em></div>
                </div>
            </div>
            
            <div class="quote-card-botanical">
                <p>🌿 <em>"You are not behind. You are exactly where your next chapter begins."</em></p>
            </div>
        </div>
        <div class="page-footer">Page 4 of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_how_to_use(raw):
    return """
    <div class="page doc-page" id="page-5">
        <div class="page-header">
            <span class="header-section">WELCOME & ORIENTATION</span>
            <span class="header-num">05</span>
        </div>
        <div class="content-box">
            <div class="chapter-tag">GUIDELINES FOR MINDFUL USAGE</div>
            <h2 class="page-title">How to Experience This Journal</h2>
            <div class="accent-line"></div>

            <div class="principle-cards">
                <div class="principle-item">
                    <div class="p-icon">01</div>
                    <div class="p-text">
                        <h4>Do Not Rush the Beginning</h4>
                        <p>Complete Section 1 (Goodbye, 2026) fully before jumping into 2027 goal setting. You cannot plant vibrant new seeds in soil crowded with last year's weeds and unresolved exhaustion.</p>
                    </div>
                </div>

                <div class="principle-item">
                    <div class="p-icon">02</div>
                    <div class="p-text">
                        <h4>Energy Over Rigidity</h4>
                        <p>If you miss 3 days, a week, or even an entire month, turn immediately to <strong>Page 30: The Bad-Day Recovery Plan</strong>. Consistency is not the absence of falling; it is the grace to return without guilt or self-punishment.</p>
                    </div>
                </div>

                <div class="principle-item">
                    <div class="p-icon">03</div>
                    <div class="p-text">
                        <h4>Digital Stylus or Home Print Binding</h4>
                        <p><strong>Digital:</strong> Open this PDF in GoodNotes, Notability, Samsung Notes, or Apple Books on your iPad/tablet.<br>
                        <strong>Print:</strong> Print in standard A4 format (single or double-sided) on 80–100 GSM paper and bind with a simple spiral coil at your local print shop.</p>
                    </div>
                </div>

                <div class="principle-item">
                    <div class="p-icon">04</div>
                    <div class="p-text">
                        <h4>The 7-Minute Sunday Evening Ritual</h4>
                        <p>Spend just 7 quiet minutes every Sunday evening with a warm cup of chai or herbal tea. Review your weekly priorities and check your habit rhythm for the week ahead.</p>
                    </div>
                </div>
            </div>

            {render_chintu("🦉", "CHINTU'S FIRST RULE OF SURVIVAL", "If you miss 3 days or write with messy handwriting, please DO NOT tear the page out like you did in your school notebook! We don't do drama here in 2027. Just turn the page and keep moving.")}

            <div class="pledge-box">
                <h4>My 2027 Journaling Pledge</h4>
                <p>I commit to showing up with honesty, patience, and kindness toward myself throughout 2027.</p>
                <div class="sign-line">
                    <span>Signature: <input type="text" class="inline-input" placeholder="Sign your name here"></span>
                    <span>Date: <input type="text" class="inline-input" placeholder="DD / MM / YYYY"></span>
                </div>
            </div>
        </div>
        <div class="page-footer">Page 5 of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_section_divider(num, title_raw, raw, section):
    # Extract subtitle and quote
    sub = ""
    quote = ""
    for line in raw.split('\n'):
        if line.startswith('* **Subtitle:**'):
            sub = line.replace('* **Subtitle:**', '').strip()
        elif 'Anchoring Quote:' in line:
            quote = line.split('Anchoring Quote:')[1].replace('*', '').strip()

    roman_map = {6: "SECTION 01", 12: "SECTION 02", 20: "SECTION 03", 43: "SECTION 05"}
    roman = roman_map.get(num, f"SECTION {num}")

    return f"""
    <div class="page divider-page" id="page-{num}">
        <div class="divider-frame">
            <div class="divider-badge">{roman}</div>
            <h1 class="divider-title">{html.escape(title_raw.replace('SECTION', '').strip())}</h1>
            <div class="gold-flourish">✦ ✦ ✦</div>
            <h3 class="divider-subtitle">{html.escape(sub)}</h3>
            <div class="divider-quote-box">
                <p class="divider-quote">{html.escape(quote)}</p>
            </div>
            <div class="botanical-accent">🌿 🕊️ 🌿</div>
        </div>
        <div class="page-footer">Page {num} of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_wheel_of_life(raw, num, section):
    spheres = [
        ("Career & Professional Learning", "1. Growth, projects, appraisals"),
        ("Financial Security & Savings (₹)", "2. Emergency fund, SIPs, debts"),
        ("Physical Health & Vitality", "3. Movement, protein, sleep, energy"),
        ("Mental & Emotional Peace", "4. Stress management, mindfulness"),
        ("Family & Home Environment", "5. Warmth, boundaries, relationships"),
        ("Friendships & Community", "6. Genuine bonds, mutual support"),
        ("Creativity & Personal Hobbies", "7. Making, writing, learning for joy"),
        ("Personal Freedom & Joy", "8. Leisure, autonomy, laughing often")
    ]
    sphere_rows = ""
    for idx, (sp, desc) in enumerate(spheres, 1):
        sphere_rows += f"""
        <div class="wheel-row">
            <div class="wheel-label"><strong>{idx}. {sp}</strong><br><small>{desc}</small></div>
            <div class="wheel-scale">
                {"".join([f'<label class="radio-dot"><input type="radio" name="sp_{idx}" value="{v}"><span>{v}</span></label>' for v in range(1, 11)])}
            </div>
            <div class="wheel-score"><input type="text" class="score-input" placeholder="/10"></div>
        </div>
        """

    return f"""
    <div class="page doc-page" id="page-{num}">
        <div class="page-header">
            <span class="header-section">{section}</span>
            <span class="header-num">{num:02d}</span>
        </div>
        <div class="content-box">
            <div class="chapter-tag">LIFE BALANCE AUDIT</div>
            <h2 class="page-title">The 8-Spoke Balance Wheel</h2>
            <p class="section-intro">Rate your current satisfaction in each life dimension from 1 (severely neglected) to 10 (thriving). Be radically honest.</p>
            <div class="accent-line"></div>

            <div class="wheel-table">
                {sphere_rows}
            </div>

            <div class="synthesis-card">
                <h4>🎯 The Keystone Dimension</h4>
                <p>Looking at your scores above, which <strong>single area</strong>—if intentionally nurtured and improved in 2027—will have the greatest positive ripple effect across all other dimensions?</p>
                <textarea class="ruled-textarea" rows="3" placeholder="Write the one life area and why it is your keystone..."></textarea>
            </div>
        </div>
        <div class="page-footer">Page {num} of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_vision_board(raw, num, section):
    return f"""
    <div class="page doc-page" id="page-{num}">
        <div class="page-header">
            <span class="header-section">{section}</span>
            <span class="header-num">{num:02d}</span>
        </div>
        <div class="content-box">
            <div class="chapter-tag">VISUAL INTENTIONS</div>
            <h2 class="page-title">My 2027 Aesthetic Vision Board</h2>
            <p class="section-intro">Paste printed images, stickers, quotes, or draw sketches representing how you want your 2027 to feel.</p>
            <div class="accent-line"></div>

            <div class="vision-grid">
                <div class="vision-box bg-cream-border">
                    <div class="v-header">🌿 Space & Living Environment</div>
                    <div class="v-canvas" contenteditable="true">
                        <span class="placeholder-text">[ Paste imagery, write keywords, or sketch: Clean room, balcony plants, quiet desk ]</span>
                    </div>
                </div>
                <div class="vision-box bg-rose-border">
                    <div class="v-header">🌸 Body, Stamina & Energy</div>
                    <div class="v-canvas" contenteditable="true">
                        <span class="placeholder-text">[ Paste imagery or write: 8k steps, wholesome Indian meals, rested eyes, morning glow ]</span>
                    </div>
                </div>
                <div class="vision-box bg-lavender-border">
                    <div class="v-header">📚 Learning, Craft & Career</div>
                    <div class="v-canvas" contenteditable="true">
                        <span class="placeholder-text">[ Paste imagery or write: Books read, deep work sessions, certificates, proud projects ]</span>
                    </div>
                </div>
                <div class="vision-box bg-gold-border">
                    <div class="v-header">💰 Financial Security & Peace (₹)</div>
                    <div class="v-canvas" contenteditable="true">
                        <span class="placeholder-text">[ Paste imagery or write: Steady SIPs, zero debt anxiety, emergency buffer, thoughtful spends ]</span>
                    </div>
                </div>
            </div>
            
            <div class="vision-footer-note">
                <em>"The pictures you focus on become the quiet soundtrack of your daily choices."</em>
            </div>
        </div>
        <div class="page-footer">Page {num} of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_financial_page(raw, num, section):
    return f"""
    <div class="page doc-page" id="page-{num}">
        <div class="page-header">
            <span class="header-section">{section}</span>
            <span class="header-num">{num:02d}</span>
        </div>
        <div class="content-box">
            <div class="chapter-tag">FINANCIAL AUTONOMY</div>
            <h2 class="page-title">Financial Freedom & Savings Planner (₹)</h2>
            <p class="section-intro">Anchor your financial confidence using the balanced 50/30/20 framework adapted for Indian households.</p>
            <div class="accent-line"></div>

            <div class="targets-strip">
                <div class="target-card">
                    <span class="t-title">Monthly Net Income</span>
                    <div class="t-val">₹ <input type="text" class="money-input" placeholder="50,000"></div>
                </div>
                <div class="target-card">
                    <span class="t-title">2027 Annual Savings Target</span>
                    <div class="t-val">₹ <input type="text" class="money-input" placeholder="1,50,000"></div>
                </div>
                <div class="target-card">
                    <span class="t-title">6-Month Emergency Buffer</span>
                    <div class="t-val">₹ <input type="text" class="money-input" placeholder="1,80,000"></div>
                </div>
            </div>

            <div class="model-503020">
                <div class="model-col col-needs">
                    <div class="m-head">
                        <h4>50% Essentials (Needs)</h4>
                        <span class="m-amt">Target: ₹ <input type="text" class="mini-amt" placeholder="25,000"></span>
                    </div>
                    <ul class="m-list">
                        <li>Rent / Home EMI</li>
                        <li>Groceries, Milk & Vegetables</li>
                        <li>Electricity, WiFi & Phone Bills</li>
                        <li>Metro / Fuel / Commute</li>
                        <li>Parents' Medical & Medications</li>
                    </ul>
                </div>

                <div class="model-col col-wants">
                    <div class="m-head">
                        <h4>30% Lifestyle (Wants)</h4>
                        <span class="m-amt">Target: ₹ <input type="text" class="mini-amt" placeholder="15,000"></span>
                    </div>
                    <ul class="m-list">
                        <li>Dining Out / Swiggy / Zomato</li>
                        <li>Shopping & Festive Apparel</li>
                        <li>Cinema, Weekend Outings & Cafes</li>
                        <li>Hobbies & Short Getaways</li>
                        <li>Subscriptions (OTT, Gym, Apps)</li>
                    </ul>
                </div>

                <div class="model-col col-wealth">
                    <div class="m-head">
                        <h4>20% Wealth & Savings</h4>
                        <span class="m-amt">Target: ₹ <input type="text" class="mini-amt" placeholder="10,000"></span>
                    </div>
                    <ul class="m-list">
                        <li>Monthly Index Fund SIPs</li>
                        <li>Emergency Fund Top-up (FD/Liquid)</li>
                        <li>PPF / EPF Contributions</li>
                        <li>Pure Health & Term Insurance</li>
                        <li>High-Interest Debt Prepayment</li>
                    </ul>
                </div>
            </div>

            <div class="impulse-rule-box">
                <h4>🛑 The 48-Hour Impulse Cooling Rule</h4>
                <p>For any unplanned non-essential purchase above <strong>₹1,000</strong>, I will enforce a strict 48-hour cooling-off pause before clicking "Buy Now". If I still genuinely need it after 48 hours, I will buy it guilt-free from my 30% Lifestyle budget.</p>
            </div>

            {render_chintu("💸", "CHINTU'S MIDNIGHT WALLET ALERT", "🚨 That 1:30 AM Blinkit cart with 1 ice cream bar, chips, and ₹35 late-night delivery charge is NOT a mental health investment. Step away from the UPI PIN!")}
        </div>
        <div class="page-footer">Page {num} of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_habit_tracker(raw, num, section):
    days_headers = "".join([f"<th>{d}</th>" for d in range(1, 32)])
    def make_habit_row(habit_name, sub):
        boxes = "".join([f'<td><input type="checkbox" class="h-chk"></td>' for _ in range(31)])
        return f"""
        <tr>
            <td class="habit-name-cell">
                <input type="text" class="habit-title-input" value="{habit_name}"><br>
                <small>{sub}</small>
            </td>
            {boxes}
            <td class="tally-cell"><input type="text" class="tally-input" placeholder="/31"></td>
        </tr>
        """

    return f"""
    <div class="page doc-page" id="page-{num}">
        <div class="page-header">
            <span class="header-section">{section}</span>
            <span class="header-num">{num:02d}</span>
        </div>
        <div class="content-box">
            <div class="chapter-tag">DAILY CONSISTENCY ENGINE</div>
            <h2 class="page-title">365-Day Micro-Habit Tracker Master</h2>
            <p class="section-intro">Track no more than 4 core anchor habits. Research proves tracking more than 4 leads to habit fatigue and collapse.</p>
            <div class="accent-line"></div>

            <div class="tracker-legend">
                <span>Month: <input type="text" class="inline-input-sm" placeholder="e.g. January"></span>
                <span>Anchor Goal: 80% Consistency (25+ days ticked)</span>
            </div>

            <div class="habit-table-wrapper">
                <table class="habit-table">
                    <thead>
                        <tr>
                            <th class="habit-col-hdr">Core Anchor Habit</th>
                            {days_headers}
                            <th>Tally</th>
                        </tr>
                    </thead>
                    <tbody>
                        {make_habit_row("1. Physical Vitality", "8k Steps or 30m Workout")}
                        {make_habit_row("2. Career / Skill Moat", "45-90m Deep Focus / Study")}
                        {make_habit_row("3. Mental Well-being", "Balcony Sunlight + No Morning Phone")}
                        {make_habit_row("4. Financial Discipline", "Logged Daily ₹ Spends & Zero Impulse")}
                    </tbody>
                </table>
            </div>

            <div class="habit-rule-note">
                <p>💡 <strong>The "Never Miss Twice" Principle:</strong> Missing one day is life happening. Missing two days is the start of a new, unwanted habit. If you miss yesterday, prioritize today above everything else.</p>
            </div>

            {render_chintu("🏋️‍♂️", "CHINTU'S HABIT MATH", "Doing 5 pushups or reading 2 pages = 100% win. Watching 3 hours of gym motivation reels while eating samosas = 0% win. Keep it simple and tick the box!")}
        </div>
        <div class="page-footer">Page {num} of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_recovery_plan(raw, num, section):
    return f"""
    <div class="page doc-page" id="page-{num}">
        <div class="page-header">
            <span class="header-section">{section}</span>
            <span class="header-num">{num:02d}</span>
        </div>
        <div class="content-box">
            <div class="chapter-tag">EMERGENCY PROTOCOL</div>
            <h2 class="page-title serif-italic">The "Bad-Day Recovery Plan"</h2>
            <p class="section-intro">Read this page whenever you miss days, feel overwhelmed, or want to quit.</p>
            <div class="accent-line"></div>

            <div class="recovery-banner">
                <h3>Take a breath. You are not starting from zero; you are starting from experience.</h3>
                <p>"You missed four days. Or maybe two weeks. You scrolled mindlessly for hours, ordered junk food, and didn't touch your planner. Guess what? You are a human being, not an algorithm. This journal keeps no penalty points. Welcome home."</p>
            </div>

            <div class="recovery-steps">
                <div class="rec-step">
                    <span class="rec-num">1</span>
                    <div class="rec-body">
                        <h4>Rehydrate Your Body</h4>
                        <p>Go to the kitchen right now and drink a tall glass of cool water. Wash your face with cold water to gently down-regulate your nervous system.</p>
                    </div>
                </div>

                <div class="rec-step">
                    <span class="rec-num">2</span>
                    <div class="rec-body">
                        <h4>Clear Just ONE Flat Surface</h4>
                        <p>Spend exactly 3 minutes clearing your study desk, making your bed, or putting clothes away. Physical order signals mental calm.</p>
                    </div>
                </div>

                <div class="rec-step">
                    <span class="rec-num">3</span>
                    <div class="rec-body">
                        <h4>Complete ONE 10-Minute Micro-Task</h4>
                        <p>Do not attempt to catch up on everything today. Open one chapter, answer one email, or walk for 10 minutes around your terrace.</p>
                    </div>
                </div>

                <div class="rec-step">
                    <span class="rec-num">4</span>
                    <div class="rec-body">
                        <h4>Forgive Yourself in Ink</h4>
                        <p>Write your gentle reset declaration below:</p>
                        <div class="forgive-box">
                            <em>"I am allowed to have messy days. My dedication resumes right now, without shame or guilt."</em>
                        </div>
                    </div>
                </div>
            </div>

            {render_chintu("☕", "CHINTU'S REALITY HUG", "Had a bad day? Koi baat nahi, even ISRO rockets recalculate trajectory! Drink water, take a warm shower, and sleep early. Tomorrow is a brand new sunrise.")}
        </div>
        <div class="page-footer">Page {num} of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_monthly_spread(num, title_raw, raw, section):
    # Extract month name
    month_match = re.search(r'(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)\s+2027', raw, re.IGNORECASE)
    month_name = month_match.group(1).title() if month_match else f"Month {num-30}"
    m_icon, m_tag, m_tip = get_chintu_month_tip(month_name)

    intention = ""
    for line in raw.split('\n'):
        if 'Monthly Intention:' in line:
            intention = line.split('Monthly Intention:')[1].replace('*', '').strip()

    return f"""
    <div class="page doc-page" id="page-{num}">
        <div class="page-header">
            <span class="header-section">2027 MONTHLY JOURNEY</span>
            <span class="header-num">{num:02d}</span>
        </div>
        <div class="content-box">
            <div class="month-hero-strip">
                <div>
                    <span class="chapter-tag">2027 DATED SPREAD</span>
                    <h2 class="month-title">{month_name} 2027</h2>
                </div>
                <div class="month-intent-card">
                    <span class="m-sub">MONTHLY INTENTION</span>
                    <p><em>"{html.escape(intention)}"</em></p>
                </div>
            </div>
            <div class="accent-line"></div>

            <div class="monthly-grid-layout">
                <div class="m-top-priorities">
                    <h4>🎯 Top 3 Core Priorities</h4>
                    <div class="p-input-row"><span>1.</span> <input type="text" class="ruled-line-input" placeholder="Primary milestone to accomplish this month"></div>
                    <div class="p-input-row"><span>2.</span> <input type="text" class="ruled-line-input" placeholder="Secondary priority to protect"></div>
                    <div class="p-input-row"><span>3.</span> <input type="text" class="ruled-line-input" placeholder="Personal habit or well-being goal"></div>
                </div>

                <div class="m-key-dates">
                    <h4>📅 Key Dates & Commitments</h4>
                    <textarea class="ruled-textarea-sm" rows="3" placeholder="Exams, salary credit day, family functions, fee deadlines, festivals..."></textarea>
                </div>
            </div>

            <div class="m-pillars-container">
                <div class="m-pillar-box bg-sage-light">
                    <h5>💰 Financial Pillar</h5>
                    <p>Monthly Savings Goal: ₹ <input type="text" class="mini-input" placeholder="10,000"></p>
                    <p>Impulse Spend Limit: <input type="text" class="mini-input" placeholder="Under 3 orders"></p>
                </div>
                <div class="m-pillar-box bg-rose-light">
                    <h5>🌸 Vitality & Health</h5>
                    <p>Movement Goal: <input type="text" class="mini-input" placeholder="8,000 steps daily"></p>
                    <p>Sleep Routine: <input type="text" class="mini-input" placeholder="Lights out by 11 PM"></p>
                </div>
                <div class="m-pillar-box bg-lavender-light">
                    <h5>📚 Career & Learning</h5>
                    <p>Core Sprint: <input type="text" class="mini-input" placeholder="Complete Module / Project"></p>
                    <p>Weekly Moat: <input type="text" class="mini-input" placeholder="3 hours deep work"></p>
                </div>
            </div>

            <div class="m-micro-steps">
                <h4>⚡ Month-Opening Micro Actions</h4>
                <div class="chk-item"><input type="checkbox"> <span>Automate SIP & savings transfer immediately on salary credit day</span></div>
                <div class="chk-item"><input type="checkbox"> <span>Set up calendar and protect one full rest evening every week</span></div>
                <div class="chk-item"><input type="checkbox"> <span>Review previous month's wins and set clean intentions</span></div>
            </div>

            {render_chintu(m_icon, m_tag, m_tip)}

            <div class="m-reflection-box">
                <h4>🌿 End-of-Month Reflection</h4>
                <p>What worked with ease this month? What needs a gentle realignment?</p>
                <textarea class="ruled-textarea" rows="2" placeholder="Write your quiet reflection before opening the next month..."></textarea>
            </div>
        </div>
        <div class="page-footer">Page {num} of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_jar_of_wins(raw, num, section):
    bubbles = "".join([f"""
    <div class="win-bubble">
        <span class="bubble-num">#{i}</span>
        <input type="text" class="win-date" placeholder="DD/MM">
        <textarea class="win-text" rows="2" placeholder="A victory or quiet blessing I am proud of..."></textarea>
    </div>
    """ for i in range(1, 13)])

    return f"""
    <div class="page doc-page" id="page-{num}">
        <div class="page-header">
            <span class="header-section">{section}</span>
            <span class="header-num">{num:02d}</span>
        </div>
        <div class="content-box">
            <div class="chapter-tag">RESILIENCE & JOY ARCHIVE</div>
            <h2 class="page-title">The Jar of Micro-Wins (12 Victory Badges)</h2>
            <p class="section-intro">Throughout 2027, log 12 moments that made you proud—especially the quiet ones nobody clapped for.</p>
            <div class="accent-line"></div>

            <div class="jar-grid">
                {bubbles}
            </div>
            
            <div class="jar-quote">
                <em>"We do not remember days; we remember moments of courage and quiet grace."</em>
            </div>

            {render_chintu("🏆", "CHINTU'S MICRO-WIN CHECK", "Did you drink 2 liters of water? Did you say a polite NO to extra unpaid weekend work? Did you not text your ex? Put it in the jar—that's a certified victory!")}
        </div>
        <div class="page-footer">Page {num} of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_closing(raw, num, section):
    return f"""
    <div class="page doc-page" id="page-{num}">
        <div class="page-header">
            <span class="header-section">{section}</span>
            <span class="header-num">{num:02d}</span>
        </div>
        <div class="content-box">
            <div class="chapter-tag">FINAL BLESSING & EMPOWERMENT</div>
            <h2 class="page-title serif-italic">You Did It, and You Are Ready.</h2>
            <div class="accent-line"></div>

            <div class="letter-body">
                <p class="lead-quote">"Take a moment to close your eyes, place your hand over your heart, and feel the steady rhythm of your life."</p>

                <p>You have journeyed through 365 days of growth, uncertainty, joyful discoveries, quiet tears, unexpected setbacks, and astonishing resilience. Look through the pages of this journal—not to count what you didn't finish, but to witness how many times you showed up for yourself when it would have been easier to give up.</p>

                <p>You dared to define what truly matters. You held respectful boundaries when pressure was high. You saved with intention. You moved your body with appreciation. And most importantly, you learned to forgive yourself when days were messy.</p>

                <p>You no longer need to chase a life that merely looks impressive on paper. You have built a life that feels authentic, grounded, peaceful, and deeply right for you.</p>

                <p>Carry this quiet power with you into every room you enter. You are prepared, you are grounded, and you are ready.</p>

                <p class="warm-closing">With boundless belief in your path,</p>
                <div class="author-sign-wrap">
                    <div class="author-sign">Kanchan Pathare</div>
                    <div class="author-title">Author & Independent Creator • India</div>
                </div>
            </div>

            <div class="closing-emblem">
                <span>✦ 🕊️ ✦</span>
            </div>

            {render_chintu("🎓", "CHINTU'S GRADUATION NOTE", "Look at you! You actually stayed true to yourself through 2027. I'm proud of you, buddy. Now treat yourself to extra hot ginger chai and a well-earned celebration!")}
        </div>
        <div class="page-footer">Page {num} of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_back_cover(raw):
    return """
    <div class="page cover-page back-cover-page" id="page-52">
        <div class="botanical-corner top-left">┌</div>
        <div class="botanical-corner top-right">┐</div>
        <div class="botanical-corner bottom-left">└</div>
        <div class="botanical-corner bottom-right">┘</div>
        <div class="cover-inner-border">
            <div class="gold-flourish">━━━━━ ✦ ━━━━━</div>
            <div class="back-quote-box">
                <blockquote class="back-quote">
                    "May you always remember: You do not have to be remarkable every single day. Showing up with a gentle, honest heart is always enough."
                </blockquote>
            </div>
            
            <div class="back-author-note">
                <p>Designed with deep love for Indian dreamers, doers, and seekers by <strong>Kanchan Pathare</strong>.</p>
            </div>

            <div class="back-ecosystem-card">
                <h4>CONTINUE YOUR TRANSFORMATION</h4>
                <p>Explore the companion habit mastery book:<br>
                <strong>The Girl Who Always Started Tomorrow: Mira's 30-Day Habit Adventure</strong></p>
                <div class="back-social-links">
                    <span>📸 Instagram: @kanchanpathare.author</span>
                    <span>🌐 SuperProfile: superprofile.bio/kanchanpathare</span>
                </div>
            </div>
            
            <div class="back-isbn-box">
                <span>DEAR 2027, I'M READY. • DIGITAL & PRINTABLE EDITION</span>
                <span>© 2026–2027 KANCHAN PATHARE • ALL RIGHTS RESERVED</span>
            </div>
        </div>
        <div class="page-footer">Page 52 of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

def render_standard_worksheet(num, title_raw, raw, section):
    # Parse items in worksheet
    items = []
    lines = raw.split('\n')
    clean_title = title_raw.replace('##', '').strip()
    
    # Extract guidance quote or instructions
    instructions = ""
    for line in lines:
        if line.startswith('* **Instructions:**'):
            instructions = line.replace('* **Instructions:**', '').strip()
        elif line.startswith('* **Philosophy:**'):
            instructions = line.replace('* **Philosophy:**', '').strip()

    # Body elements
    elements_html = []
    for line in lines[1:]:
        line = line.strip()
        if not line or line.startswith('* **Instructions:**') or line.startswith('* **Philosophy:**'):
            continue
        
        if line.startswith('* **') and ':**' in line:
            heading = line.split(':**')[0].replace('* **', '').strip()
            rest = line.split(':**')[1].strip()
            elements_html.append(f"""
            <div class="worksheet-section">
                <h4 class="ws-heading">{html.escape(heading)}</h4>
                {f'<p class="ws-desc">{html.escape(rest)}</p>' if rest else ''}
                <textarea class="ruled-textarea" rows="3" placeholder="Write your reflection here..."></textarea>
            </div>
            """)
        elif line.startswith('* [ ]'):
            text = line.replace('* [ ]', '').strip()
            elements_html.append(f"""
            <div class="chk-item">
                <input type="checkbox">
                <span>{html.escape(text)}</span>
            </div>
            """)
        elif line.startswith('*') or line.startswith('1.') or line.startswith('2.') or line.startswith('3.') or line.startswith('4.'):
            text = line.lstrip('*123456789. ').strip()
            elements_html.append(f"""
            <div class="prompt-item">
                <p class="prompt-text">✦ {html.escape(text)}</p>
                <input type="text" class="ruled-line-input" placeholder="Your thoughtful response...">
            </div>
            """)

    extra_chintu = ""
    if num == 7:
        extra_chintu = render_chintu("🧐", "CHINTU'S HONEST OBSERVATION", "Admit it: 70% of your 2026 screentime was street food reels and 2:00 AM videos of people cleaning rugs. Forgive yourself, but close Instagram earlier in 2027!")
    elif num == 17:
        extra_chintu = render_chintu("🛡️", "CHINTU'S BOUNDARY SHIELD", "When relatives ask 'When is your wedding?' or 'What is your CTC package?', smile politely and say: 'Aunty, my astrologer advised me to keep financials confidential until Sensex reaches 1,00,000.'")
    elif num == 21:
        extra_chintu = render_chintu("🍳", "CHINTU'S PROTEIN REALITY", "Chai and 2 Parle-G biscuits do NOT count as a high-protein breakfast! Eat eggs, paneer, sprouts, or tofu before your muscles submit a formal resignation letter.")
    elif num == 26:
        extra_chintu = render_chintu("📵", "CHINTU'S BEDTIME SURVIVAL", "Putting your phone on charge outside the bedroom feels like emotional heartbreak on Night 1. But by Night 3, you will sleep like a baby Kumbhakarna.")

    return f"""
    <div class="page doc-page" id="page-{num}">
        <div class="page-header">
            <span class="header-section">{section}</span>
            <span class="header-num">{num:02d}</span>
        </div>
        <div class="content-box">
            <div class="chapter-tag">GUIDED WORKSHEET</div>
            <h2 class="page-title">{html.escape(clean_title)}</h2>
            {f'<p class="section-intro">{html.escape(instructions)}</p>' if instructions else ''}
            <div class="accent-line"></div>

            {extra_chintu}

            <div class="worksheet-body">
                {"".join(elements_html)}
            </div>
        </div>
        <div class="page-footer">Page {num} of 52 • Dear 2027, I'm Ready.</div>
    </div>
    """

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dear 2027, I'm Ready. — Complete 52-Page Master Journal & Planner</title>
    <!-- Google Fonts for Modern Minimalist Luxury & Editorial Clarity -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&family=Lora:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        :root {{
            --base-cream: #F8F9FA;         /* Nordic Crisp Canvas */
            --cream-card: #EEF1F4;         /* Soft Mist Card Fill */
            --sage-green: #2B323B;         /* Nordic Charcoal Slate */
            --sage-light: #E2E6EC;         /* Pale Mist Slate */
            --dusty-rose: #4A5568;         /* Cool Steel Slate */
            --rose-light: #ECEEF2;         /* Subtle Steel Tint */
            --soft-lavender: #64748B;      /* Slate Grey */
            --lavender-light: #F0F2F6;     /* Light Cloud */
            --muted-gold: #1A1E24;         /* Architectural Ink Black */
            --gold-light: #E8EBEF;         /* Subtle Stone Fill */
            --espresso-dark: #0F1216;      /* Pure High-Contrast Modern Ink */
            --border-subtle: rgba(15, 18, 22, 0.12); /* Ultra-fine hairline rules */
            --border-dotted: rgba(15, 18, 22, 0.24);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: #16181D;
            font-family: 'Plus Jakarta Sans', 'Montserrat', sans-serif;
            color: var(--espresso-dark);
            line-height: 1.5;
            -webkit-print-color-adjust: exact !important;
            print-color-adjust: exact !important;
        }}

        /* Floating Interactive Action Toolbar */
        .no-print-toolbar {{
            position: fixed;
            top: 16px;
            right: 20px;
            z-index: 9999;
            background: rgba(248, 249, 250, 0.96);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(15, 18, 22, 0.2);
            border-radius: 8px;
            padding: 8px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        }}

        .toolbar-btn {{
            background: var(--espresso-dark);
            color: #FFFFFF;
            border: none;
            padding: 8px 16px;
            border-radius: 4px;
            font-size: 12.5px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .toolbar-btn:hover {{
            background: #2D3239;
            transform: translateY(-1px);
        }}
        .toolbar-btn.gold {{
            background: #2B323B;
            color: #FFFFFF;
        }}
        .toolbar-title {{
            font-size: 12.5px;
            font-weight: 700;
            color: var(--espresso-dark);
            letter-spacing: 0.5px;
        }}

        /* Document Pages Container */
        .journal-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 40px 0;
            gap: 30px;
        }}

        /* Standard A4 Page Dimensions */
        .page {{
            width: 210mm;
            min-height: 297mm;
            max-height: 297mm;
            background-color: var(--base-cream);
            position: relative;
            box-shadow: 0 12px 36px rgba(0,0,0,0.25);
            padding: 18mm 20mm 16mm 22mm; /* 22mm binding edge left */
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden;
            page-break-after: always;
            page-break-inside: avoid;
        }}

        /* Running Page Header & Footer */
        .page-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 10px;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: rgba(73, 53, 46, 0.6);
            border-bottom: 0.5px solid var(--border-subtle);
            padding-bottom: 6px;
            margin-bottom: 12px;
        }}
        .header-num {{
            font-weight: 700;
            font-family: 'Montserrat', sans-serif;
            color: var(--muted-gold);
        }}
        .page-footer {{
            text-align: center;
            font-size: 9.5px;
            letter-spacing: 1px;
            color: rgba(73, 53, 46, 0.5);
            border-top: 0.5px solid var(--border-subtle);
            padding-top: 8px;
            margin-top: auto;
        }}

        /* Typography Styles */
        h1, h2, h3, .serif-italic {{
            font-family: 'Space Grotesk', 'Plus Jakarta Sans', sans-serif;
            color: var(--espresso-dark);
            letter-spacing: -0.3px;
        }}
        .cover-title {{
            font-family: 'Space Grotesk', 'Plus Jakarta Sans', sans-serif;
            font-size: 42px;
            line-height: 1.1;
            text-align: center;
            font-weight: 700;
            letter-spacing: -1px;
            text-transform: uppercase;
        }}
        .page-title {{
            font-size: 24px;
            font-weight: 700;
            line-height: 1.2;
            letter-spacing: -0.5px;
            margin-bottom: 4px;
        }}
        .chapter-tag {{
            font-size: 9.5px;
            letter-spacing: 2.5px;
            font-weight: 700;
            color: var(--sage-green);
            text-transform: uppercase;
            margin-bottom: 3px;
        }}
        .section-intro {{
            font-size: 11.5px;
            color: rgba(15, 18, 22, 0.75);
            margin-bottom: 10px;
            font-style: italic;
        }}
        .accent-line {{
            width: 36px;
            height: 2px;
            background: var(--espresso-dark);
            margin-bottom: 14px;
            border-radius: 1px;
        }}

        /* Minimalist Corner Crosshairs */
        .botanical-corner {{
            position: absolute;
            font-family: monospace;
            font-size: 18px;
            font-weight: 300;
            color: var(--espresso-dark);
            opacity: 0.55;
        }}
        .top-left {{ top: 16px; left: 16px; }}
        .top-right {{ top: 16px; right: 16px; }}
        .bottom-left {{ bottom: 16px; left: 16px; }}
        .bottom-right {{ bottom: 16px; right: 16px; }}

        /* Front Cover Specifics */
        .cover-page {{
            padding: 16mm;
            text-align: center;
            justify-content: center;
        }}
        .cover-inner-border {{
            border: 1.5px solid var(--espresso-dark);
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 30px;
            position: relative;
        }}
        .cover-inner-border::after {{
            content: '';
            position: absolute;
            top: 5px; left: 5px; right: 5px; bottom: 5px;
            border: 0.5px solid rgba(15, 18, 22, 0.25);
            pointer-events: none;
        }}
        .cover-tag {{
            font-size: 10px;
            letter-spacing: 3px;
            font-weight: 700;
            color: var(--sage-green);
            margin-bottom: 22px;
        }}
        .cover-subtitle {{
            font-size: 16px;
            font-weight: 600;
            margin-top: 14px;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: var(--dusty-rose);
        }}
        .cover-tagline {{
            font-size: 13px;
            font-style: italic;
            color: rgba(15, 18, 22, 0.8);
            max-width: 440px;
            margin: 18px 0;
            font-family: 'Lora', Georgia, serif;
        }}
        .gold-flourish {{
            color: var(--espresso-dark);
            font-size: 14px;
            letter-spacing: 6px;
            margin: 12px 0;
            opacity: 0.6;
        }}
        .cover-author-box {{
            margin-top: 25px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2px;
        }}
        .by-text {{
            font-size: 10px;
            letter-spacing: 4px;
            color: rgba(15, 18, 22, 0.5);
            font-weight: 600;
        }}
        .author-name {{
            font-family: 'Space Grotesk', 'Playfair Display', sans-serif;
            font-size: 22px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
        }}
        .cover-pills {{
            margin-top: 35px;
            display: flex;
            gap: 10px;
        }}
        .pill {{
            background: #FFFFFF;
            color: var(--espresso-dark);
            border: 1px solid var(--border-subtle);
            padding: 6px 14px;
            border-radius: 4px;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 0.8px;
            text-transform: uppercase;
        }}

        /* Section Divider Pages */
        .divider-page {{
            text-align: center;
            justify-content: center;
            padding: 25mm 20mm;
        }}
        .divider-frame {{
            border: 1.5px solid var(--espresso-dark);
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 30px;
            background: #FFFFFF;
        }}
        .divider-badge {{
            font-size: 10.5px;
            letter-spacing: 4px;
            font-weight: 700;
            color: var(--dusty-rose);
            margin-bottom: 15px;
            text-transform: uppercase;
        }}
        .divider-title {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 36px;
            line-height: 1.15;
            margin-bottom: 12px;
            letter-spacing: -1px;
            text-transform: uppercase;
        }}
        .divider-subtitle {{
            font-size: 15px;
            font-weight: 400;
            color: rgba(15, 18, 22, 0.8);
            margin-bottom: 25px;
            font-style: italic;
        }}
        .divider-quote-box {{
            max-width: 440px;
            border-top: 1px solid var(--border-subtle);
            border-bottom: 1px solid var(--border-subtle);
            padding: 16px 20px;
            margin: 20px 0;
        }}
        .divider-quote {{
            font-family: 'Lora', Georgia, serif;
            font-size: 13.5px;
            font-style: italic;
            line-height: 1.6;
        }}
        .botanical-accent {{
            margin-top: 20px;
            font-size: 14px;
            letter-spacing: 8px;
            opacity: 0.5;
        }}

        /* Chintu Character Widget - Modern Minimalist Slate */
        .chintu-card {{
            display: flex;
            align-items: center;
            gap: 12px;
            background: #FFFFFF;
            border: 1px solid var(--border-subtle);
            border-left: 3.5px solid var(--sage-green);
            border-radius: 4px;
            padding: 8px 12px;
            margin: 10px 0;
            box-shadow: 0 1px 4px rgba(0,0,0,0.03);
        }}
        .chintu-avatar {{
            display: flex;
            flex-direction: column;
            align-items: center;
            min-width: 44px;
            text-align: center;
            border-right: 0.5px solid var(--border-subtle);
            padding-right: 10px;
        }}
        .chintu-icon {{
            font-size: 22px;
            line-height: 1;
        }}
        .chintu-name {{
            font-size: 7.5px;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: var(--espresso-dark);
            margin-top: 2px;
        }}
        .chintu-bubble {{
            flex: 1;
        }}
        .chintu-title {{
            font-size: 8px;
            font-weight: 800;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            color: var(--dusty-rose);
            display: block;
            margin-bottom: 2px;
        }}
        .chintu-text {{
            font-size: 10px;
            line-height: 1.35;
            color: var(--espresso-dark);
            font-style: italic;
        }}

        /* Cards & Content Layout */
        .card {{
            border-radius: 8px;
            padding: 12px 16px;
            margin-bottom: 12px;
            border: 0.5px solid var(--border-subtle);
        }}
        .bg-cream {{ background: var(--cream-card); }}
        .bg-rose {{ background: var(--rose-light); border-color: var(--dusty-rose); }}
        .bg-lavender {{ background: var(--lavender-light); border-color: var(--soft-lavender); }}
        .bg-sage {{ background: var(--sage-light); border-color: var(--sage-green); }}

        .card h3, .card h4 {{
            font-size: 13.5px;
            font-weight: 700;
            margin-bottom: 4px;
        }}
        .card p {{
            font-size: 11px;
            line-height: 1.5;
            color: rgba(73, 53, 46, 0.9);
        }}

        /* Form Inputs & Interactive Lines */
        input[type="text"], textarea {{
            background: transparent;
            border: none;
            color: var(--espresso-dark);
            font-family: 'Montserrat', sans-serif;
            font-size: 12px;
            outline: none;
            width: 100%;
        }}
        .ruled-line-input {{
            border-bottom: 0.5px dashed var(--border-dotted);
            padding: 4px 2px;
            margin-bottom: 6px;
            font-size: 12px;
        }}
        .ruled-line-input:focus {{
            border-bottom: 1px solid var(--muted-gold);
            background: rgba(214, 181, 109, 0.08);
        }}
        .ruled-textarea {{
            border: none;
            background-image: repeating-linear-gradient(transparent, transparent 23px, var(--border-dotted) 24px);
            line-height: 24px;
            padding: 4px 4px;
            width: 100%;
            resize: none;
            font-size: 12px;
        }}
        .ruled-textarea:focus {{
            background-color: rgba(255, 255, 255, 0.4);
        }}
        .ruled-textarea-sm {{
            border: none;
            background-image: repeating-linear-gradient(transparent, transparent 20px, var(--border-dotted) 21px);
            line-height: 21px;
            padding: 2px 4px;
            width: 100%;
            resize: none;
            font-size: 11px;
        }}

        /* Checkbox styling */
        input[type="checkbox"] {{
            accent-color: var(--sage-green);
            width: 15px;
            height: 15px;
            cursor: pointer;
        }}
        .chk-item {{
            display: flex;
            align-items: flex-start;
            gap: 10px;
            margin-bottom: 8px;
            font-size: 11.5px;
            line-height: 1.4;
        }}

        /* TOC Styling */
        .toc-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 10px;
        }}
        .toc-card {{
            background: #FFFDF9;
            border: 0.5px solid var(--border-subtle);
            border-radius: 6px;
            padding: 10px 14px;
        }}
        .toc-badge {{
            display: inline-block;
            font-size: 9px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 10px;
            background: rgba(73, 53, 46, 0.1);
            margin-bottom: 4px;
        }}
        .toc-badge.sage {{ background: var(--sage-light); color: #3E5431; }}
        .toc-badge.rose {{ background: var(--rose-light); color: #8C404E; }}
        .toc-badge.lavender {{ background: var(--lavender-light); color: #534571; }}
        .toc-badge.gold {{ background: var(--gold-light); color: #7B5F23; }}
        .toc-card h4 {{
            font-size: 12.5px;
            font-weight: 700;
            margin-bottom: 4px;
        }}
        .toc-card ul {{
            list-style: none;
            font-size: 10.5px;
            line-height: 1.4;
        }}
        .p-num {{
            font-weight: 600;
            color: var(--muted-gold);
            margin-right: 4px;
        }}

        /* Author Welcome & Letter */
        .lead-quote {{
            font-family: 'Lora', Georgia, serif;
            font-size: 13.5px;
            font-style: italic;
            color: var(--espresso-dark);
            border-left: 2px solid var(--muted-gold);
            padding-left: 12px;
            margin-bottom: 12px;
        }}
        .letter-body p {{
            font-size: 11.5px;
            line-height: 1.6;
            margin-bottom: 10px;
            color: rgba(73, 53, 46, 0.95);
        }}
        .author-sign-wrap {{
            margin-top: 14px;
        }}
        .author-sign, .script-author {{
            font-family: 'Caveat', cursive;
            font-size: 28px;
            font-weight: 700;
            color: #38241D;
        }}
        .author-title {{
            font-size: 10px;
            color: rgba(73, 53, 46, 0.6);
            letter-spacing: 0.5px;
        }}

        /* Principle Cards */
        .principle-cards {{
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 14px;
        }}
        .principle-item {{
            display: flex;
            gap: 14px;
            background: #FFFDF9;
            border: 0.5px solid var(--border-subtle);
            border-radius: 6px;
            padding: 10px 14px;
            align-items: flex-start;
        }}
        .p-icon {{
            font-size: 16px;
            font-weight: 700;
            color: var(--muted-gold);
            font-family: 'Cormorant Garamond', Georgia, serif;
            min-width: 24px;
        }}
        .p-text h4 {{
            font-size: 12px;
            font-weight: 700;
            margin-bottom: 2px;
        }}
        .p-text p {{
            font-size: 10.5px;
            line-height: 1.45;
            color: rgba(73, 53, 46, 0.85);
        }}

        /* 8-Spoke Wheel of Life */
        .wheel-table {{
            display: flex;
            flex-direction: column;
            gap: 6px;
            margin-bottom: 12px;
        }}
        .wheel-row {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: #FFFDF9;
            border: 0.5px solid var(--border-subtle);
            border-radius: 6px;
            padding: 6px 12px;
        }}
        .wheel-label {{
            width: 210px;
            font-size: 11px;
            line-height: 1.25;
        }}
        .wheel-label small {{
            font-size: 9px;
            color: rgba(73, 53, 46, 0.6);
        }}
        .wheel-scale {{
            display: flex;
            gap: 5px;
        }}
        .radio-dot {{
            display: flex;
            flex-direction: column;
            align-items: center;
            font-size: 8.5px;
            cursor: pointer;
        }}
        .radio-dot input {{
            accent-color: var(--sage-green);
            width: 12px;
            height: 12px;
        }}
        .score-input {{
            width: 42px;
            text-align: center;
            font-weight: 700;
            font-size: 12px;
            border: 0.5px solid var(--muted-gold);
            border-radius: 4px;
            padding: 2px;
        }}
        .synthesis-card {{
            background: var(--cream-card);
            border: 0.5px solid var(--border-subtle);
            border-radius: 6px;
            padding: 10px 14px;
        }}
        .synthesis-card h4 {{
            font-size: 12px;
            margin-bottom: 4px;
        }}
        .synthesis-card p {{
            font-size: 10.5px;
            margin-bottom: 6px;
        }}

        /* Vision Board Canvas */
        .vision-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 170px 170px;
            gap: 12px;
            margin-bottom: 12px;
        }}
        .vision-box {{
            background: #FFFDF9;
            border-radius: 8px;
            padding: 12px;
            display: flex;
            flex-direction: column;
            border: 1px dashed var(--muted-gold);
        }}
        .bg-cream-border {{ border-color: var(--sage-green); background: rgba(168, 184, 154, 0.08); }}
        .bg-rose-border {{ border-color: var(--dusty-rose); background: rgba(232, 180, 188, 0.08); }}
        .bg-lavender-border {{ border-color: var(--soft-lavender); background: rgba(217, 208, 235, 0.08); }}
        .bg-gold-border {{ border-color: var(--muted-gold); background: rgba(214, 181, 109, 0.08); }}
        .v-header {{
            font-size: 11px;
            font-weight: 700;
            margin-bottom: 6px;
            border-bottom: 0.5px solid rgba(73, 53, 46, 0.15);
            padding-bottom: 4px;
        }}
        .v-canvas {{
            flex: 1;
            font-size: 11px;
            color: rgba(73, 53, 46, 0.5);
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 8px;
            outline: none;
        }}

        /* Financial 50/30/20 Page */
        .targets-strip {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 12px;
        }}
        .target-card {{
            background: #FFFDF9;
            border: 0.5px solid var(--border-subtle);
            border-radius: 6px;
            padding: 8px 12px;
            text-align: center;
        }}
        .t-title {{
            font-size: 9.5px;
            text-transform: uppercase;
            font-weight: 600;
            color: rgba(73, 53, 46, 0.7);
        }}
        .t-val {{
            font-size: 15px;
            font-weight: 700;
            color: var(--espresso-dark);
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 4px;
            margin-top: 2px;
        }}
        .money-input {{
            font-size: 14px;
            font-weight: 700;
            border-bottom: 0.5px solid var(--muted-gold);
            width: 100px;
            text-align: center;
        }}
        .model-503020 {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 12px;
        }}
        .model-col {{
            background: #FFFDF9;
            border-radius: 6px;
            padding: 10px 12px;
            border: 0.5px solid var(--border-subtle);
        }}
        .col-needs {{ border-top: 3px solid var(--sage-green); }}
        .col-wants {{ border-top: 3px solid var(--dusty-rose); }}
        .col-wealth {{ border-top: 3px solid var(--muted-gold); }}
        .m-head h4 {{
            font-size: 11px;
            font-weight: 700;
            margin-bottom: 2px;
        }}
        .m-amt {{
            font-size: 10px;
            color: rgba(73, 53, 46, 0.7);
            display: block;
            margin-bottom: 8px;
        }}
        .mini-amt {{
            width: 60px;
            font-size: 10.5px;
            font-weight: 600;
            border-bottom: 0.5px dashed var(--border-dotted);
        }}
        .m-list {{
            list-style: disc;
            padding-left: 14px;
            font-size: 9.5px;
            line-height: 1.5;
            color: rgba(73, 53, 46, 0.85);
        }}
        .impulse-rule-box {{
            background: var(--rose-light);
            border: 0.5px solid var(--dusty-rose);
            border-radius: 6px;
            padding: 10px 14px;
        }}
        .impulse-rule-box h4 {{
            font-size: 11.5px;
            margin-bottom: 3px;
        }}
        .impulse-rule-box p {{
            font-size: 10.5px;
            line-height: 1.45;
        }}

        /* Habit Tracker Master */
        .tracker-legend {{
            display: flex;
            justify-content: space-between;
            font-size: 11px;
            margin-bottom: 8px;
            font-weight: 600;
        }}
        .inline-input-sm {{
            width: 100px;
            border-bottom: 0.5px solid var(--muted-gold);
            font-size: 11px;
            font-weight: 700;
        }}
        .habit-table-wrapper {{
            overflow-x: auto;
            margin-bottom: 12px;
        }}
        .habit-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 9px;
            background: #FFFDF9;
        }}
        .habit-table th, .habit-table td {{
            border: 0.5px solid var(--border-subtle);
            text-align: center;
            padding: 4px 1px;
        }}
        .habit-col-hdr {{
            width: 130px;
            text-align: left;
            padding-left: 6px;
        }}
        .habit-name-cell {{
            text-align: left;
            padding: 4px 6px;
            font-size: 10px;
        }}
        .habit-title-input {{
            font-weight: 600;
            font-size: 10.5px;
        }}
        .h-chk {{
            width: 11px;
            height: 11px;
            margin: 0;
        }}
        .tally-cell {{
            width: 35px;
        }}
        .tally-input {{
            width: 30px;
            text-align: center;
            font-size: 10px;
            font-weight: 700;
        }}
        .habit-rule-note {{
            font-size: 10.5px;
            background: var(--cream-card);
            border: 0.5px solid var(--border-subtle);
            padding: 8px 12px;
            border-radius: 6px;
        }}

        /* Recovery Plan Page */
        .recovery-banner {{
            background: var(--sage-light);
            border: 0.5px solid var(--sage-green);
            border-radius: 8px;
            padding: 12px 16px;
            margin-bottom: 14px;
        }}
        .recovery-banner h3 {{
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 4px;
        }}
        .recovery-banner p {{
            font-size: 11px;
            line-height: 1.5;
            font-style: italic;
        }}
        .recovery-steps {{
            display: flex;
            flex-direction: column;
            gap: 10px;
        }}
        .rec-step {{
            display: flex;
            gap: 12px;
            background: #FFFDF9;
            border: 0.5px solid var(--border-subtle);
            border-radius: 6px;
            padding: 10px 14px;
            align-items: flex-start;
        }}
        .rec-num {{
            background: var(--muted-gold);
            color: var(--espresso-dark);
            width: 22px;
            height: 22px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 11px;
            flex-shrink: 0;
        }}
        .rec-body h4 {{
            font-size: 12px;
            font-weight: 700;
            margin-bottom: 2px;
        }}
        .rec-body p {{
            font-size: 10.5px;
            line-height: 1.4;
            color: rgba(73, 53, 46, 0.85);
        }}
        .forgive-box {{
            background: var(--rose-light);
            border: 0.5px dashed var(--dusty-rose);
            border-radius: 6px;
            padding: 8px 12px;
            margin-top: 6px;
            font-size: 11px;
            color: #692E39;
        }}

        /* Monthly Dated Spreads */
        .month-hero-strip {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #FFFDF9;
            border: 0.5px solid var(--border-subtle);
            border-radius: 6px;
            padding: 10px 16px;
            margin-bottom: 12px;
        }}
        .month-title {{
            font-size: 24px;
            font-weight: 700;
            line-height: 1.1;
        }}
        .month-intent-card {{
            text-align: right;
            max-width: 280px;
        }}
        .m-sub {{
            font-size: 8.5px;
            letter-spacing: 1.5px;
            color: var(--muted-gold);
            font-weight: 700;
            display: block;
        }}
        .month-intent-card p {{
            font-size: 10.5px;
            font-family: 'Lora', Georgia, serif;
            color: rgba(73, 53, 46, 0.9);
        }}
        .monthly-grid-layout {{
            display: grid;
            grid-template-columns: 3fr 2fr;
            gap: 12px;
            margin-bottom: 12px;
        }}
        .m-top-priorities, .m-key-dates {{
            background: #FFFDF9;
            border: 0.5px solid var(--border-subtle);
            border-radius: 6px;
            padding: 10px 14px;
        }}
        .m-top-priorities h4, .m-key-dates h4, .m-micro-steps h4, .m-reflection-box h4 {{
            font-size: 11.5px;
            font-weight: 700;
            margin-bottom: 6px;
        }}
        .p-input-row {{
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 11px;
            margin-bottom: 4px;
        }}
        .m-pillars-container {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 12px;
        }}
        .m-pillar-box {{
            border-radius: 6px;
            padding: 8px 12px;
            border: 0.5px solid var(--border-subtle);
        }}
        .bg-sage-light {{ background: var(--sage-light); border-color: var(--sage-green); }}
        .bg-rose-light {{ background: var(--rose-light); border-color: var(--dusty-rose); }}
        .bg-lavender-light {{ background: var(--lavender-light); border-color: var(--soft-lavender); }}
        .m-pillar-box h5 {{
            font-size: 11px;
            font-weight: 700;
            margin-bottom: 4px;
        }}
        .m-pillar-box p {{
            font-size: 9.5px;
            line-height: 1.5;
            color: rgba(73, 53, 46, 0.9);
        }}
        .mini-input {{
            border-bottom: 0.5px dashed var(--border-dotted);
            font-size: 9.5px;
            width: 100%;
        }}
        .m-micro-steps {{
            background: #FFFDF9;
            border: 0.5px solid var(--border-subtle);
            border-radius: 6px;
            padding: 10px 14px;
            margin-bottom: 12px;
        }}
        .m-reflection-box {{
            background: var(--cream-card);
            border: 0.5px solid var(--border-subtle);
            border-radius: 6px;
            padding: 10px 14px;
        }}
        .m-reflection-box p {{
            font-size: 10.5px;
            font-style: italic;
            margin-bottom: 4px;
        }}

        /* Jar of Wins */
        .jar-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 12px;
        }}
        .win-bubble {{
            background: #FFFDF9;
            border: 1px dashed var(--muted-gold);
            border-radius: 8px;
            padding: 8px 10px;
            position: relative;
        }}
        .bubble-num {{
            font-size: 9px;
            font-weight: 700;
            color: var(--muted-gold);
        }}
        .win-date {{
            font-size: 9px;
            width: 50px;
            float: right;
            text-align: right;
            border-bottom: 0.5px dashed var(--border-dotted);
        }}
        .win-text {{
            font-size: 10px;
            line-height: 1.35;
            resize: none;
            width: 100%;
            margin-top: 4px;
            border: none;
        }}
        .jar-quote {{
            text-align: center;
            font-size: 11px;
            font-family: 'Lora', Georgia, serif;
            color: rgba(73, 53, 46, 0.7);
        }}

        /* Back Cover Specifics */
        .back-cover-page {{
            padding: 18mm;
        }}
        .back-quote-box {{
            max-width: 420px;
            margin: 20px 0;
            padding: 16px;
            border-left: 2px solid var(--muted-gold);
            background: rgba(255, 255, 255, 0.4);
            border-radius: 4px;
        }}
        .back-quote {{
            font-family: 'Lora', Georgia, serif;
            font-size: 15px;
            font-style: italic;
            line-height: 1.6;
            color: var(--espresso-dark);
        }}
        .back-author-note {{
            font-size: 12px;
            margin-bottom: 25px;
            color: rgba(73, 53, 46, 0.85);
        }}
        .back-ecosystem-card {{
            background: #FFFDF9;
            border: 0.5px solid var(--muted-gold);
            border-radius: 8px;
            padding: 14px 20px;
            max-width: 440px;
            margin-bottom: 30px;
        }}
        .back-ecosystem-card h4 {{
            font-size: 11px;
            letter-spacing: 2px;
            color: var(--sage-green);
            margin-bottom: 6px;
        }}
        .back-ecosystem-card p {{
            font-size: 12px;
            line-height: 1.5;
            margin-bottom: 10px;
        }}
        .back-social-links {{
            display: flex;
            flex-direction: column;
            gap: 4px;
            font-size: 10.5px;
            color: rgba(73, 53, 46, 0.75);
            font-weight: 500;
        }}
        .back-isbn-box {{
            font-size: 9px;
            letter-spacing: 1.5px;
            color: rgba(73, 53, 46, 0.5);
            display: flex;
            flex-direction: column;
            gap: 3px;
        }}

        /* Print Specific Media Rules */
        @media print {{
            body {{
                background-color: transparent !important;
            }}
            .no-print-toolbar {{
                display: none !important;
            }}
            .journal-container {{
                padding: 0 !important;
                gap: 0 !important;
            }}
            .page {{
                margin: 0 !important;
                box-shadow: none !important;
                page-break-after: always !important;
                page-break-inside: avoid !important;
                width: 210mm !important;
                height: 297mm !important;
                min-height: 297mm !important;
                max-height: 297mm !important;
            }}
        }}

        @page {{
            size: A4 portrait;
            margin: 0;
        }}
    </style>
</head>
<body>

    <!-- Floating Interactive Action Toolbar -->
    <div class="no-print-toolbar">
        <span class="toolbar-title">📖 Dear 2027 Master Journal (52 Pages)</span>
        <button class="toolbar-btn gold" onclick="window.print()">
            🖨️ Print / Save as A4 PDF
        </button>
        <button class="toolbar-btn" onclick="fillSampleData()">
            ✨ Fill Sample Goals
        </button>
        <button class="toolbar-btn" onclick="clearAllData()">
            🧹 Clear
        </button>
    </div>

    <!-- Document Pages Wrapper -->
    <div class="journal-container">
        {pages_content}
    </div>

    <script>
        function fillSampleData() {{
            const inputs = document.querySelectorAll('.ruled-line-input, .score-input, .money-input, .mini-amt');
            const sampleAnswers = [
                "Establish peaceful 10:30 PM sleep hygiene and daily 8,000 steps",
                "Automate ₹15,000 monthly SIP into Nifty 50 Index Fund",
                "Complete 90 minutes of daily distraction-free AI & product study",
                "Hold respectful boundaries against toxic social and family comparison",
                "Build 6 months of living expenses in liquid emergency buffer"
            ];
            let i = 0;
            inputs.forEach(inp => {{
                if (!inp.value) {{
                    inp.value = sampleAnswers[i % sampleAnswers.length];
                    i++;
                }}
            }});
            alert("Sample entries populated! You can now review, customize, or click 'Print / Save as A4 PDF'.");
        }}

        function clearAllData() {{
            if (confirm("Are you sure you want to clear all entered responses?")) {{
                document.querySelectorAll('input[type="text"], textarea').forEach(el => el.value = "");
                document.querySelectorAll('input[type="checkbox"]').forEach(el => el.checked = false);
            }}
        }}
    </script>
</body>
</html>
"""

if __name__ == '__main__':
    build_planner()

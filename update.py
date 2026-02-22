import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

replacement = """<div class="content" style="padding: 30px 20px 20px 30px; text-align: center; overflow-y: auto; overflow-x: hidden;">
                        <div style="font-weight: 700; font-size: 1.05rem; color: var(--text-main); margin-bottom: 12px; letter-spacing: 0.5px;">
                            Sri Kadari Narsimhaswamy Prasanna
                        </div>

                        <div style="font-weight: 700; font-size: 1.1rem; margin-bottom: 5px; line-height: 1.4;">
                            Mrs. S.K. Janavi (Manjula) &amp; Mrs. G.R. Suresh Babu <span style="font-size: 0.85em;">PSI</span>
                        </div>
                        
                        <div style="font-size: 0.95rem; margin-bottom: 8px; font-style: italic; opacity: 0.9;">
                            Cordially invite you to take part in
                        </div>
                        
                        <div style="font-family: var(--font-heading); font-size: 1.4rem; font-weight: 700; color: var(--text-accent); margin-bottom: 12px; line-height: 1.3;">
                            "Sri Lakshmi Narasimha Swamy Pooja"
                        </div>

                        <hr style="border: 0; border-top: 1px solid rgba(196, 154, 69, 0.3); margin: 12px 0;">

                        <div style="display: flex; justify-content: center; align-items: center; gap: 12px; margin-bottom: 8px;">
                            <div style="font-size: 1rem; font-weight: 500;">March</div>
                            <div style="font-size: 1.8rem; font-weight: 700; color: var(--text-accent); border: 2px solid var(--text-accent); padding: 4px 12px; border-radius: 4px; line-height: 1;">14</div>
                            <div style="font-size: 1rem; font-weight: 500;">2025</div>
                        </div>

                        <div style="font-style: italic; font-size: 0.95rem; margin-bottom: 3px;">
                            Friday at 10.00am Onwards
                        </div>
                        <div style="font-style: italic; font-size: 0.95rem; margin-bottom: 15px;">
                            Lunch: 12.30pm
                        </div>

                        <div style="border: 1px dashed rgba(196, 154, 69, 0.6); padding: 12px; border-radius: 8px; background: rgba(0,0,0,0.02); margin-bottom: 15px;">
                            <div style="font-weight: 700; font-size: 1.1rem; color: var(--text-accent); margin-bottom: 6px;">Venue</div>
                            <div style="font-size: 0.85rem; line-height: 1.4; margin-bottom: 8px;">
                                "Namma Kanasu", No.1515, 7th Block,<br>
                                S.M.V. Layout, Near Ullala RTO Office,<br>
                                Mallathahalli, Bangalore - 91.
                            </div>
                            <a href="https://maps.app.goo.gl/AENr8VCK2PSr6i8s7?g_st=ic" target="_blank" style="color: var(--text-accent); text-decoration: none; font-weight: 600; font-style: italic; display: inline-flex; align-items: center; gap: 4px; font-size: 0.9rem;">
                                ↗ Tap for directions
                            </a>
                        </div>

                        <div style="display: flex; justify-content: space-between; text-align: left; font-size: 0.85rem; margin-bottom: 15px; margin-top: auto; align-items: flex-end;">
                            <div style="flex: 1;">
                                <div style="font-weight: 700; color: var(--text-accent); margin-bottom: 4px; font-size: 0.95rem;">Your's</div>
                                <div style="line-height: 1.4; font-weight: 600;">Smt/Sri. Janavi<br>Suresh Babu</div>
                            </div>
                            <div style="flex: 1.4; text-align: right; line-height: 1.4; font-weight: 600;">
                                <div style="margin-bottom: 2px;"><span style="color: var(--text-main);">Mob:</span> <a href="tel:9448048294" style="color: #2b4b9b; text-decoration: none;">9448048294</a> | <a href="tel:7019312549" style="color: #2b4b9b; text-decoration: none;">7019312549</a></div>
                                <div><a href="tel:9980929268" style="color: #2b4b9b; text-decoration: none;">9980929268</a> | <a href="tel:8310757905" style="color: #2b4b9b; text-decoration: none;">8310757905</a></div>
                            </div>
                        </div>

                        <div style="display: flex; gap: 10px; justify-content: center; padding-bottom: 10px;">
                            <button class="open-btn" style="margin-top: 0; margin-bottom: 0; padding: 10px 20px; font-size: 0.85rem; color: var(--text-accent); border-color: var(--text-accent); background: transparent;" onclick="flipBack('page1')">Previous Page</button>
                            <button class="open-btn" style="margin-top: 0; margin-bottom: 0; padding: 10px 20px; font-size: 0.85rem; color: var(--page-color); background-color: var(--text-accent); border-color: var(--text-accent);" onclick="flipNext('page2')">Next Page</button>
                        </div>
                        <!-- Rings injected via JS -->"""

new_text = re.sub(
    r'<div class="content" style="padding-top: 30px;">.*?<!-- Rings injected via JS -->',
    replacement, text, flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Replacement successful")

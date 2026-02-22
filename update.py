import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

replacement = """<div class="content" style="padding: 25px 20px 20px 20px; text-align: center; overflow-y: auto; overflow-x: hidden; display: flex; flex-direction: column; justify-content: space-between;">
                            <div style="font-family: var(--font-heading); font-weight: 700; font-size: clamp(1.2rem, 3.5vw, 1.5rem); color: var(--text-accent); margin-bottom: 15px; letter-spacing: 0.5px; text-transform: uppercase; line-height: 1.2;">
                                Sri Kadari Narsimhaswamy Prasanna
                            </div>

                            <div style="font-weight: 700; font-size: 1.05rem; margin-bottom: 5px; line-height: 1.4; color: var(--text-main);">
                                Mrs. S.K. Janavi (Manjula) &amp; Mrs. G.R. Suresh Babu <span style="font-size: 0.8em; opacity: 0.9;">PSI</span>
                            </div>
                            
                            <div style="font-size: 0.95rem; margin-bottom: 10px; line-height: 1.4; font-style: italic; opacity: 0.9; color: var(--text-main);">
                                Cordially invite you to take part in
                            </div>
                            
                            <div style="font-family: var(--font-heading); font-size: 1.4rem; font-weight: 700; color: var(--text-accent); margin-bottom: 10px; line-height: 1.3;">
                                "Sri Lakshmi Narasimha Swamy Pooja"
                            </div>

                            <hr style="border: 0; border-top: 1px solid rgba(196, 154, 69, 0.4); margin: 10px 15%; width: 70%;">

                            <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin-bottom: 10px; color: var(--text-main);">
                                <div style="font-size: 1.1rem; font-weight: 500;">March</div>
                                <div style="font-size: 1.8rem; font-weight: 700; color: var(--text-accent); border: 2px solid var(--text-accent); padding: 5px 12px; border-radius: 4px; line-height: 1;">08</div>
                                <div style="font-size: 1.1rem; font-weight: 500;">2026</div>
                            </div>

                            <div style="font-style: italic; font-size: 1rem; margin-bottom: 5px; text-transform: capitalize; line-height: 1.4; color: var(--text-main);">
                                sunday<br>10am onwards
                            </div>
                            <div style="font-style: italic; font-size: 0.95rem; margin-bottom: 15px; opacity: 0.9; color: var(--text-main);">
                                Lunch: 12.30pm
                            </div>

                            <div style="border: 1px dashed rgba(196, 154, 69, 0.5); padding: 12px; border-radius: 8px; background: rgba(0,0,0,0.02); margin-bottom: 15px;">
                                <div style="font-weight: 700; font-size: 1.1rem; color: var(--text-accent); margin-bottom: 6px;">Venue</div>
                                <div style="font-size: 0.9rem; line-height: 1.4; margin-bottom: 8px; color: var(--text-main);">
                                    "Namma Kanasu", No.1515, 7th Block,<br>
                                    S.M.V. Layout, Near Ullala RTO Office,<br>
                                    Mallathahalli, Bangalore - 91.
                                </div>
                                <a href="https://maps.app.goo.gl/AENr8VCK2PSr6i8s7?g_st=ic" target="_blank" style="color: var(--text-accent); text-decoration: none; font-weight: 600; font-style: italic; display: inline-flex; align-items: center; gap: 5px; font-size: 0.9rem;">
                                    ↗ Tap for directions
                                </a>
                            </div>

                            <div style="display: flex; justify-content: space-between; text-align: left; font-size: 0.85rem; margin-bottom: 15px; align-items: flex-end; width: 100%; color: var(--text-main);">
                                <div style="flex: 1;">
                                    <div style="font-weight: 700; color: var(--text-accent); margin-bottom: 4px; font-size: 0.95rem;">Your's</div>
                                    <div style="line-height: 1.4; font-weight: 600;">Smt/Sri. Janavi<br>Suresh Babu</div>
                                </div>
                                <div style="flex: 1.5; text-align: right; line-height: 1.4; font-weight: 600;">
                                    <div style="margin-bottom: 3px;">Mob: <a href="tel:9448048294" style="color: #2b4b9b; text-decoration: none;">9448048294</a> | <a href="tel:7019312549" style="color: #2b4b9b; text-decoration: none;">7019312549</a></div>
                                    <div><a href="tel:9980929268" style="color: #2b4b9b; text-decoration: none;">9980929268</a> | <a href="tel:8310757905" style="color: #2b4b9b; text-decoration: none;">8310757905</a></div>
                                </div>
                            </div>

                            <div style="display: flex; gap: 10px; justify-content: center; padding-bottom: 10px;">
                                <button class="open-btn" style="margin: 0; padding: 10px 20px; font-size: 0.9rem; color: var(--text-accent); border-color: var(--text-accent); background: transparent;" onclick="flipBack('page1')">Previous Page</button>
                                <button class="open-btn" style="margin: 0; padding: 10px 20px; font-size: 0.9rem; color: var(--page-color); background-color: var(--text-accent); border-color: var(--text-accent); font-weight: 600;" onclick="flipNext('page2')">Next Page</button>
                            </div>
                            <!-- Rings injected via JS -->
                        </div>"""

new_text = re.sub(
    r'<div class="content"\s*style="padding: 15px; text-align: center; overflow-y: auto; overflow-x: hidden; background: linear-gradient.*?<!-- Rings injected via JS -->\s*</div>',
    replacement, text, flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Replacement successful")

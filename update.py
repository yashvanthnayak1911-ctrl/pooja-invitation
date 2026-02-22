import re

with open("index.html", "r", encoding="utf-8") as f:
    text = f.read()

replacement = """<div class="content" style="padding: 15px; text-align: center; overflow-y: auto; overflow-x: hidden; background: linear-gradient(rgba(20, 5, 5, 0.65), rgba(40, 10, 20, 0.7)), url('front-image.png') center/cover; border: 3px solid rgba(214, 169, 22, 0.6); border-radius: 10px; margin: 10px; height: calc(100% - 20px); color: var(--page-color); display: flex; flex-direction: column; justify-content: space-between;">
                            <div style="font-family: var(--font-heading); font-weight: 700; font-size: clamp(1.1rem, 3.5vw, 1.3rem); color: #d6a916; margin-bottom: 5px; letter-spacing: 0.5px; text-transform: uppercase; text-shadow: 2px 2px 4px rgba(0,0,0,0.8); line-height: 1.1;">
                                Sri Kadari Narsimhaswamy Prasanna
                            </div>

                            <div style="font-weight: 700; font-size: 0.95rem; margin-bottom: 3px; line-height: 1.2; text-shadow: 1px 1px 3px rgba(0,0,0,0.8);">
                                Mrs. S.K. Janavi (Manjula) &amp; Mrs. G.R. Suresh Babu <span style="font-size: 0.8em; opacity: 0.9;">PSI</span>
                            </div>
                            
                            <div style="font-size: 0.85rem; margin-bottom: 5px; line-height: 1.2; font-style: italic; opacity: 0.9;">
                                Cordially invite you to take part in
                            </div>
                            
                            <div style="font-family: var(--font-heading); font-size: 1.3rem; font-weight: 700; color: #d6a916; margin-bottom: 5px; line-height: 1.2; text-shadow: 2px 2px 4px rgba(0,0,0,0.8);">
                                "Sri Lakshmi Narasimha Swamy Pooja"
                            </div>

                            <hr style="border: 0; border-top: 1px solid rgba(214, 169, 22, 0.4); margin: 5px 15%; width: 70%;">

                            <div style="display: flex; justify-content: center; align-items: center; gap: 10px; margin-bottom: 3px;">
                                <div style="font-size: 0.9rem; font-weight: 500;">March</div>
                                <div style="font-size: 1.5rem; font-weight: 700; color: #d6a916; border: 2px solid #d6a916; padding: 2px 10px; border-radius: 4px; line-height: 1; box-shadow: 0 0 10px rgba(214, 169, 22, 0.2), inset 0 0 10px rgba(214, 169, 22, 0.2);">14</div>
                                <div style="font-size: 0.9rem; font-weight: 500;">2025</div>
                            </div>

                            <div style="font-style: italic; font-size: 0.9rem; margin-bottom: 2px; text-transform: capitalize; line-height: 1.2;">
                                sunday<br>10am onwards
                            </div>
                            <div style="font-style: italic; font-size: 0.85rem; margin-bottom: 5px; opacity: 0.9;">
                                Lunch: 12.30pm
                            </div>

                            <div style="border: 1px dashed rgba(214, 169, 22, 0.5); padding: 8px; border-radius: 8px; background: rgba(0,0,0,0.4); margin-bottom: 5px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                                <div style="font-weight: 700; font-size: 1rem; color: #d6a916; margin-bottom: 4px;">Venue</div>
                                <div style="font-size: 0.8rem; line-height: 1.3; margin-bottom: 4px; color: rgba(255,255,255,0.9);">
                                    "Namma Kanasu", No.1515, 7th Block,<br>
                                    S.M.V. Layout, Near Ullala RTO Office,<br>
                                    Mallathahalli, Bangalore - 91.
                                </div>
                                <a href="https://maps.app.goo.gl/AENr8VCK2PSr6i8s7?g_st=ic" target="_blank" style="color: #d6a916; text-decoration: none; font-weight: 600; font-style: italic; display: inline-flex; align-items: center; gap: 5px; font-size: 0.85rem; transition: opacity 0.3s;" onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">
                                    ↗ Tap for directions
                                </a>
                            </div>

                            <div style="display: flex; justify-content: space-between; text-align: left; font-size: 0.8rem; margin-bottom: 5px; align-items: flex-end; width: 100%;">
                                <div style="flex: 1;">
                                    <div style="font-weight: 700; color: #d6a916; margin-bottom: 2px; font-size: 0.9rem;">Your's</div>
                                    <div style="line-height: 1.3; font-weight: 500; text-shadow: 1px 1px 2px rgba(0,0,0,0.8);">Smt/Sri. Janavi<br>Suresh Babu</div>
                                </div>
                                <div style="flex: 1.5; text-align: right; line-height: 1.3; font-weight: 500; text-shadow: 1px 1px 2px rgba(0,0,0,0.8);">
                                    <div style="margin-bottom: 2px;"><span style="color: #d6a916;">Mob:</span> <a href="tel:9448048294" style="color: #6bb5ff; text-decoration: none;">9448048294</a> | <a href="tel:7019312549" style="color: #6bb5ff; text-decoration: none;">7019312549</a></div>
                                    <div><a href="tel:9980929268" style="color: #6bb5ff; text-decoration: none;">9980929268</a> | <a href="tel:8310757905" style="color: #6bb5ff; text-decoration: none;">8310757905</a></div>
                                </div>
                            </div>

                            <div style="display: flex; gap: 10px; justify-content: center; padding-bottom: 0;">
                                <button class="open-btn" style="margin: 0; padding: 6px 15px; font-size: 0.8rem; color: #d6a916; border-color: #d6a916; background: rgba(0,0,0,0.5); backdrop-filter: blur(5px);" onclick="flipBack('page1')">Previous Page</button>
                                <button class="open-btn" style="margin: 0; padding: 6px 15px; font-size: 0.8rem; color: #1a1a2e; background-color: #d6a916; border-color: #d6a916; font-weight: 600;" onclick="flipNext('page2')">Next Page</button>
                            </div>
                            <!-- Rings injected via JS -->
                        </div>"""

new_text = re.sub(
    r'<div class="content"\s*style="padding: 25px 20px 20px 20px; text-align: center; overflow-y: auto; overflow-x: hidden; background: linear-gradient.*?<!-- Rings injected via JS -->\s*</div>',
    replacement, text, flags=re.DOTALL
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_text)

print("Updated text sizing and margins.")

import re

# Read the file
with open('c:\\Users\\yashv\\OneDrive\\Desktop\\invitation\\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new content for page 2
new_content = """                <div class="side">
                    <div class="content inner-content page-layout"
                        style="text-align: center; overflow-y: auto; overflow-x: hidden; display: flex; flex-direction: column; justify-content: center; gap: 0.5vh; padding: 10px 15px; background-image: url('front-image.png'); background-size: cover; background-position: center; border-radius: 5px;">
                        
                        <div class="header-text"
                            style="font-family: var(--font-heading), serif; font-weight: 700; font-size: clamp(1.1rem, 3.5vw, 1.3rem); line-height: 1.3; color: #8b2b1a; text-shadow: 0px 1px 2px rgba(0,0,0,0.1); margin-top: -1.5vh; margin-bottom: 0.5vh;">
                            You are cordially<br>invited to join us for<br>Poojas at our Home
                        </div>

                        <div class="date-box"
                            style="font-family: var(--font-heading), serif; font-size: clamp(1rem, 3.5vw, 1.25rem); font-weight: 700; color: #8b2b1a; margin: 0.5vh 0;">
                            08 March 2026, Sunday
                        </div>

                        <div class="events-container" style="display: flex; flex-direction: column; gap: 1vh; align-items: center; width: 100%;">
                            <div class="event-bubble" style="background-color: rgba(255, 241, 216, 0.9); border-top: 2px solid #dfa25b; border-bottom: 2px solid #dfa25b; border-radius: 12px; padding: 1vh 2vw; width: 90%; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                                <p class="time" style="font-size: clamp(0.9rem, 2.5vw, 1.1rem); margin: 0; color: #b74124; font-weight: 600;">Morning 10:00 AM</p>
                                <h4 class="event-name" style="font-size: clamp(1.05rem, 3vw, 1.3rem); margin: 0; color: #8b2b1a; font-weight: 700; font-family: var(--font-heading), serif;">Srinivasa Kalyanotsava</h4>
                            </div>

                            <div class="event-bubble" style="background-color: rgba(255, 241, 216, 0.9); border-top: 2px solid #dfa25b; border-bottom: 2px solid #dfa25b; border-radius: 12px; padding: 1vh 2vw; width: 90%; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
                                <p class="time" style="font-size: clamp(0.9rem, 2.5vw, 1.1rem); margin: 0; color: #b74124; font-weight: 600;">Evening 6:00 PM</p>
                                <h4 class="event-name" style="font-size: clamp(1.05rem, 3vw, 1.3rem); margin: 0; color: #8b2b1a; font-weight: 700; font-family: var(--font-heading), serif;">Satyanarayanaswamy Pooja</h4>
                            </div>
                        </div>

                        <div class="invite-section" style="margin-top: 1vh; position: relative;">
                            <div style="font-family: var(--font-heading), serif; font-weight: 700; font-size: clamp(0.9rem, 2.8vw, 1.1rem); color: #8b2b1a; margin-bottom: 0.25vh;">
                                Invited by: SGT Family
                            </div>
                            <div style="font-weight: 600; font-size: clamp(0.8rem, 2.5vw, 0.95rem); line-height: 1.4; color: #a43419;">
                                Sri Mathi Lalitha &amp; Sri Ravishankar<br>
                                Sri Mathi Manjula &amp; Sri Shreyas
                            </div>
                        </div>

                        <div class="nav-button-container" style="margin-top: 1vh;">
                            <button class="open-btn nav-btn"
                                style="font-size: 0.9rem; font-weight: 600; padding: 6px 20px; border-radius: 20px;"
                                onclick="flipBack('page1')">Previous Page</button>
                        </div>
                        <!-- Rings injected via JS -->
                    </div>
                </div>"""

# Replace the specific div with the new content using regex
# We start from `<div class="side">` inside `#page2` up to its matching `</div>` covering the rings comment.
pattern = r'<div class="side">\s*<div class="content inner-content page-layout"[\s\S]*?<!-- Rings injected via JS -->\s*</div>\s*</div>'
updated_content = re.sub(pattern, new_content, content, count=1)

with open('c:\\Users\\yashv\\OneDrive\\Desktop\\invitation\\index.html', 'w', encoding='utf-8') as f:
    f.write(updated_content)

print("HTML content updated successfully")

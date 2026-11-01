from pathlib import Path
import streamlit as st

st.set_page_config(page_title="Union High School | Student Art Wall", page_icon="🎨", layout="wide")

RED = "#df1733"
LOGO = Path(__file__).parent / "union-logo.png"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;1,500;1,600&display=swap');
:root { --red:#df1733; --ink:#171717; --paper:#fbfaf8; --muted:#827d77; --line:#e9e5df; --cream:#f2efea; }
html { scroll-behavior:smooth; }
.stApp { background:var(--paper); color:var(--ink); font-family:'DM Sans',sans-serif; }
.block-container { max-width:1440px; padding:0 0 0; }
[data-testid="stHeader"] { background:transparent; }
[data-testid="stToolbar"] { right:1rem; }
h1,h2,h3 { font-family:'Playfair Display',Georgia,serif; font-weight:500; letter-spacing:-.035em; }
p { line-height:1.7; }
a { color:var(--red)!important; }
.site-header { display:flex; align-items:center; gap:14px; background:#fff; padding:12px clamp(22px,5.3vw,64px); border-bottom:1px solid #e9e6e1; }
.site-header img { width:42px;height:42px;object-fit:contain; }
.site-name {font-size:13px;font-weight:700;line-height:1.25;}
.site-sub {font-size:8px;color:#817b75;letter-spacing:.13em;text-transform:uppercase;margin-top:4px;}
.site-nav {margin-left:auto;display:flex;align-items:center;gap:28px;font-size:10px;font-weight:600;}
.site-nav a {color:#252525!important;text-decoration:none!important;}
.nav-cta {background:var(--red);color:white!important;padding:13px 18px;}
.hero { background:radial-gradient(ellipse at 80% 45%,#202020 0%,#171717 60%); color:white; padding:clamp(42px,7vw,88px) clamp(24px,5.3vw,64px) 38px; position:relative; overflow:hidden; }
.hero-grid {display:grid;grid-template-columns:1.2fr .9fr;gap:clamp(25px,6vw,90px);align-items:center;max-width:1300px;margin:auto;}
.eyebrow {font-size:9px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;margin-bottom:24px;}
.hero h1 {font-size:clamp(42px,5.5vw,68px);line-height:.98;color:white;margin:0 0 18px;}
.red-italic {color:var(--red);font-style:italic;}
.hero-copy {color:#d3d0cd;max-width:520px;font-size:13px;}
.hero-actions {display:flex;align-items:center;gap:24px;margin:26px 0 24px;flex-wrap:wrap;}
.primary-link {display:inline-block;background:var(--red);color:white!important;padding:14px 20px;font-size:10px;font-weight:700;text-decoration:none!important;}
.text-link {color:white!important;text-decoration:none!important;font-size:10px;font-weight:700;}
.privacy-line {font-size:9px;color:#b4b0ac;margin-top:20px;}
.art-poster {max-width:420px;width:100%;justify-self:center;background:#242424;border:1px solid #45413d;padding:20px;transform:rotate(.6deg);position:relative;}
.poster-top,.poster-bottom {display:flex;justify-content:space-between;color:#c4beb7;font-size:7px;letter-spacing:.13em;text-transform:uppercase;}
.poster-paper {background:#f8f5ef;color:#282624;padding:14px;margin:16px 0;}
.poster-caption {font-size:7px;letter-spacing:.12em;text-transform:uppercase;}
.poster-art {height:clamp(150px,20vw,240px);background:#ebe5d9;position:relative;overflow:hidden;margin:12px 0;}
.poster-sun {position:absolute;width:42px;height:42px;border-radius:50%;background:var(--red);right:15%;top:12%;}
.poster-black {position:absolute;left:-5%;bottom:-25%;width:85%;height:63%;background:#252523;border-radius:65% 60% 0 0;transform:rotate(-8deg);}
.poster-tan {position:absolute;right:-4%;bottom:-10%;width:62%;height:48%;background:#bdb3a5;border-radius:60% 55% 0 0;}
.hero-index {text-align:right;max-width:1300px;margin:35px auto 0;color:#b5b0a9;font-size:8px;letter-spacing:.16em;}
.section {padding:clamp(42px,6vw,82px) clamp(22px,2.5vw,32px);border-bottom:1px solid var(--line);scroll-margin-top:16px;}
.section-inner {max-width:1360px;margin:auto;}
.section-kicker {font-size:9px;letter-spacing:.17em;text-transform:uppercase;color:#827b74;margin-bottom:20px;}
.section-heading {font-size:clamp(35px,4.5vw,49px);line-height:.98;margin:0;}
.gallery-intro {display:grid;grid-template-columns:1fr .62fr;gap:30px;align-items:end;margin-bottom:32px;}
.gallery-intro p {color:#827d77;font-size:12px;max-width:400px;margin:0 0 4px;}
.empty-gallery {background:#f3f0eb;border:1px solid #e6e1db;min-height:205px;display:grid;grid-template-columns:.8fr 1.2fr;gap:24px;align-items:center;padding:26px 5%;}
.mini-art {width:115px;height:135px;background:#fbf8f2;box-shadow:0 8px 20px #00000012;transform:rotate(-4deg);padding:8px;justify-self:center;position:relative;}
.mini-art-inner {height:100%;background:#e9e1d5;position:relative;overflow:hidden;}
.mini-art-inner:before {content:'';position:absolute;left:-15%;bottom:25%;height:45%;width:100%;background:#c6b8a4;border-radius:0 0 55% 45%;}
.mini-art-inner:after {content:'';position:absolute;left:-10%;bottom:-10%;height:55%;width:120%;background:#242423;border-radius:60% 50% 0 0;transform:rotate(-7deg);}
.mini-sun {position:absolute;z-index:3;right:12%;top:20%;width:22px;height:22px;background:var(--red);border-radius:50%;}
.empty-label {font-size:8px;letter-spacing:.17em;color:var(--red);font-weight:700;text-transform:uppercase;}
.empty-title {font-family:'Playfair Display',Georgia,serif;font-size:23px;line-height:1.15;margin:13px 0 7px;}
.empty-desc {font-size:10px;color:#8a837b;margin-bottom:15px;}
.jump-link {font-size:10px;font-weight:700;color:var(--red)!important;text-decoration:none!important;}
.submission-grid {display:grid;grid-template-columns:.85fr 1.15fr;gap:clamp(28px,8vw,120px);align-items:start;}
.submission-copy {max-width:440px;}
.submission-copy p {font-size:12px;color:#817b75;}
.privacy-note {border-left:2px solid var(--red);background:#f1eee9;padding:15px 16px;margin-top:22px;font-size:10px;color:#77716a;}
.privacy-note strong {color:#242424;display:block;margin-bottom:4px;}
.form-card {background:white;border:1px solid #e9e5e0;box-shadow:0 10px 35px #00000005;padding:clamp(18px,3vw,30px);}
.form-head {display:flex;align-items:center;gap:10px;font-size:13px;font-weight:700;margin-bottom:20px;}
.form-number {font-family:'Playfair Display',serif;color:var(--red);}
.preview-badge {margin-left:auto;background:#f7eeee;color:#b9a5a5;padding:5px 7px;font-size:7px;letter-spacing:.1em;}
.form-foot {font-size:8px;color:#99918a;text-align:center;margin-top:12px;}
.rule-section {background:#171717;color:white;padding:clamp(40px,6vw,72px) clamp(22px,5.3vw,64px);}
.rules-grid {max-width:1300px;margin:auto;display:grid;grid-template-columns:.9fr 1.25fr;gap:clamp(28px,8vw,100px);}
.rule-section h2 {font-size:clamp(32px,4vw,42px);line-height:1.05;color:white;margin:22px 0;}
.rules-list {display:grid;grid-template-columns:1fr 1fr;gap:0 30px;}
.rule {border-top:1px solid #393735;padding:16px 0;font-size:10px;color:#aaa49d;line-height:1.7;}
.rule strong {display:block;color:white;font-size:11px;margin-bottom:5px;}
.rule-no {color:var(--red);margin-right:10px;}
.disclaimer {font-size:9px;color:#918b85;line-height:1.7;margin-top:20px;}
div[data-testid="stForm"] {border:0;padding:0;}
div.stButton>button,div.stFormSubmitButton>button {background:var(--red);color:white;border:0;border-radius:0;font-weight:700;min-height:42px;}
div.stButton>button:hover,div.stFormSubmitButton>button:hover {background:#bd1028;color:white;border:0;}
[data-testid="stFileUploader"] {border:1px dashed #d4cec6;background:#fcfbf9;padding:10px;}
@media(max-width:760px) {
 .site-nav {gap:12px;font-size:9px;} .site-nav .nav-optional {display:none;}
 .hero-grid,.gallery-intro,.submission-grid,.rules-grid {grid-template-columns:1fr;}
 .art-poster {max-width:420px;margin-top:5px;}
 .hero-index {margin-top:22px;}
 .gallery-intro p {margin-top:10px;}
 .empty-gallery {grid-template-columns:.6fr 1.4fr;padding:20px 14px;gap:14px;}
 .mini-art {width:85px;height:105px;}
 .empty-title {font-size:20px;}
 .rules-list {grid-template-columns:1fr;}
}
@media(max-width:420px) {
 .site-header {padding:10px 14px;gap:9px;} .site-header img {width:34px;height:34px;}
 .site-nav {gap:9px;} .nav-cta {padding:10px 11px;}
 .empty-gallery {grid-template-columns:1fr;} .mini-art {display:none;}
}
</style>
""", unsafe_allow_html=True)

# Header navigation uses native in-page anchors so links scroll to their actual sections.
logo_html = f'<img src="data:image/png;base64,{__import__("base64").b64encode(LOGO.read_bytes()).decode()}" alt="Union Spartan logo">' if LOGO.exists() else '<div style="font-size:28px">🎨</div>'
st.markdown(f"""
<header class="site-header">
 {logo_html}
 <div><div class="site-name">Union High School</div><div class="site-sub">Student Art Wall · Rosehill, NC</div></div>
 <nav class="site-nav">
   <a href="#gallery">The gallery</a>
   <a class="nav-optional" href="#community-rules">Community rules</a>
   <a class="nav-cta" href="#share-art">Share your art&nbsp; →</a>
 </nav>
</header>
""", unsafe_allow_html=True)

st.markdown("""
<section class="hero">
 <div class="hero-grid">
  <div>
   <div class="eyebrow">🔴 &nbsp; A STUDENT GALLERY CONCEPT</div>
   <h1>Made here.<br><span class="red-italic">Shared with pride.</span></h1>
   <p class="hero-copy">A place for Union students to show the art they make. Put your work out there under an artist name you choose.</p>
   <div class="hero-actions"><a class="primary-link" href="#share-art">Share a piece&nbsp; →</a><a class="text-link" href="#gallery">Take a look at the wall&nbsp; ↓</a></div>
   <div class="privacy-line">◇ &nbsp; No real name needed. Keep your personal details private.</div>
  </div>
  <div class="art-poster">
   <div class="poster-top"><span>Union · student work</span><span>01—∞</span></div>
   <div class="poster-paper"><div class="poster-caption">The wall is yours</div><div class="poster-art"><div class="poster-sun"></div><div class="poster-black"></div><div class="poster-tan"></div></div><div class="poster-caption">Your art goes here</div></div>
   <div class="poster-bottom"><span>Home of the Spartans</span><span>Rosehill, NC</span></div>
  </div>
 </div>
 <div class="hero-index">01 / ARTISTS</div>
</section>
""", unsafe_allow_html=True)

# Real anchor target for gallery and the red "Add the first preview" action.
st.markdown('<div id="gallery"></div>', unsafe_allow_html=True)
st.markdown('<section class="section"><div class="section-inner"><div class="gallery-intro"><div><div class="section-kicker">THE GALLERY　—</div><h2 class="section-heading">The wall starts<br>with <span class="red-italic">you.</span></h2></div><p>A spot for the sketches, photos, paintings, and ideas made by Union students. This preview is waiting for its first piece.</p></div></div></section>', unsafe_allow_html=True)

if "artworks" not in st.session_state:
    st.session_state.artworks = []

if not st.session_state.artworks:
    st.markdown("""
    <div class="empty-gallery">
      <div class="mini-art"><div class="mini-art-inner"><span class="mini-sun"></span></div></div>
      <div><div class="empty-label">NO ARTWORKS YET</div><div class="empty-title">Every gallery has a first piece.</div>
      <div class="empty-desc">Choose a favorite work and preview how it could look on the wall.</div>
      <a class="jump-link" href="#gallery">Add the first preview&nbsp; →</a></div>
    </div>
    """, unsafe_allow_html=True)
    # This is the real working submission area, anchored below; the gallery link above
    # intentionally jumps to the gallery section, as requested.
else:
    cols = st.columns(3)
    for i, artwork in enumerate(reversed(st.session_state.artworks)):
        with cols[i % 3]:
            st.image(artwork["image"], use_container_width=True)
            st.subheader(artwork["title"])
            st.caption(f'By {artwork["artist"]}')

st.markdown('<div style="height:72px"></div><div id="share-art"></div>', unsafe_allow_html=True)
st.markdown("""
<section class="section"><div class="section-inner submission-grid">
 <div class="submission-copy"><div class="section-kicker">YOUR TURN　—</div>
 <h2 class="section-heading">Put your<br><span class="red-italic">work on the wall.</span></h2>
 <p>Pick an image and tell us what to call you. You can use an artist name or nickname instead of your real name.</p>
 <div class="privacy-note"><strong>✳ &nbsp; Your name, your choice.</strong>Please don't add your real name, phone number, or other personal details to your art or title.</div>
 </div>
 <div class="form-card"><div class="form-head"><span class="form-number">01</span> Add your artwork <span class="preview-badge">PREVIEW ONLY</span></div>
 """, unsafe_allow_html=True)

with st.form("artwork_form", clear_on_submit=True):
    uploaded = st.file_uploader("Choose a file or drop it here · JPG, PNG, or WEBP · up to 10 MB", type=["jpg", "jpeg", "png", "webp"])
    a, b = st.columns(2)
    with a:
        title = st.text_input("Artwork title (optional)", max_chars=70, placeholder="Give it a name")
    with b:
        artist = st.text_input("Artist name (optional)", max_chars=40, placeholder="Nickname or artist name")
    consent = st.checkbox("I made this artwork or have permission to share it, and it follows the community rules.")
    submitted = st.form_submit_button("Preview my artwork　→", use_container_width=True)

if submitted:
    if uploaded is None:
        st.error("Choose an image first.")
    elif uploaded.size > 10 * 1024 * 1024:
        st.error("Please choose an image under 10 MB.")
    elif not consent:
        st.error("Please confirm permission to share this artwork.")
    else:
        st.session_state.artworks.append({
            "image": uploaded.getvalue(),
            "title": title.strip() or "Untitled artwork",
            "artist": artist.strip() or "Anonymous artist",
        })
        st.success("Preview added. It appears in the gallery above during this session.")
        st.rerun()

st.markdown('<div class="form-foot">This is a local preview only. Your image and details are not uploaded to a permanent gallery or saved.</div></div></div></section>', unsafe_allow_html=True)

st.markdown('<div id="community-rules"></div><section class="rule-section"><div class="rules-grid"><div><div class="eyebrow">🔴 &nbsp; A GOOD WALL MAKES ROOM FOR EVERYONE</div><h2>Keep it creative.<br><span class="red-italic">Keep it respectful.</span></h2></div><div class="rules-list"><div><div class="rule"><strong><span class="rule-no">01</span>Make it yours to share.</strong>Post work you created, or artwork you have permission to share.</div><div class="rule"><strong><span class="rule-no">03</span>Respect people’s privacy.</strong>Use an artist name if you like. Leave out real names, contact details, and private information.</div></div><div><div class="rule"><strong><span class="rule-no">02</span>No violence or illegal material.</strong>Don’t post art promoting violence, threats, or illegal activity.</div><div class="rule"><strong><span class="rule-no">04</span>Make space for your classmates.</strong>No harassment or content that targets or humiliates another person.</div></div><div class="disclaimer" style="grid-column:1/-1">This is a concept preview, not a live school submission or moderation service. Any public gallery should be reviewed and approved by the school before launch.</div></div></div></section>', unsafe_allow_html=True)
st.markdown('<div style="background:#171717;color:#aaa49d;text-align:center;font-size:9px;padding:18px">Union High School · Student Art Wall concept · Student privacy comes first.</div>', unsafe_allow_html=True)

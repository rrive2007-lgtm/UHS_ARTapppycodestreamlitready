from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="Union High School — Student Art Wall",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

RED = "#df1733"
INK = "#171717"
PAPER = "#faf9f7"
CREAM = "#f1eee8"

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;1,500&display=swap');
    .stApp { background: #faf9f7; color: #171717; }
    .block-container { max-width: 1280px; padding-top: 1.2rem; }
    [data-testid="stHeader"] { background: transparent; }
    h1, h2, h3 { font-family: 'Playfair Display', Georgia, serif; }
    .brandline { border-bottom: 1px solid #e9e6e1; padding-bottom: 15px; margin-bottom: 18px; }
    .brandname { font-size: 15px; font-weight: 750; line-height: 1.25; }
    .brandsub { font-size: 9px; color: #77736f; letter-spacing: .13em; text-transform: uppercase; margin-top: 4px; }
    .hero { background: #171717; color: white; padding: clamp(24px, 5vw, 64px); margin: 8px 0 48px; }
    .eyebrow { font-size: 10px; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; margin-bottom: 22px; }
    .hero h1 { color: white; font-size: clamp(38px, 5vw, 64px); line-height: 1.02; margin-bottom: 18px; }
    .red { color: #df1733; font-style: italic; }
    .hero p { color: #d2d0ce; max-width: 560px; }
    .label { font-size: 9px; color: #706a64; letter-spacing: .16em; text-transform: uppercase; font-weight: 700; margin-bottom: 15px; }
    .empty { background: #f1eee8; border: 1px solid #e6e1db; padding: 28px; }
    .empty h3 { font-size: 25px; margin-top: 12px; }
    .muted { color: #77736f; font-size: 12px; }
    .poster { background: #202020; border: 1px solid #45433f; padding: 18px; }
    .poster-head, .poster-foot { display: flex; justify-content: space-between; color: #c4beb7; font-size: 8px; letter-spacing: .13em; text-transform: uppercase; }
    .poster-paper { background: #f7f3ec; padding: 12px; margin: 14px 0; color: #252525; }
    .poster-art { height: 210px; background: #ebe5d9; position: relative; overflow: hidden; margin: 10px 0; }
    .poster-art:before { content: ''; position: absolute; width: 95%; height: 60%; background: #262625; border-radius: 60% 55% 0 0; left: -8%; bottom: -18%; transform: rotate(-8deg); }
    .poster-art:after { content: ''; position: absolute; width: 65%; height: 45%; background: #bdb3a5; border-radius: 55% 50% 0 0; right: -5%; bottom: -8%; }
    .sun { position: absolute; z-index: 2; width: 42px; height: 42px; border-radius: 50%; background: #df1733; right: 15%; top: 12%; }
    .poster-caption { font-size: 8px; letter-spacing: .1em; text-transform: uppercase; color: #5f5951; }
    div.stButton > button, div.stFormSubmitButton > button { background: #df1733; color: white; border: 0; border-radius: 0; font-weight: 700; }
    div.stButton > button:hover, div.stFormSubmitButton > button:hover { background: #bd1028; color: white; border: 0; }
    [data-testid="stFileUploader"] { background: #fcfbf9; border: 1px dashed #d4cec6; padding: 10px; }
    .rulebox { border-top: 1px solid #ded8d1; padding: 15px 0; font-size: 12px; }
    @media(max-width: 700px) { .hero { padding: 24px; } .poster-art { height: 160px; } }
    </style>
    """,
    unsafe_allow_html=True,
)

logo_path = Path(__file__).parent / "union-logo.png"
logo_col, title_col = st.columns([0.09, 0.91], vertical_alignment="center")
with logo_col:
    if logo_path.exists():
        st.image(str(logo_path), width=48)
    else:
        st.markdown("🎨")
with title_col:
    st.markdown(
        '<div class="brandline"><div class="brandname">Union High School</div>'
        '<div class="brandsub">Student Art Wall · Rosehill, NC</div></div>',
        unsafe_allow_html=True,
    )

left, right = st.columns([1.15, 0.85], gap="large")
with left:
    st.markdown(
        '<div class="hero"><div class="eyebrow">🔴 &nbsp; A STUDENT GALLERY CONCEPT</div>'
        '<h1>Made here.<br><span class="red">Shared with pride.</span></h1>'
        '<p>A place for Union students to show the art they make. Put your work out there under an artist name you choose.</p>'
        '<p>◇ &nbsp; No real name needed. Keep your personal details private.</p></div>',
        unsafe_allow_html=True,
    )
with right:
    st.markdown(
        '<div class="poster"><div class="poster-head"><span>Union · student work</span><span>01—∞</span></div>'
        '<div class="poster-paper"><span class="poster-caption">The wall is yours</span>'
        '<div class="poster-art"><span class="sun"></span></div>'
        '<div class="poster-caption">Your art goes here</div></div>'
        '<div class="poster-foot"><span>Home of the Spartans</span><span>Rosehill, NC</span></div></div>',
        unsafe_allow_html=True,
    )

gallery_tab, submit_tab, rules_tab = st.tabs(["The gallery", "Share your art", "Community rules"])

if "artworks" not in st.session_state:
    st.session_state.artworks = []

with gallery_tab:
    st.markdown('<div class="label">THE GALLERY</div>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-size:clamp(32px,4vw,46px)">The wall starts<br>with <span class="red">you.</span></h2>', unsafe_allow_html=True)
    st.markdown('<p class="muted">A spot for sketches, photos, paintings, and ideas made by Union students.</p>', unsafe_allow_html=True)
    if not st.session_state.artworks:
        st.markdown(
            '<div class="empty"><div class="label" style="color:#df1733">NO ARTWORKS YET</div>'
            '<h3>Every gallery has a first piece.</h3>'
            '<p class="muted">Choose a favorite work and preview how it could look on the wall.</p></div>',
            unsafe_allow_html=True,
        )
        st.info("Choose **Share your art** above to add the first preview.")
    else:
        cols = st.columns(3)
        for i, artwork in enumerate(reversed(st.session_state.artworks)):
            with cols[i % 3]:
                st.image(artwork["image"], use_container_width=True)
                st.subheader(artwork["title"])
                st.caption(f'By {artwork["artist"]}')

with submit_tab:
    intro, formcol = st.columns([0.85, 1.15], gap="large")
    with intro:
        st.markdown('<div class="label">YOUR TURN</div>', unsafe_allow_html=True)
        st.markdown('<h2 style="font-size:clamp(32px,4vw,46px)">Put your<br><span class="red">work on the wall.</span></h2>', unsafe_allow_html=True)
        st.write("Pick an image and tell us what to call you. Use an artist name or nickname instead of your real name.")
        st.warning("Your name, your choice. Please don't add real names, phone numbers, or other personal details to artwork or titles.")
    with formcol:
        st.subheader("01  Add your artwork")
        st.caption("PREVIEW ONLY · Nothing is publicly uploaded.")
        with st.form("artwork_form", clear_on_submit=True):
            uploaded = st.file_uploader("Choose an image (JPG, PNG, or WEBP; max 10 MB)", type=["jpg", "jpeg", "png", "webp"])
            title = st.text_input("Artwork title (optional)", max_chars=70, placeholder="Give it a name")
            artist = st.text_input("Artist name (optional)", max_chars=40, placeholder="Nickname or artist name")
            permission = st.checkbox("I made this artwork or have permission to share it, and it follows the community rules.")
            submitted = st.form_submit_button("Preview my artwork →", use_container_width=True)
        if submitted:
            if uploaded is None:
                st.error("Choose an image first.")
            elif uploaded.size > 10 * 1024 * 1024:
                st.error("Please choose an image under 10 MB.")
            elif not permission:
                st.error("Please confirm that you have permission to share this artwork.")
            else:
                st.session_state.artworks.append({
                    "image": uploaded.getvalue(),
                    "title": title.strip() or "Untitled artwork",
                    "artist": artist.strip() or "Anonymous artist",
                })
                st.success("Preview added. Open the gallery tab to see it.")
        st.caption("Demo limitation: previews are temporary and are not saved permanently or shared with other visitors.")

with rules_tab:
    st.markdown('<div class="label">A GOOD WALL MAKES ROOM FOR EVERYONE</div>', unsafe_allow_html=True)
    st.markdown('<h2 style="font-size:clamp(32px,4vw,46px)">Keep it creative.<br><span class="red">Keep it respectful.</span></h2>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="rulebox"><b>01 · Make it yours to share.</b><br>Post work you created or have permission to share.</div>', unsafe_allow_html=True)
        st.markdown('<div class="rulebox"><b>03 · Respect people’s privacy.</b><br>Use an artist name and leave out private information.</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="rulebox"><b>02 · No violence or illegal material.</b><br>Do not post content promoting threats or illegal activity.</div>', unsafe_allow_html=True)
        st.markdown('<div class="rulebox"><b>04 · Make space for classmates.</b><br>No harassment or content that targets or humiliates another person.</div>', unsafe_allow_html=True)
    st.info("This is a concept demo, not a live school submission or moderation service. The school should approve and moderate any public gallery before launch.")

st.markdown("---")
st.caption("Union High School · Student Art Wall concept · Student privacy comes first.")

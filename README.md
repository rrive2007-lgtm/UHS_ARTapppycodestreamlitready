# Union High School Student Art Wall — Streamlit project

## Upload these files to GitHub
Put these files directly in the repository's root (the main page, not inside another folder):
- `app.py`
- `requirements.txt`
- `union-logo.png`

## Deploy on Streamlit Community Cloud
1. Open https://share.streamlit.io/
2. Choose **Create app**.
3. Repository: your GitHub repository, e.g. `your-user/your-repository` (do not add `/tree/main`).
4. Branch: `main` (or the actual branch name shown on GitHub).
5. Main file path: `app.py`.
6. Click Deploy.

`requirements.txt` contains one dependency per real line. It must not contain literal `\n` characters.

## Demo features
- Responsive school-themed layout and Spartan logo
- Gallery, artwork submission, and community rules tabs
- Image upload with file type and 10 MB limit
- Optional title and artist alias; blank artist name displays as Anonymous artist
- Preview submissions in the current Streamlit session

## Limitations
This is a prototype. Upload previews are temporary and are not saved to a permanent database or shared among visitors. Before real school use, add persistent storage, a moderation workflow, suitable access controls, and school approval. Avoid collecting unnecessary personal information from students.

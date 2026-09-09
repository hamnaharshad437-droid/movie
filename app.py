"""
🎬 MOVIE HUB - Modern Movie Discovery Web Application
Single-file self-contained application for effortless local running and Streamlit Cloud deployment.
Requires only: streamlit, requests, pandas
"""

import os
import requests
import streamlit as st
import pandas as pd
from typing import Optional, Dict, Any, List

# ==============================================================================
# 1. PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Movie Hub | Discover. Explore. Watch.",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================================================================
# 2. DESIGN THEME & CUSTOM CSS (Dark Blue + Black Palette)
# ==============================================================================
st.markdown(
    """
    <style>
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Playfair+Display:wght@600;700&display=swap');

:root {
    --bg-main: #07090D;
    --bg-secondary: #0D1118;
    --bg-card: #111720;
    --bg-card-soft: #151C26;
    --primary-blue: #193B5A;
    --accent-blue: #4E9FE6;
    --bright-blue: #79BDF2;
    --text-white: #F5F7FA;
    --text-muted: #9BA7B5;
    --border-subtle: #27313D;
    --border-soft: #1C2530;
    --badge-gold: #D7A84B;
    --danger: #C86A6A;
}

html, body, [class*="css"] {
    font-family: 'Manrope', -apple-system, BlinkMacSystemFont, sans-serif;
    background: var(--bg-main) !important;
    color: var(--text-white) !important;
}

body {
    letter-spacing: 0.01em;
}

.block-container {
    padding-top: 2rem !important;
    padding-bottom: 4rem !important;
    max-width: 1380px !important;
}

/* Remove Streamlit chrome that makes the app feel like a prototype */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header[data-testid="stHeader"] {
    background: rgba(7, 9, 13, 0.88) !important;
}
div[data-testid="stToolbar"] { display: none; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0B0F15 !important;
    border-right: 1px solid var(--border-soft) !important;
}

section[data-testid="stSidebar"] .block-container {
    padding: 1.6rem 1.15rem 2rem !important;
}

section[data-testid="stSidebar"] [data-testid="stRadio"] > label {
    display: none;
}

section[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 4px;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label {
    border-radius: 8px !important;
    padding: 9px 11px !important;
    color: #AAB4C0 !important;
    transition: background 0.18s ease, color 0.18s ease;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background: #151B24 !important;
    color: #F5F7FA !important;
}

section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
    background: #182331 !important;
    color: #F5F7FA !important;
    box-shadow: inset 3px 0 0 var(--accent-blue);
}

section[data-testid="stSidebar"] hr {
    border-color: var(--border-soft) !important;
}

/* Brand */
.brand-container {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 0 0 1.25rem;
    margin-bottom: 1.25rem;
    border-bottom: 1px solid var(--border-soft);
}

.brand-icon {
    font-size: 1.35rem;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 9px;
    background: #162B3E;
    border: 1px solid #2B526F;
    box-shadow: none;
}

.brand-title {
    font-size: 1.2rem;
    font-weight: 800;
    letter-spacing: 1.8px;
    color: #F5F7FA;
    line-height: 1.1;
}

.brand-subtitle {
    font-size: 0.67rem;
    color: #7396B3;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    font-weight: 700;
    margin-top: 3px;
}

/* Buttons */
.stButton > button {
    background: #17212D !important;
    color: #EAF0F5 !important;
    border: 1px solid #2B3745 !important;
    border-radius: 7px !important;
    min-height: 38px !important;
    padding: 0.42rem 0.95rem !important;
    font-weight: 700 !important;
    font-size: 0.86rem !important;
    transition: all 0.18s ease !important;
    box-shadow: none !important;
}

.stButton > button:hover {
    background: #203143 !important;
    border-color: #4B7594 !important;
    color: #F5F7FA !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 5px 16px rgba(0,0,0,0.28) !important;
}

.stButton > button[kind="primary"] {
    background: #2A628F !important;
    border-color: #3979A9 !important;
    color: #F5F7FA !important;
}

.stButton > button[kind="primary"]:hover {
    background: #3478A9 !important;
    border-color: #5A9BC6 !important;
}

.stButton > button[kind="secondary"] {
    background: #121922 !important;
    border-color: #2B3745 !important;
    color: #C7D0D9 !important;
}

/* Inputs */
.stTextInput > div > div > input,
.stSelectbox > div > div,
.stMultiSelect > div > div,
.stNumberInput > div > div > input {
    background: #10161E !important;
    border: 1px solid #293440 !important;
    color: #F5F7FA !important;
    border-radius: 7px !important;
}

.stTextInput > div > div > input:focus {
    border-color: #4D86AA !important;
    box-shadow: 0 0 0 1px #4D86AA !important;
}

[data-baseweb="select"] > div {
    background: #10161E !important;
    border-color: #293440 !important;
}

[data-baseweb="popover"],
[data-baseweb="menu"] {
    background: #121922 !important;
    border: 1px solid #293440 !important;
}

[data-baseweb="menu"] li:hover {
    background: #1B2835 !important;
}

/* Slider */
.stSlider [data-baseweb="slider"] [role="slider"] {
    background: #79BDF2 !important;
}

/* Headings */
h1, h2, h3 {
    color: #F5F7FA !important;
    letter-spacing: -0.025em;
}

h1 {
    font-weight: 800 !important;
}

h2, h3 {
    font-weight: 750 !important;
}

.stMarkdown p {
    color: #B5BEC9;
}

/* Movie cards */
.movie-card-container {
    background: #10161E;
    border: 1px solid #202B36;
    border-radius: 8px;
    overflow: hidden;
    transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
    margin-bottom: 0.65rem;
    position: relative;
}

.movie-card-container:hover {
    transform: translateY(-4px);
    border-color: #3E6078;
    box-shadow: 0 12px 28px rgba(0,0,0,0.38);
}

.movie-poster-wrap {
    position: relative;
    width: 100%;
    padding-top: 150%;
    overflow: hidden;
    background: #080B10;
}

.movie-poster-img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease, filter 0.3s ease;
}

.movie-card-container:hover .movie-poster-img {
    transform: scale(1.035);
    filter: brightness(1.05);
}

.movie-card-content {
    padding: 12px 13px 13px;
}

.movie-card-title {
    font-size: 0.92rem;
    font-weight: 750;
    color: #F2F5F7;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    margin-bottom: 5px;
}

.movie-card-meta {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 0.77rem;
    color: #8F9BA8;
    margin-bottom: 7px;
}

.rating-badge {
    background: rgba(215, 168, 75, 0.10);
    border: 1px solid rgba(215, 168, 75, 0.30);
    color: #E0B861;
    font-weight: 800;
    font-size: 0.74rem;
    padding: 2px 7px;
    border-radius: 5px;
    display: inline-flex;
    align-items: center;
    gap: 3px;
}

.genre-pill {
    background: #192B3A;
    color: #9FC6E3;
    border: 1px solid #294255;
    font-size: 0.68rem;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 4px;
    display: inline-block;
    white-space: nowrap;
}

/* Hero */
.hero-banner {
    position: relative;
    width: 100%;
    border-radius: 10px;
    overflow: hidden;
    background: #10161E;
    border: 1px solid #202B36;
    margin-bottom: 1.6rem;
    box-shadow: 0 18px 40px rgba(0,0,0,0.42);
}

.hero-backdrop {
    width: 100%;
    height: 450px;
    object-fit: cover;
    display: block;
    filter: saturate(0.92);
}

.hero-overlay {
    position: absolute;
    inset: 0;
    background:
        linear-gradient(90deg, rgba(7,9,13,0.97) 0%, rgba(7,9,13,0.83) 36%, rgba(7,9,13,0.22) 78%, rgba(7,9,13,0.05) 100%),
        linear-gradient(0deg, rgba(7,9,13,0.94) 0%, rgba(7,9,13,0.22) 52%, transparent 100%);
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 2.25rem 2.6rem;
}

.hero-tagline {
    color: #82A9C5;
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 2.2px;
    font-weight: 800;
    margin-bottom: 7px;
}

.hero-title {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 2.9rem;
    font-weight: 700;
    color: #F5F7FA;
    line-height: 1.1;
    margin-bottom: 12px;
    text-shadow: 0 3px 18px rgba(0,0,0,0.65);
}

.hero-meta {
    display: flex;
    align-items: center;
    gap: 14px;
    font-size: 0.84rem;
    color: #AAB4BF;
    margin-bottom: 13px;
}

.hero-overview {
    max-width: 670px;
    font-size: 0.9rem;
    line-height: 1.65;
    color: #D2D8DE;
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    margin-bottom: 16px;
}

/* Detail page */
.details-backdrop-header {
    position: relative;
    width: 100%;
    height: 390px;
    border-radius: 10px;
    overflow: hidden;
    margin-bottom: 1.7rem;
    border: 1px solid #202B36;
}

.details-backdrop-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: saturate(0.88);
}

.details-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(to top, #07090D 7%, rgba(7,9,13,0.68) 55%, rgba(7,9,13,0.18) 100%);
}

.stat-card {
    background: #10161E;
    border: 1px solid #222D38;
    border-radius: 7px;
    padding: 0.9rem 1rem;
    margin-bottom: 0.9rem;
}

.stat-label {
    font-size: 0.68rem;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    color: #8995A2;
    margin-bottom: 5px;
    font-weight: 700;
}

.stat-val {
    font-size: 1.05rem;
    font-weight: 750;
    color: #F2F5F7;
}

.cast-card {
    background: #10161E;
    border: 1px solid #222D38;
    border-radius: 7px;
    overflow: hidden;
    text-align: center;
    padding-bottom: 9px;
    transition: transform 0.18s ease, border-color 0.18s ease;
}

.cast-card:hover {
    transform: translateY(-3px);
    border-color: #3E6078;
}

.cast-img {
    width: 100%;
    height: 155px;
    object-fit: cover;
    background: #080B10;
}

.cast-name {
    font-size: 0.8rem;
    font-weight: 750;
    color: #F1F4F6;
    margin-top: 7px;
    padding: 0 4px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.cast-char {
    font-size: 0.7rem;
    color: #8995A2;
    padding: 0 4px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* Tabs, alerts and expanders */
button[data-baseweb="tab"] {
    color: #8F9BA8 !important;
    font-weight: 700 !important;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #D9E6EF !important;
}

div[data-testid="stAlert"] {
    background: #111922 !important;
    border: 1px solid #293744 !important;
    color: #C6D0D9 !important;
}

details {
    border-color: #293440 !important;
    background: #0F151D !important;
}

.stProgress > div > div > div {
    background: #4E9FE6 !important;
}

/* Mobile */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem 0.8rem 3rem !important;
    }

    .hero-backdrop {
        height: 360px;
    }

    .hero-overlay {
        padding: 1.35rem;
    }

    .hero-title {
        font-size: 2rem;
    }

    .details-backdrop-header {
        height: 280px;
    }
}
</style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 3. TMDB API CONSTANTS & CURATED DEMO DATASET
# ==============================================================================
TMDB_BASE_URL = "https://api.themoviedb.org/3"
TMDB_IMAGE_BASE = "https://image.tmdb.org/t/p"
POSTER_PLACEHOLDER = "https://placehold.co/500x750/0b1628/2d8cff?text=No+Poster+Available"
BACKDROP_PLACEHOLDER = "https://placehold.co/1280x720/08111f/1677ff?text=Movie+Hub"
PROFILE_PLACEHOLDER = "https://placehold.co/185x278/0b1628/a7b0c0?text=Actor"

GENRES_FALLBACK: Dict[int, str] = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    14: "Fantasy",
    36: "History",
    27: "Horror",
    10402: "Music",
    9648: "Mystery",
    10749: "Romance",
    878: "Science Fiction",
    10770: "TV Movie",
    53: "Thriller",
    10752: "War",
    37: "Western",
}

DEMO_MOVIES: List[Dict[str, Any]] = [
    {
        "id": 693134,
        "title": "Dune: Part Two",
        "tagline": "Long live the fighters.",
        "overview": "Follow the mythic journey of Paul Atreides as he unites with Chani and the Fremen while on a warpath of revenge against the conspirators who destroyed his family. Facing a choice between the love of his life and the fate of the known universe, he endeavors to prevent a terrible future only he can foresee.",
        "poster_path": "/1pdfLvkbY9ohJlCjQH2CZjjYVvJ.jpg",
        "backdrop_path": "/xOMo8BRK7PfcJv9JCnx7s520DRq.jpg",
        "release_date": "2024-02-27",
        "vote_average": 8.2,
        "vote_count": 5300,
        "genre_ids": [878, 12],
        "genres": [{"id": 878, "name": "Science Fiction"}, {"id": 12, "name": "Adventure"}],
        "runtime": 166,
        "original_language": "en",
        "budget": 190000000,
        "revenue": 711844358,
        "director": "Denis Villeneuve",
        "cast": [
            {"name": "Timothée Chalamet", "character": "Paul Atreides", "profile_path": "/BE2sdjpgsa2rNTFa66f7upkaOP.jpg"},
            {"name": "Zendaya", "character": "Chani", "profile_path": "/so3PFVR1btjhkB1Lj0gqcb1FSjF.jpg"},
            {"name": "Rebecca Ferguson", "character": "Lady Jessica", "profile_path": "/4W1sHdQk4aWjY94i5vKxJ2n0wF3.jpg"},
            {"name": "Javier Bardem", "character": "Stilgar", "profile_path": "/6N915g0fKovF42kS8Z2U1Uq83kH.jpg"},
        ],
        "trailer_key": "Way9Dexny3w",
        "category": "trending",
    },
    {
        "id": 157336,
        "title": "Interstellar",
        "tagline": "Mankind was born on Earth. It was never meant to die here.",
        "overview": "The adventures of a group of explorers who make use of a newly discovered wormhole to surpass the limitations on human space travel and conquer the vast distances involved in an interstellar voyage.",
        "poster_path": "/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
        "backdrop_path": "/xJHokMbljvjADYdit5fK5VQsXEG.jpg",
        "release_date": "2014-11-05",
        "vote_average": 8.4,
        "vote_count": 34500,
        "genre_ids": [12, 18, 878],
        "genres": [{"id": 12, "name": "Adventure"}, {"id": 18, "name": "Drama"}, {"id": 878, "name": "Science Fiction"}],
        "runtime": 169,
        "original_language": "en",
        "budget": 165000000,
        "revenue": 731000000,
        "director": "Christopher Nolan",
        "cast": [
            {"name": "Matthew McConaughey", "character": "Joseph Cooper", "profile_path": "/sY2mwpafcwqyYS1siiSuXZY9RsZ.jpg"},
            {"name": "Anne Hathaway", "character": "Dr. Amelia Brand", "profile_path": "/tLelKoPNiyJCSEtQT81FGg4fXgH.jpg"},
            {"name": "Jessica Chastain", "character": "Murphy Cooper", "profile_path": "/nkCp9U6Lz7p8oGj3k8Z1K82j0wM.jpg"},
            {"name": "Michael Caine", "character": "Professor John Brand", "profile_path": "/klNxkH15u2yN492i0oK5J98j0wF.jpg"},
        ],
        "trailer_key": "zSWdZVtXT7E",
        "category": "top_rated",
    },
    {
        "id": 27205,
        "title": "Inception",
        "tagline": "Your mind is the scene of the crime.",
        "overview": "Cobb, a skilled thief who steals corporate secrets through the use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster.",
        "poster_path": "/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg",
        "backdrop_path": "/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg",
        "release_date": "2010-07-15",
        "vote_average": 8.4,
        "vote_count": 36000,
        "genre_ids": [28, 878, 12],
        "genres": [{"id": 28, "name": "Action"}, {"id": 878, "name": "Science Fiction"}, {"id": 12, "name": "Adventure"}],
        "runtime": 148,
        "original_language": "en",
        "budget": 160000000,
        "revenue": 836836967,
        "director": "Christopher Nolan",
        "cast": [
            {"name": "Leonardo DiCaprio", "character": "Dom Cobb", "profile_path": "/wo2hJpn04vbtmh0B9utCFdsQhxM.jpg"},
            {"name": "Joseph Gordon-Levitt", "character": "Arthur", "profile_path": "/dhv9V6uI8e974Q4lQ64hG73j0wF.jpg"},
            {"name": "Elliot Page", "character": "Ariadne", "profile_path": "/tpjh802HwJ71k9X7e9Hk0K82j0wF.jpg"},
            {"name": "Tom Hardy", "character": "Eames", "profile_path": "/yVGF93v078f4v1M1r3B0y4N7e7H.jpg"},
        ],
        "trailer_key": "YoHD9XEInc0",
        "category": "popular",
    },
    {
        "id": 155,
        "title": "The Dark Knight",
        "tagline": "Welcome to a world without rules.",
        "overview": "Batman raises the stakes in his war on crime. With the help of Lt. Jim Gordon and District Attorney Harvey Dent, Batman sets out to dismantle the remaining criminal organizations that plague the streets.",
        "poster_path": "/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        "backdrop_path": "/nMKdUUepR0i5zn0y1T4CsSB5chy.jpg",
        "release_date": "2008-07-16",
        "vote_average": 8.5,
        "vote_count": 32000,
        "genre_ids": [18, 28, 80, 53],
        "genres": [{"id": 18, "name": "Drama"}, {"id": 28, "name": "Action"}, {"id": 80, "name": "Crime"}, {"id": 53, "name": "Thriller"}],
        "runtime": 152,
        "original_language": "en",
        "budget": 185000000,
        "revenue": 1004558444,
        "director": "Christopher Nolan",
        "cast": [
            {"name": "Christian Bale", "character": "Bruce Wayne / Batman", "profile_path": "/b7fTC9WFkgq6EONCFr4Tbg1587v.jpg"},
            {"name": "Heath Ledger", "character": "Joker", "profile_path": "/5Y9HnYYa9jF4D08g0v9K82j0wM.jpg"},
            {"name": "Aaron Eckhart", "character": "Harvey Dent", "profile_path": "/9v88fN08u3Y7uN74p4L5g0wM.jpg"},
        ],
        "trailer_key": "EXeTwQWrcwY",
        "category": "top_rated",
    },
    {
        "id": 569094,
        "title": "Spider-Man: Across the Spider-Verse",
        "tagline": "It's how you wear the mask that matters.",
        "overview": "After reuniting with Gwen Stacy, Brooklyn’s full-time Spider-Man is catapulted across the Multiverse, encountering the Spider Society charged with protecting existence itself.",
        "poster_path": "/8Vt6mWEReuy4Of61Lnj5Xj704m8.jpg",
        "backdrop_path": "/4HodYYKEIsGOdinkGi2Ucz6X9i0.jpg",
        "release_date": "2023-05-31",
        "vote_average": 8.4,
        "vote_count": 6800,
        "genre_ids": [16, 28, 12, 878],
        "genres": [{"id": 16, "name": "Animation"}, {"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}],
        "runtime": 140,
        "original_language": "en",
        "budget": 100000000,
        "revenue": 690516673,
        "director": "Joaquim Dos Santos",
        "cast": [
            {"name": "Shameik Moore", "character": "Miles Morales (voice)", "profile_path": "/uMC1n4fMhY0K82j0wM.jpg"},
            {"name": "Hailee Steinfeld", "character": "Gwen Stacy (voice)", "profile_path": "/wj9Hj0K82j0wM498fN.jpg"},
        ],
        "trailer_key": "cqGjhVJWtEg",
        "category": "popular",
    },
    {
        "id": 872585,
        "title": "Oppenheimer",
        "tagline": "The world forever changes.",
        "overview": "The story of J. Robert Oppenheimer's role in the development of the atomic bomb during World War II, exploring ambition, moral dilemmas, and the dawn of the nuclear era.",
        "poster_path": "/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
        "backdrop_path": "/fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg",
        "release_date": "2023-07-19",
        "vote_average": 8.1,
        "vote_count": 9200,
        "genre_ids": [18, 36],
        "genres": [{"id": 18, "name": "Drama"}, {"id": 36, "name": "History"}],
        "runtime": 180,
        "original_language": "en",
        "budget": 100000000,
        "revenue": 957000000,
        "director": "Christopher Nolan",
        "cast": [
            {"name": "Cillian Murphy", "character": "J. Robert Oppenheimer", "profile_path": "/360cpvgKT99qlNToqxhzHGQhKzy.jpg"},
            {"name": "Emily Blunt", "character": "Kitty Oppenheimer", "profile_path": "/nPJdtVuWuR5rZsAooR37nL1v1T.jpg"},
        ],
        "trailer_key": "uYPbbksJxIg",
        "category": "top_rated",
    },
    {
        "id": 129,
        "title": "Spirited Away",
        "tagline": "Tunnel to the world of wonder.",
        "overview": "A young girl, Chihiro, becomes trapped in a strange new world of spirits. When her parents undergo a mysterious transformation, she must call upon her courage to free them.",
        "poster_path": "/393mhqrL0tjxqaqplvr594gQvWj.jpg",
        "backdrop_path": "/Ab8mkHmkYADjU7wQiOkia9BzGvS.jpg",
        "release_date": "2001-07-20",
        "vote_average": 8.5,
        "vote_count": 16000,
        "genre_ids": [16, 14, 10751],
        "genres": [{"id": 16, "name": "Animation"}, {"id": 14, "name": "Fantasy"}],
        "runtime": 125,
        "original_language": "ja",
        "budget": 19000000,
        "revenue": 395580000,
        "director": "Hayao Miyazaki",
        "cast": [
            {"name": "Rumi Hiiragi", "character": "Chihiro (voice)", "profile_path": "/5ZgL3M9K0wF498fN.jpg"},
        ],
        "trailer_key": "ByXuk9QqQkk",
        "category": "top_rated",
    },
    {
        "id": 496243,
        "title": "Parasite",
        "tagline": "Act like you own the place.",
        "overview": "All unemployed, Ki-taek's family takes peculiar interest in the wealthy Parks for their livelihood until they get entangled in an unexpected incident.",
        "poster_path": "/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg",
        "backdrop_path": "/hiKmpZMGZsrkA3cdce8a7Dpos1j.jpg",
        "release_date": "2019-05-30",
        "vote_average": 8.5,
        "vote_count": 17800,
        "genre_ids": [35, 53, 18],
        "genres": [{"id": 35, "name": "Comedy"}, {"id": 53, "name": "Thriller"}, {"id": 18, "name": "Drama"}],
        "runtime": 133,
        "original_language": "ko",
        "budget": 11400000,
        "revenue": 263136741,
        "director": "Bong Joon-ho",
        "cast": [
            {"name": "Song Kang-ho", "character": "Kim Ki-taek", "profile_path": "/b4iP4K5g0wM498fN.jpg"},
        ],
        "trailer_key": "5xH0R_fxysQ",
        "category": "top_rated",
    },
    {
        "id": 823464,
        "title": "Godzilla x Kong: The New Empire",
        "tagline": "Rise together or fall alone.",
        "overview": "Godzilla and Kong must reunite against a colossal undiscovered threat hidden within our world that challenges their very existence – and our own.",
        "poster_path": "/tMefBSflR6PGQLv7WvFPpKLZkyk.jpg",
        "backdrop_path": "/qrGtVFxaD8c7et0j3hxYvNdJNu8.jpg",
        "release_date": "2024-03-27",
        "vote_average": 7.2,
        "vote_count": 3600,
        "genre_ids": [28, 878, 12],
        "genres": [{"id": 28, "name": "Action"}, {"id": 878, "name": "Science Fiction"}],
        "runtime": 115,
        "original_language": "en",
        "budget": 135000000,
        "revenue": 567650016,
        "director": "Adam Wingard",
        "cast": [
            {"name": "Rebecca Hall", "character": "Dr. Andrews", "profile_path": "/uMC1n4fMhY0K82j0wM.jpg"},
        ],
        "trailer_key": "lV1OOlGwExM",
        "category": "now_playing",
    },
    {
        "id": 1022789,
        "title": "Inside Out 2",
        "tagline": "Make room for new emotions.",
        "overview": "Teenager Riley's mind headquarters is undergoing a sudden demolition to make room for something unexpected: new Emotions including Anxiety, Envy, and Embarrassment.",
        "poster_path": "/vpnVM9B6NMmQpWeZvzLvDESb2QY.jpg",
        "backdrop_path": "/xg27NrXi7VXCGUr7MG75UqLl6Vg.jpg",
        "release_date": "2024-06-11",
        "vote_average": 7.6,
        "vote_count": 4500,
        "genre_ids": [16, 10751, 35],
        "genres": [{"id": 16, "name": "Animation"}, {"id": 10751, "name": "Family"}, {"id": 35, "name": "Comedy"}],
        "runtime": 96,
        "original_language": "en",
        "budget": 200000000,
        "revenue": 1690000000,
        "director": "Kelsey Mann",
        "cast": [
            {"name": "Amy Poehler", "character": "Joy (voice)", "profile_path": "/uMC1n4fMhY0K82j0wM.jpg"},
            {"name": "Maya Hawke", "character": "Anxiety (voice)", "profile_path": "/wj9Hj0K82j0wM498fN.jpg"},
        ],
        "trailer_key": "LEjhY15eCx0",
        "category": "upcoming",
    },
    {
        "id": 533535,
        "title": "Deadpool & Wolverine",
        "tagline": "Come together.",
        "overview": "A listless Wade Wilson toils in civilian life. But when his homeworld faces existential annihilation, Wade must reluctantly suit-up with an even more reluctant Wolverine.",
        "poster_path": "/8cdWjvZQUExUUTzyp4t6EDMubfO.jpg",
        "backdrop_path": "/9l1eZiJHmhr5jA625egvdngzqPI.jpg",
        "release_date": "2024-07-24",
        "vote_average": 7.7,
        "vote_count": 4800,
        "genre_ids": [28, 35, 878],
        "genres": [{"id": 28, "name": "Action"}, {"id": 35, "name": "Comedy"}],
        "runtime": 128,
        "original_language": "en",
        "budget": 200000000,
        "revenue": 1337000000,
        "director": "Shawn Levy",
        "cast": [
            {"name": "Ryan Reynolds", "character": "Deadpool", "profile_path": "/uMC1n4fMhY0K82j0wM.jpg"},
            {"name": "Hugh Jackman", "character": "Wolverine", "profile_path": "/wj9Hj0K82j0wM498fN.jpg"},
        ],
        "trailer_key": "73_1biulkYk",
        "category": "now_playing",
    }
]

# ==============================================================================
# 4. API HELPER METHODS
# ==============================================================================
def get_api_key() -> Optional[str]:
    """Resolve TMDB API key from session, secrets, or environment."""
    if "tmdb_api_key" in st.session_state and st.session_state.tmdb_api_key:
        candidate = st.session_state.tmdb_api_key.strip()
        if candidate:
            return candidate

    try:
        if "TMDB_API_KEY" in st.secrets:
            key = str(st.secrets["TMDB_API_KEY"]).strip()
            if key and key != "your_tmdb_api_key_here":
                return key
    except Exception:
        pass

    env_key = os.environ.get("TMDB_API_KEY", "").strip()
    if env_key and env_key != "your_tmdb_api_key_here":
        return env_key

    return None

def is_api_configured() -> bool:
    key = get_api_key()
    return key is not None and len(key) >= 10

def get_poster_url(poster_path: Optional[str]) -> str:
    if not poster_path:
        return POSTER_PLACEHOLDER
    if poster_path.startswith("http"):
        return poster_path
    return f"{TMDB_IMAGE_BASE}/w500{poster_path}"

def get_backdrop_url(backdrop_path: Optional[str]) -> str:
    if not backdrop_path:
        return BACKDROP_PLACEHOLDER
    if backdrop_path.startswith("http"):
        return backdrop_path
    return f"{TMDB_IMAGE_BASE}/w1280{backdrop_path}"

def get_profile_url(profile_path: Optional[str]) -> str:
    if not profile_path:
        return PROFILE_PLACEHOLDER
    if profile_path.startswith("http"):
        return profile_path
    return f"{TMDB_IMAGE_BASE}/w185{profile_path}"

def format_runtime(minutes: Optional[int]) -> str:
    if not minutes or minutes <= 0:
        return "N/A"
    hrs, mins = minutes // 60, minutes % 60
    return f"{hrs}h {mins}m" if hrs > 0 and mins > 0 else (f"{hrs}h" if hrs > 0 else f"{mins}m")

def format_currency(amount: Optional[int]) -> str:
    return f"${amount:,.0f}" if amount and amount > 0 else "Not disclosed"

def format_release_year(release_date: Optional[str]) -> str:
    return release_date[:4] if release_date and len(release_date) >= 4 else "TBA"

def _make_tmdb_request(endpoint: str, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
    api_key = get_api_key()
    if not api_key:
        return None
    req_params = {"api_key": api_key, "language": "en-US"}
    if params:
        req_params.update(params)
    url = f"{TMDB_BASE_URL}/{endpoint.lstrip('/')}"
    try:
        resp = requests.get(url, params=req_params, timeout=7)
        if resp.status_code == 200:
            return resp.json()
    except Exception:
        pass
    return None

@st.cache_data(ttl=1800, show_spinner=False)
def get_genres() -> Dict[int, str]:
    if is_api_configured():
        data = _make_tmdb_request("genre/movie/list")
        if data and "genres" in data:
            return {g["id"]: g["name"] for g in data["genres"]}
    return GENRES_FALLBACK

@st.cache_data(ttl=1800, show_spinner=False)
def get_trending(time_window: str = "day") -> List[Dict[str, Any]]:
    if is_api_configured():
        data = _make_tmdb_request(f"trending/movie/{time_window}")
        if data and "results" in data:
            return data["results"]
    return [m for m in DEMO_MOVIES if m.get("category") in ["trending", "popular"]] or DEMO_MOVIES[:8]

@st.cache_data(ttl=1800, show_spinner=False)
def get_popular() -> List[Dict[str, Any]]:
    if is_api_configured():
        data = _make_tmdb_request("movie/popular")
        if data and "results" in data:
            return data["results"]
    return [m for m in DEMO_MOVIES if m.get("category") == "popular"] or DEMO_MOVIES[:10]

@st.cache_data(ttl=1800, show_spinner=False)
def get_top_rated() -> List[Dict[str, Any]]:
    if is_api_configured():
        data = _make_tmdb_request("movie/top_rated")
        if data and "results" in data:
            return data["results"]
    return [m for m in DEMO_MOVIES if m.get("category") == "top_rated"] or DEMO_MOVIES[:8]

@st.cache_data(ttl=1800, show_spinner=False)
def get_now_playing() -> List[Dict[str, Any]]:
    if is_api_configured():
        data = _make_tmdb_request("movie/now_playing")
        if data and "results" in data:
            return data["results"]
    return [m for m in DEMO_MOVIES if m.get("category") == "now_playing"] or DEMO_MOVIES[:8]

@st.cache_data(ttl=1800, show_spinner=False)
def get_upcoming() -> List[Dict[str, Any]]:
    if is_api_configured():
        data = _make_tmdb_request("movie/upcoming")
        if data and "results" in data:
            return data["results"]
    return [m for m in DEMO_MOVIES if m.get("category") == "upcoming"] or DEMO_MOVIES[-6:]

@st.cache_data(ttl=1800, show_spinner=False)
def search_movies(query: str) -> List[Dict[str, Any]]:
    if not query or not query.strip():
        return []
    clean_q = query.strip()
    if is_api_configured():
        data = _make_tmdb_request("search/movie", {"query": clean_q, "include_adult": "false"})
        if data and "results" in data:
            return data["results"]
    q_low = clean_q.lower()
    return [m for m in DEMO_MOVIES if q_low in m["title"].lower() or q_low in m.get("overview", "").lower()]

@st.cache_data(ttl=1800, show_spinner=False)
def get_movie_details(movie_id: int) -> Optional[Dict[str, Any]]:
    if is_api_configured():
        data = _make_tmdb_request(f"movie/{movie_id}", {"append_to_response": "credits,videos,similar"})
        if data and "id" in data:
            trailer_key = None
            if "videos" in data and "results" in data["videos"]:
                for v in data["videos"]["results"]:
                    if v.get("site") == "YouTube" and v.get("type") in ["Trailer", "Teaser"]:
                        trailer_key = v.get("key")
                        if v.get("official"):
                            break
            data["trailer_key"] = trailer_key
            director = "Unknown"
            cast_list = []
            if "credits" in data:
                for member in data["credits"].get("crew", []):
                    if member.get("job") == "Director":
                        director = member.get("name")
                        break
                for c in data["credits"].get("cast", [])[:10]:
                    cast_list.append({
                        "name": c.get("name"),
                        "character": c.get("character"),
                        "profile_path": c.get("profile_path")
                    })
            data["director"] = director
            data["cast"] = cast_list
            return data

    for m in DEMO_MOVIES:
        if m["id"] == movie_id:
            res = dict(m)
            res["similar"] = {"results": [sm for sm in DEMO_MOVIES if sm["id"] != movie_id][:6]}
            return res
    return None

@st.cache_data(ttl=1800, show_spinner=False)
def discover_movies(genre_id: Optional[int] = None, min_rating: Optional[float] = None, year: Optional[int] = None, sort_by: str = "popularity.desc") -> List[Dict[str, Any]]:
    if is_api_configured():
        params = {"sort_by": sort_by, "include_adult": "false"}
        if genre_id:
            params["with_genres"] = str(genre_id)
        if min_rating:
            params["vote_average.gte"] = min_rating
            params["vote_count.gte"] = 100
        if year:
            params["primary_release_year"] = year
        data = _make_tmdb_request("discover/movie", params)
        if data and "results" in data:
            return data["results"]

    results = list(DEMO_MOVIES)
    if genre_id:
        results = [m for m in results if genre_id in m.get("genre_ids", [])]
    if min_rating:
        results = [m for m in results if m.get("vote_average", 0) >= min_rating]
    if year:
        results = [m for m in results if m.get("release_date", "").startswith(str(year))]
    if sort_by == "vote_average.desc":
        results.sort(key=lambda x: x.get("vote_average", 0), reverse=True)
    return results

def get_similar_movies(movie_id: int, limit: int = 4) -> List[Dict[str, Any]]:
    details = get_movie_details(movie_id)
    if details and "similar" in details and "results" in details["similar"]:
        sims = [m for m in details["similar"]["results"] if m.get("id") != movie_id]
        if sims:
            return sims[:limit]
    return [m for m in DEMO_MOVIES if m.get("id") != movie_id][:limit]

# ==============================================================================
# 5. CONTENT-BASED RECOMMENDATION ENGINE
# ==============================================================================
MOOD_PRESETS = {
    "🔥 High-Octane Action": [28, 12, 53],
    "🧠 Mind-Bending Sci-Fi": [878, 9648],
    "😄 Feel-Good & Comedy": [35, 16, 10751],
    "🕵️ Dark Crime & Noir": [80, 18, 53],
    "🐉 Epic Fantasy Realms": [14, 12],
    "❤️ Romance & Heartfelt": [10749, 18],
    "👻 Horror & Thrills": [27, 53],
}

def get_recommendations_from_watchlist(watchlist: Dict[int, Dict[str, Any]], limit: int = 8) -> List[Dict[str, Any]]:
    if not watchlist:
        return []
    genre_freq: Dict[int, int] = {}
    saved_ids = set(watchlist.keys())
    for m in watchlist.values():
        for gid in m.get("genre_ids", []):
            genre_freq[gid] = genre_freq.get(gid, 0) + 1
    if not genre_freq:
        return [m for m in DEMO_MOVIES if m["id"] not in saved_ids][:limit]
    top_genre = sorted(genre_freq.items(), key=lambda x: x[1], reverse=True)[0][0]
    candidates = discover_movies(genre_id=top_genre, min_rating=7.0)
    unseen = [m for m in candidates if m["id"] not in saved_ids]
    return unseen[:limit] if unseen else [m for m in DEMO_MOVIES if m["id"] not in saved_ids][:limit]

# ==============================================================================
# 6. UI CARD & GRID RENDERERS
# ==============================================================================
def is_in_watchlist(movie_id: int) -> bool:
    return movie_id in st.session_state.get("watchlist", {})

def toggle_watchlist(movie: Dict[str, Any]):
    if "watchlist" not in st.session_state:
        st.session_state.watchlist = {}
    mid = movie["id"]
    if mid in st.session_state.watchlist:
        del st.session_state.watchlist[mid]
        st.toast(f"Removed '{movie.get('title')}' from Watchlist.", icon="🗑️")
    else:
        st.session_state.watchlist[mid] = movie
        st.toast(f"Added '{movie.get('title')}' to Watchlist!", icon="❤️")

def render_movie_card(movie: Dict[str, Any], key_prefix: str = ""):
    mid = movie.get("id")
    title = movie.get("title", "Untitled")
    poster = get_poster_url(movie.get("poster_path"))
    rating = movie.get("vote_average", 0.0)
    year = format_release_year(movie.get("release_date"))
    genres = get_genres()
    genre_name = ""
    if "genres" in movie and movie["genres"]:
        genre_name = movie["genres"][0]["name"]
    elif "genre_ids" in movie and movie["genre_ids"]:
        genre_name = genres.get(movie["genre_ids"][0], "")

    genre_pill = f'<span class="genre-pill">{genre_name}</span>' if genre_name else ""

    st.markdown(
        f"""
        <div class="movie-card-container">
            <div class="movie-poster-wrap">
                <img class="movie-poster-img" src="{poster}" alt="{title}" loading="lazy" />
            </div>
            <div class="movie-card-content">
                <div class="movie-card-title" title="{title}">{title}</div>
                <div class="movie-card-meta">
                    <span class="rating-badge">⭐ {rating:.1f}</span>
                    <span>{year}</span>
                </div>
                <div style="margin-top: 4px;">{genre_pill}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns([1.3, 1])
    with c1:
        if st.button("Details", key=f"{key_prefix}det_{mid}"):
            st.session_state.previous_page = st.session_state.get("current_page", "Home")
            st.session_state.selected_movie_id = mid
            st.rerun()
    with c2:
        saved = is_in_watchlist(mid)
        label = "❤️ Saved" if saved else "+ List"
        if st.button(label, key=f"{key_prefix}wl_{mid}", type="secondary" if saved else "primary"):
            toggle_watchlist(movie)
            st.rerun()

def render_movie_grid(movies: List[Dict[str, Any]], cols_per_row: int = 4, key_prefix: str = ""):
    if not movies:
        st.markdown(
            """
            <div style="text-align: center; padding: 2.5rem 1rem; color: #9BA7B5; background: #111720; border-radius: 12px; border: 1px dashed #27313D;">
                <div style="font-size: 2.5rem; margin-bottom: 8px;">🎬</div>
                <h3 style="color: #F5F7FA; margin-bottom: 4px;">No movies found</h3>
                <p>Try adjusting your search query, genre, or rating filters.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        return
    for i in range(0, len(movies), cols_per_row):
        row = movies[i:i + cols_per_row]
        cols = st.columns(cols_per_row)
        for idx, m in enumerate(row):
            with cols[idx]:
                render_movie_card(m, key_prefix=f"{key_prefix}r{i}_")

def render_hero(movie: Dict[str, Any]):
    if not movie:
        return
    mid = movie.get("id")
    title = movie.get("title", "Featured Film")
    backdrop = get_backdrop_url(movie.get("backdrop_path"))
    overview = movie.get("overview", "")
    rating = movie.get("vote_average", 0.0)
    year = format_release_year(movie.get("release_date"))
    tagline = movie.get("tagline", "FEATURED SELECTION")

    st.markdown(
        f"""
        <div class="hero-banner">
            <img class="hero-backdrop" src="{backdrop}" alt="{title}" />
            <div class="hero-overlay">
                <div class="hero-tagline">{tagline}</div>
                <div class="hero-title">{title}</div>
                <div class="hero-meta">
                    <span class="rating-badge">⭐ {rating:.1f}</span>
                    <span>📅 {year}</span>
                </div>
                <div class="hero-overview">{overview}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    b1, b2, b_space = st.columns([2, 2.2, 5.8])
    with b1:
        if st.button("🎬 View Details", key=f"hero_det_{mid}"):
            st.session_state.previous_page = st.session_state.get("current_page", "Home")
            st.session_state.selected_movie_id = mid
            st.rerun()
    with b2:
        saved = is_in_watchlist(mid)
        if st.button("✅ In Watchlist" if saved else "❤️ Add to Watchlist", key=f"hero_wl_{mid}", type="secondary" if saved else "primary"):
            toggle_watchlist(movie)
            st.rerun()

def render_movie_details(movie_id: int):
    movie = get_movie_details(movie_id)
    if not movie:
        st.error("Movie details not available.")
        if st.button("← Return to Browse"):
            st.session_state.selected_movie_id = None
            st.rerun()
        return

    # Back Navigation
    prev_page = st.session_state.get("previous_page", "Home")
    if st.button(f"← Back to {prev_page}", key="back_from_det_btn"):
        st.session_state.selected_movie_id = None
        st.rerun()

    # Backdrop & Details
    backdrop = get_backdrop_url(movie.get("backdrop_path"))
    poster = get_poster_url(movie.get("poster_path"))
    title = movie.get("title", "Untitled")
    tagline = movie.get("tagline", "")
    overview = movie.get("overview", "No synopsis provided.")
    rating = movie.get("vote_average", 0.0)
    vote_count = movie.get("vote_count", 0)
    release_date = movie.get("release_date", "TBA")
    runtime = format_runtime(movie.get("runtime"))
    director = movie.get("director", "Unknown")
    budget = format_currency(movie.get("budget"))
    revenue = format_currency(movie.get("revenue"))

    st.markdown(
        f"""
        <div class="details-backdrop-header">
            <img class="details-backdrop-img" src="{backdrop}" alt="{title}" />
            <div class="details-overlay"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c_post, c_info = st.columns([1, 2.2])
    with c_post:
        st.markdown(
            f"""
            <div style="border-radius: 12px; overflow: hidden; border: 2px solid #27313D; box-shadow: 0 10px 30px rgba(0,0,0,0.7); margin-top: -80px; position: relative; z-index: 10;">
                <img src="{poster}" alt="{title}" style="width: 100%; display: block;" />
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)
        saved = is_in_watchlist(movie_id)
        if st.button("✅ In Watchlist (Remove)" if saved else "❤️ Add to Watchlist", key="det_wl_toggle", type="secondary" if saved else "primary"):
            toggle_watchlist(movie)
            st.rerun()

    with c_info:
        st.markdown(f"<h1>{title}</h1>", unsafe_allow_html=True)
        if tagline:
            st.markdown(f"<p style='color: #79BDF2; font-style: italic; font-size: 1.05rem;'>\"{tagline}\"</p>", unsafe_allow_html=True)
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; gap: 14px; flex-wrap: wrap; margin-bottom: 16px;">
                <span class="rating-badge" style="font-size: 0.95rem; padding: 4px 10px;">⭐ {rating:.1f} ({vote_count:,} votes)</span>
                <span style="color: #9BA7B5;">📅 {release_date}</span>
                <span style="color: #9BA7B5;">⏱️ {runtime}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("### Overview")
        st.write(overview)

        m1, m2, m3 = st.columns(3)
        with m1:
            st.markdown(f'<div class="stat-card"><div class="stat-label">Director</div><div class="stat-val">{director}</div></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="stat-card"><div class="stat-label">Budget</div><div class="stat-val">{budget}</div></div>', unsafe_allow_html=True)
        with m3:
            st.markdown(f'<div class="stat-card"><div class="stat-label">Revenue</div><div class="stat-val">{revenue}</div></div>', unsafe_allow_html=True)

    st.divider()

    # Cast Section
    cast = movie.get("cast", [])
    if cast:
        st.markdown("### 🎭 Top Cast")
        cast_cols = st.columns(min(len(cast), 6))
        for idx, act in enumerate(cast[:6]):
            with cast_cols[idx]:
                p_url = get_profile_url(act.get("profile_path"))
                st.markdown(
                    f"""
                    <div class="cast-card">
                        <img class="cast-img" src="{p_url}" alt="{act.get('name')}" />
                        <div class="cast-name">{act.get('name')}</div>
                        <div class="cast-char">{act.get('character')}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        st.markdown("<br>", unsafe_allow_html=True)

    st.divider()

    # Official Trailer
    st.markdown("### 🎬 Official Trailer")
    if movie.get("trailer_key"):
        st.video(f"https://www.youtube.com/watch?v={movie['trailer_key']}")
    else:
        st.info("Official video trailer is not currently available for this title.")

    st.divider()

    # Similar Titles
    st.markdown("### 🎬 Similar Movies")
    render_movie_grid(get_similar_movies(movie_id, limit=4), cols_per_row=4, key_prefix="sim_")

# ==============================================================================
# 7. MAIN ROUTING & CONTROLLERS
# ==============================================================================
# State Initialization
if "watchlist" not in st.session_state:
    st.session_state.watchlist = {}
if "selected_movie_id" not in st.session_state:
    st.session_state.selected_movie_id = None
if "current_page" not in st.session_state:
    st.session_state.current_page = "🏠 Home"
if "previous_page" not in st.session_state:
    st.session_state.previous_page = "Home"
if "selected_genre_id" not in st.session_state:
    st.session_state.selected_genre_id = None
if "search_query" not in st.session_state:
    st.session_state.search_query = ""

# Sidebar Brand
st.sidebar.markdown(
    """
    <div class="brand-container">
        <div class="brand-icon">🎬</div>
        <div>
            <div class="brand-title">MOVIE HUB</div>
            <div class="brand-subtitle">Discover • Explore • Watch</div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

wl_count = len(st.session_state.watchlist)
wl_label = f"❤️ My Watchlist ({wl_count})" if wl_count > 0 else "❤️ My Watchlist"

NAV_ITEMS = [
    "🏠 Home",
    "🔥 Trending",
    "⭐ Popular",
    "🎬 Now Playing",
    "🏆 Top Rated",
    "🎭 Genres",
    "🔍 Search",
    wl_label,
    "🤖 Recommendations",
    "ℹ️ About",
]

# Find active index
active_idx = 0
for idx, opt in enumerate(NAV_ITEMS):
    if opt.split(" ")[0] == st.session_state.current_page.split(" ")[0]:
        active_idx = idx
        break

selected_nav = st.sidebar.radio("Nav", options=NAV_ITEMS, index=active_idx, label_visibility="collapsed")
base_nav = selected_nav.split(" (")[0]
if base_nav != st.session_state.current_page:
    st.session_state.current_page = base_nav
    st.session_state.selected_movie_id = None

st.sidebar.markdown("---")

# Sidebar TMDB Key Config
with st.sidebar.expander("🔑 TMDB API Key", expanded=not is_api_configured()):
    if is_api_configured():
        st.markdown(
            """
            <div style="background: rgba(22, 119, 255, 0.15); border: 1px solid #4E9FE6; padding: 10px; border-radius: 8px; font-size: 0.82rem;">
                🟢 <b>Live TMDB API Active</b><br>
                Connected to 800,000+ live movies.
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Reset API Key"):
            st.session_state.tmdb_api_key = ""
            st.rerun()
    else:
        st.markdown(
            """
            <div style="background: rgba(255, 184, 0, 0.1); border: 1px solid #D7A84B; padding: 10px; border-radius: 8px; font-size: 0.82rem; margin-bottom: 8px;">
                🟡 <b>Curated Demo Mode</b><br>
                Enter your free TMDB API key to query live movies.
            </div>
            """,
            unsafe_allow_html=True,
        )
        entered_key = st.text_input("TMDB API Key", type="password", placeholder="Paste API Key here...")
        if st.button("Connect"):
            if entered_key and len(entered_key.strip()) >= 10:
                st.session_state.tmdb_api_key = entered_key.strip()
                st.rerun()

st.sidebar.markdown("---")

# Downloadable Files Expander in App
with st.sidebar.expander("📥 Download App Files", expanded=False):
    st.markdown("<p style='font-size: 0.8rem; color: #9BA7B5;'>Download source files directly:</p>", unsafe_allow_html=True)
    try:
        with open(__file__, "r", encoding="utf-8") as f_app:
            app_code = f_app.read()
        st.download_button(
            label="📄 Download app.py",
            data=app_code,
            file_name="app.py",
            mime="text/x-python",
            key="dl_app_btn"
        )
    except Exception:
        pass

    req_text = "streamlit>=1.30.0\nrequests>=2.31.0\npandas>=2.0.0\n"
    st.download_button(
        label="📋 Download requirements.txt",
        data=req_text,
        file_name="requirements.txt",
        mime="text/plain",
        key="dl_req_btn"
    )

st.sidebar.markdown(
    """
    <div style="font-size: 0.75rem; color: #9BA7B5; text-align: center; margin-top: 2rem;">
        Powered by <b>The Movie Database</b><br>
        Movie Hub &copy; 2026
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------------------
# PAGE ROUTING
# ------------------------------------------------------------------------------
if st.session_state.selected_movie_id is not None:
    render_movie_details(st.session_state.selected_movie_id)

elif st.session_state.current_page == "🏠 Home":
    trending_list = get_trending(time_window="day")
    featured = trending_list[0] if trending_list else DEMO_MOVIES[0]
    render_hero(featured)

    st.markdown("### 🔥 Trending Now")
    render_movie_grid(get_trending("day")[:8], cols_per_row=4, key_prefix="h_trend_")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### ⭐ Popular Movies")
    render_movie_grid(get_popular()[:8], cols_per_row=4, key_prefix="h_pop_")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🏆 Top Rated")
    render_movie_grid(get_top_rated()[:8], cols_per_row=4, key_prefix="h_top_")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🆕 Upcoming Releases")
    render_movie_grid(get_upcoming()[:8], cols_per_row=4, key_prefix="h_upc_")

elif st.session_state.current_page == "🔥 Trending":
    st.markdown("# 🔥 Trending Movies")
    st.markdown("<p style='color: #9BA7B5; margin-top: -10px;'>Films capturing global audience attention.</p>", unsafe_allow_html=True)
    c_w, c_g = st.columns([2, 2])
    with c_w:
        t_frame = st.radio("Window", ["Trending Today", "Trending This Week"], horizontal=True, label_visibility="collapsed")
    with c_g:
        genre_dict = get_genres()
        sel_genre = st.selectbox("Genre Filter", ["All Genres"] + list(genre_dict.values()))

    movies = get_trending("day" if "Today" in t_frame else "week")
    if sel_genre != "All Genres":
        gid = [k for k, v in genre_dict.items() if v == sel_genre][0]
        movies = [m for m in movies if gid in m.get("genre_ids", [])]
    render_movie_grid(movies, cols_per_row=4, key_prefix="tr_page_")

elif st.session_state.current_page == "⭐ Popular":
    st.markdown("# ⭐ Popular Movies")
    st.markdown("<p style='color: #9BA7B5; margin-top: -10px;'>Worldwide most-watched films right now.</p>", unsafe_allow_html=True)
    render_movie_grid(get_popular(), cols_per_row=4, key_prefix="pop_page_")

elif st.session_state.current_page == "🎬 Now Playing":
    st.markdown("# 🎬 Now Playing in Theaters")
    st.markdown("<p style='color: #9BA7B5; margin-top: -10px;'>Catch the latest theatrical screenings.</p>", unsafe_allow_html=True)
    render_movie_grid(get_now_playing(), cols_per_row=4, key_prefix="now_page_")

elif st.session_state.current_page == "🏆 Top Rated":
    st.markdown("# 🏆 All-Time Top Rated")
    st.markdown("<p style='color: #9BA7B5; margin-top: -10px;'>Highest rated cinema masterpieces of all time.</p>", unsafe_allow_html=True)
    with st.expander("Filter Top Rated", expanded=False):
        c1, c2 = st.columns(2)
        with c1:
            genre_dict = get_genres()
            ch_genre = st.selectbox("Genre", ["All Genres"] + list(genre_dict.values()))
        with c2:
            min_r = st.slider("Minimum Rating", 7.0, 9.5, 7.5, 0.1)

    gid = [k for k, v in genre_dict.items() if v == ch_genre][0] if ch_genre != "All Genres" else None
    movies = discover_movies(genre_id=gid, min_rating=min_r, sort_by="vote_average.desc") if (gid or min_r > 7.5) else get_top_rated()
    render_movie_grid(movies, cols_per_row=4, key_prefix="top_page_")

elif st.session_state.current_page == "🎭 Genres":
    st.markdown("# 🎭 Browse by Genre")
    st.markdown("<p style='color: #9BA7B5; margin-top: -10px;'>Select any genre to explore curated titles.</p>", unsafe_allow_html=True)

    GENRE_ICONS = {
        "Action": "💥", "Adventure": "🗺️", "Animation": "🎨", "Comedy": "😂",
        "Crime": "🕵️", "Documentary": "📽️", "Drama": "🎭", "Family": "👨‍👩‍👧",
        "Fantasy": "🐉", "History": "🏛️", "Horror": "👻", "Music": "🎵",
        "Mystery": "🔍", "Romance": "❤️", "Science Fiction": "🚀",
        "TV Movie": "📺", "Thriller": "⚡", "War": "⚔️", "Western": "🤠",
    }
    g_map = get_genres()
    g_items = list(g_map.items())

    cols_per_row = 4
    for i in range(0, len(g_items), cols_per_row):
        row = g_items[i:i + cols_per_row]
        cols = st.columns(cols_per_row)
        for idx, (gid, gname) in enumerate(row):
            with cols[idx]:
                icon = GENRE_ICONS.get(gname, "🎬")
                is_sel = (st.session_state.selected_genre_id == gid)
                if st.button(f"{icon} {gname}", key=f"g_btn_{gid}", type="primary" if is_sel else "secondary"):
                    st.session_state.selected_genre_id = gid
                    st.rerun()

    active_gid = st.session_state.selected_genre_id or g_items[0][0]
    active_name = g_map.get(active_gid, "Featured Genre")
    st.markdown("---")
    st.markdown(f"### {GENRE_ICONS.get(active_name, '🎬')} Top {active_name} Movies")
    render_movie_grid(discover_movies(genre_id=active_gid), cols_per_row=4, key_prefix="genre_grid_")

elif st.session_state.current_page == "🔍 Search":
    st.markdown("# 🔍 Search Movies")
    st.markdown("<p style='color: #9BA7B5; margin-top: -10px;'>Search by title or storyline keywords.</p>", unsafe_allow_html=True)

    sc1, sc2 = st.columns([4.5, 1])
    with sc1:
        q = st.text_input("Query", value=st.session_state.search_query, placeholder="Enter movie title, e.g. Inception, Dune, Batman...", label_visibility="collapsed")
    with sc2:
        if st.button("🔍 Search", key="search_btn"):
            st.session_state.search_query = q

    if q != st.session_state.search_query:
        st.session_state.search_query = q

    if st.session_state.search_query.strip():
        results = search_movies(st.session_state.search_query)
        st.markdown(f"#### Results ({len(results)} movies found)")
        render_movie_grid(results, cols_per_row=4, key_prefix="search_res_")
    else:
        st.info("💡 Type in the search box above to find any film.")
        st.markdown("### Suggested Movies")
        render_movie_grid(get_popular()[:8], cols_per_row=4, key_prefix="search_sug_")

elif st.session_state.current_page.startswith("❤️ My Watchlist"):
    st.markdown("# ❤️ My Personal Watchlist")
    st.markdown("<p style='color: #9BA7B5; margin-top: -10px;'>Your saved collection of movies.</p>", unsafe_allow_html=True)

    wl = st.session_state.watchlist
    if not wl:
        st.markdown(
            """
            <div style="text-align: center; padding: 4rem 1.5rem; background: #111720; border-radius: 16px; border: 1px dashed #27313D; margin-top: 1.5rem;">
                <div style="font-size: 3.5rem; margin-bottom: 12px;">🍿</div>
                <h2 style="color: #F5F7FA; margin-bottom: 8px;">Your Watchlist is Empty</h2>
                <p style="color: #9BA7B5; max-width: 480px; margin: 0 auto 1.5rem auto;">
                    Browse movies and click "<b>+ List</b>" or "<b>❤️ Add to Watchlist</b>" to save them here.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        m_list = list(wl.values())
        avg_r = sum([m.get("vote_average", 0) for m in m_list]) / len(m_list)
        w1, w2, w3 = st.columns([2, 2, 2])
        with w1:
            st.markdown(f'<div class="stat-card"><div class="stat-label">Saved Movies</div><div class="stat-val">{len(m_list)} titles</div></div>', unsafe_allow_html=True)
        with w2:
            st.markdown(f'<div class="stat-card"><div class="stat-label">Average Rating</div><div class="stat-val">⭐ {avg_r:.1f} / 10</div></div>', unsafe_allow_html=True)
        with w3:
            st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
            if st.button("🗑️ Clear Watchlist", key="clear_all_wl"):
                st.session_state.watchlist = {}
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)
        render_movie_grid(m_list, cols_per_row=4, key_prefix="wl_view_")

elif st.session_state.current_page == "🤖 Recommendations":
    st.markdown("# 🤖 Smart Recommendations")
    st.markdown("<p style='color: #9BA7B5; margin-top: -10px;'>Discover movies tailored to your mood and watchlist taste.</p>", unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🎯 By Mood & Preferences", "❤️ Based on My Watchlist"])
    with tab1:
        rc1, rc2 = st.columns(2)
        with rc1:
            mood = st.selectbox("Movie Vibe", list(MOOD_PRESETS.keys()))
        with rc2:
            min_vote = st.slider("Minimum Rating", 6.0, 9.0, 7.2, 0.2)

        genre_id = MOOD_PRESETS[mood][0]
        rec_movies = discover_movies(genre_id=genre_id, min_rating=min_vote)
        st.markdown("---")
        render_movie_grid(rec_movies[:12], cols_per_row=4, key_prefix="rec_grid_")

    with tab2:
        if not st.session_state.watchlist:
            st.info("💡 Add a few movies to your Watchlist to enable personalized taste profiling.")
        else:
            wl_recs = get_recommendations_from_watchlist(st.session_state.watchlist, limit=8)
            render_movie_grid(wl_recs, cols_per_row=4, key_prefix="rec_wl_grid_")

elif st.session_state.current_page == "ℹ️ About":
    st.markdown("# ℹ️ About Movie Hub")
    st.markdown(
        """
        <div style="background: #111720; border: 1px solid #27313D; border-radius: 14px; padding: 2rem; margin-top: 1rem;">
            <h2 style="color: #F5F7FA; margin-bottom: 8px;">🎬 Movie Hub</h2>
            <p style="color: #79BDF2; font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; font-size: 0.85rem;">
                Discover • Explore • Watch
            </p>
            <p style="color: #D2D8DE; line-height: 1.7; margin-top: 1rem;">
                <b>Movie Hub</b> is a modern movie discovery and recommendation platform built with <b>Python and Streamlit</b>.
                It features a cinematic Dark Blue + Black visual identity, real-time TMDB integration, personal watchlist management,
                official YouTube trailer playback, and content-based recommendations.
            </p>
            <hr style="border-color: #27313D; margin: 1.5rem 0;" />
            <h4 style="color: #F5F7FA; margin-bottom: 8px;">⚖️ Data Attribution & Disclaimer</h4>
            <p style="font-size: 0.85rem; color: #9BA7B5; line-height: 1.6;">
                This product uses the TMDB API but is not endorsed or certified by TMDB.<br>
                <b>Movie Hub does NOT host, stream, or distribute copyrighted video files.</b>
                All trailers and media are linked directly to official YouTube embeds and legitimate metadata sources.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

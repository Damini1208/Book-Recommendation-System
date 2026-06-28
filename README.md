# 📚 Book Recommendation System

A content-based book recommendation system built with **Python** and **Streamlit**, powered by a dataset of 10,000 books with genre and page metadata.

---

## Features

- **Recommend by Book** — Enter a book you've read and get suggestions based on the same author and genre. Includes fuzzy title matching for typos.
- **Recommend by Pages** — Filter books by reading length: under 150 pages, 150–300, 300–500, or 500+ pages.
- **Recommend by Genre** — Browse books across 9 genres: Adventure, Classic, Dystopian, Fantasy, General, Historical, Mystery, Romance, and Science Fiction.

---

## Demo

> Upload the included dataset (`books.csv`) through the app's file uploader to get started.

---

## Project Structure

```
book-recommender/
├── AI.py                            # Main Streamlit application
├── books.csv  # Dataset (10,000 books)
├── requirements.txt                 # Python dependencies
├── README.md
├── .gitignore
└── LICENSE
```

---

## Dataset

The dataset (`books.csv`) contains **10,000 books** with the following key fields:

| Column | Description |
|---|---|
| `title` | Book title |
| `authors` | Author name(s) |
| `genre` | Genre (9 categories) |
| `pages` | Number of pages |
| `average_rating` | Goodreads average rating |
| `original_publication_year` | Year of publication |

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run AI.py
```

Then open your browser at `http://localhost:8501`.

---

## Requirements

```
streamlit
pandas
```

Create a `requirements.txt` with the above, or install directly:

```bash
pip install streamlit pandas
```

---

## How It Works

1. Upload the CSV file via the Streamlit sidebar uploader.
2. Choose a recommendation mode from the dropdown.
3. Enter your input (book name, page range, or genre) and click **Get Recommendations**.

The app uses `difflib.get_close_matches` for fuzzy book title matching, and filters by author/genre overlap for content-based recommendations.

---

## Built With

- [Streamlit](https://streamlit.io/) — Web app framework
- [Pandas](https://pandas.pydata.org/) — Data manipulation
- [difflib](https://docs.python.org/3/library/difflib.html) — Fuzzy string matching (Python standard library)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

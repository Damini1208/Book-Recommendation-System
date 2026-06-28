import streamlit as st
import pandas as pd
import difflib

def load_data(file):
    df = pd.read_csv(file)
    df.columns = [c.strip().lower() for c in df.columns]

    df['book_name'] = df.get('title', df.columns[0]).astype(str)
    df['author_name'] = df.get('authors', df.get('author', "")).astype(str)
    df['genre'] = df.get('genre', df.get('genres', "")).astype(str)
    df['rating'] = pd.to_numeric(df.get('average_rating', None), errors='coerce')

    df['pages'] = pd.to_numeric(df.get('pages', None), errors='coerce')
    df['publish_year'] = pd.to_numeric(df.get('original_publication_year', None),errors='coerce')
    return df

def suggest_titles(q, choices):
    return difflib.get_close_matches(q, choices, n=5, cutoff=0.4)

st.title("Book Recommender")

uploaded_file = st.file_uploader("Upload your books CSV file", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    titles = df['book_name'].tolist()

    st.success("Dataset loaded successfully!")

    st.subheader("Choose Recommendation Mode")
    mode = st.selectbox("Select mode", ["Based on Book", "Based on Pages", "Based on Genre"])
    
    if mode == "Based on Book":
        st.write("Enter a book name you have read:")
        name = st.text_input("Book Name")
        if st.button("Get Recommendations"):
            if name == "":
                st.warning("Please enter a book name.")
            else:
                match = df[df['book_name'].str.lower() == name.lower()]
                
                if match.empty:
                    suggestions = suggest_titles(name, titles)
                    if suggestions:
                        st.info("No exact match. Did you mean:")
                        st.write(suggestions)
                    else:
                        st.error("No similar books found.")
                else:
                    seed = match.iloc[0]
                    st.success(f"Found: {seed['book_name']} by {seed['author_name']}")
                    
                    same_author = df[df['author_name'] == seed['author_name']]
                    same_genre = df[df['genre'] == seed['genre']]
                    
                    recs = pd.concat([same_author, same_genre]).drop_duplicates()
                    recs = recs[recs['book_name'].str.lower() != name.lower()]
                    
                    st.write("### Recommended Books:")
                    st.dataframe(recs[['book_name', 'author_name', 'genre', 'pages', 'rating']].head(20))

    elif mode == "Based on Pages":
        range_option = st.selectbox("Select page range",
            ["<150 pages", "150 - 300 pages", "300 - 500 pages", ">500 pages"]
        )

        if st.button("Get Recommendations"):
            if range_option == "<150 pages":
                f = df[df['pages'] < 150]
            elif range_option == "150 - 300 pages":
                f = df[(df['pages'] >= 150) & (df['pages'] <= 300)]
            elif range_option == "300 - 500 pages":
                f = df[(df['pages'] >= 300) & (df['pages'] <= 500)]
            else:
                f = df[df['pages'] > 500]
            
            st.write("### Books in this page range:")
            st.dataframe(f[['book_name', 'author_name', 'pages', 'genre']].head(20))
    
    elif mode == "Based on Genre":
        st.write("Choose a genre. Possible genres include:")
        
        unique_genres = sorted(list(set(df['genre'].str.lower().dropna())))
        st.write(", ".join(unique_genres[:20]))
        
        genre_input = st.text_input("Enter genre")
        
        if st.button("Get Recommendations"):
            if genre_input == "":
                st.warning("Please enter a genre.")
            else:
                filtered = df[df['genre'].str.lower().str.contains(genre_input.lower())]
                if filtered.empty:
                    st.error("No books found for this genre.")
                else:
                    st.write("### Books in this Genre:")
                    st.dataframe(filtered[['book_name', 'author_name', 'genre', 'pages']].head(20))
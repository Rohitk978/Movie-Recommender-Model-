import streamlit as st 
st.header("Movie Recommander System")
import pickle
movies = pickle.load(open('movies_list.pkl','rb'))
similar = pickle.load(open('similar.pkl','rb'))

movie_list = movies['original_title'].values

select_value = st.selectbox("select movies from dropdown", movie_list)

def recommand(Inputmovie):
    indexs = movies[movies['original_title']==Inputmovie].index[0]
    distance = sorted(list(enumerate(similar[indexs])),reverse=True,key=lambda vector: vector[1])
    recommend = []
    for i in distance[0:5]:
        if(movies.iloc[i[0]].original_title != Inputmovie):
            recommend.append(movies.iloc[i[0]].original_title)
    return recommend


if st.button("show recommand"):
   movie_rec = recommand(select_value)
   col1,col2,col3,col4,col5 = st.columns(5)
   with col1:
       st.text(movie_rec[0])
   with col2:
       st.text(movie_rec[1])
   with col3:
       st.text(movie_rec[2])
   with col4:
       st.text(movie_rec[3])
   with col5:
       st.text(movie_rec[4])







import media
import fresh_tomatoes

"""
    Add more movies if you want to ;)
"""
toy_story = media.Movie("Toy Story","A story of a boy and his toyes that come to life","http://www.deckchaircinema.com/wp-content/uploads/2016/05/toy_story_wallpaper_by_artifypics-d5gss19.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar","a Marine in an elian plant","http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_UY1200_CR90,0,630,1200_AL_.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

movies = [toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)
print media.Movie.__doc__

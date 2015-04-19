import webbrowser

class Movie():
	
	"""This class provides a way to store movie related information

	Attributes:
		movie_title: String - name of the movie
		movie_storyline: String - a brief plot of the movie
		movie_year: Integer - year the movie was released
		movie_director: String - person who directed the movie
		poster_image: String - a link to an image of the poster art for the movie
		trailer_youtube: String - a link to a YouTube trailer of the movie
	"""
	
	# Movie constructor - it initializes title, plot, poster image, and 
	# YouTube trailer
	def __init__(self, movie_title, movie_storyline, movie_year, 
			movie_director, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.year = movie_year
		self.director = movie_director
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
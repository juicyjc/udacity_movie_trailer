import media
import fresh_tomatoes

# Create Movie objects for the various movies that will be 
# displayed on the website
hedwig = media.Movie(
    "Hedwig and the Angry Inch",
    ("After a botched sex change operation a (wo)man travels to the US to "
    "acheieve rock and roll stardom."),
    "2001",
    "John Cameron Mitchell",
    ("http://upload.wikimedia.org/wikipedia/en/thumb/6/62/HedwigandtheAngry"
    "InchMoviePoster.jpg/323px-HedwigandtheAngryInchMoviePoster.jpg"),
    "https://www.youtube.com/watch?v=4p9mPhGo1j0")

cemetary_man = media.Movie(
    "Cemetary Man", 
    ("The story of a cemetary caretaker who searches for love while defending "
    "himself from the rising dead."),
    "1994",
    "Michele Soavi",
    "http://upload.wikimedia.org/wikipedia/en/7/78/Cemeterymanposter.jpg",
    "https://www.youtube.com/watch?v=tS-GpYY6f2o")

heavenly_creatures = media.Movie(
    "Heavenly Creatures",
    ("A story of two teen girls' obssessive relationship. Based on the 1954 "
    "Parker-Hulme murder case in Christchurch, New Zealand."),
    "1994",
    "Peter Jackson",
    ("http://upload.wikimedia.org/wikipedia/en/e/e5/"
    "Heavenly_Creatures_Poster.jpg"),
    "https://www.youtube.com/watch?v=TfFDm9q8cS0")

twelve_monkeys = media.Movie(
    "Twelve Monkeys",
    ("A prisoner is sent back in time to collect information about a virus "
    "that drove mankind underground."),
    "1995",
    "Terry Gilliam",
    "http://upload.wikimedia.org/wikipedia/en/c/cf/Twelve_monkeysmp.jpg",
    "https://www.youtube.com/watch?v=wuggl3cZD8A")

tims_vermeer = media.Movie(
    "Tim's Vermeer",
    ("An inventor spends five years in an attempt to recreate Vermeer's "
    "photo-realistic painting technique."),
    "2013",
    "Teller",
    "http://upload.wikimedia.org/wikipedia/en/f/f9/Tim%27s_Vermeer_2013.jpg",
    "https://www.youtube.com/watch?v=CS_HUWs9c8c")

ghost_dog = media.Movie(
    "Ghost Dog",
    ("A man who follows the ancient code of the samurai as outlined in the "
    "book Hagakure works as a hitman for the Mafia"),
    "1999",
    "Jim Jarmusch",
    "http://upload.wikimedia.org/wikipedia/en/1/19/Ghost_Dog.jpg",
    "https://www.youtube.com/watch?v=Rml5ehAl7SM")

breaking_the_waves = media.Movie(
    "Breaking the Waves",
    ("A young Scottish woman with a history of psychological problems falls "
    "in love with an oil rig worker."),
    "1996",
    "Lars von Trier",
    ("http://upload.wikimedia.org/wikipedia/en/c/ce/"
    "Breaking_the_waves_us_poster.jpg"),
    "https://www.youtube.com/watch?v=SHqZh-9AiCs")

millers_crossing = media.Movie(
    "Miler's Crossing",
    ("A Prohibition-era gangster film about a power struggle between two "
    "rival gangs."),
    "1990",
    "Joel Cohen",
    "http://upload.wikimedia.org/wikipedia/en/2/2b/Millerscrossingposter.jpg",
    "https://www.youtube.com/watch?v=zYifReJJn4M")

dead_alive = media.Movie(
    "Dead Alive",
    ("A man falls in love, loses his mother, and battles the undead with a "
    "lawnmower."),
    "1992",
    "Peter Jackson",
    "http://upload.wikimedia.org/wikipedia/en/8/86/Braindead-poster.jpg",
    "https://www.youtube.com/watch?v=O8LIug1cP04")

holy_smoke = media.Movie(
    "Holy Smoke!",
    ("A man is hired to deprogram a woman who has moved to India and fallen "
    "for an Indian guru."),
    "1999",
    "Jane Campion",
    "http://upload.wikimedia.org/wikipedia/en/8/82/Holy_smoke_ver1.jpg",
    "https://www.youtube.com/watch?v=5K7ZnoxhiGw")

# store the movies in a list and pass them to fresh tomatoes
movies = [hedwig, breaking_the_waves, twelve_monkeys, tims_vermeer, 
          holy_smoke, dead_alive, cemetary_man, heavenly_creatures, 
          ghost_dog, millers_crossing]

fresh_tomatoes.open_movies_page(movies)

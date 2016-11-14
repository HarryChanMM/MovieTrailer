import fresh_tomatoes
import media
""" This file provides movie data. """
wonder_woman = media.Movie("Wonder Woman",
                        "An Amazonian princess leaves her island home to explore the"
                        "world and, in doing so, becomes one of the world's greatest heroes.",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcTax3jGvMVAFVa_duRg6e2B8hKGVWLujhUE7kwrz0qmGORZZBWS",
                        "https://www.youtube.com/watch?v=5HUlW21v1fQ")

valerian = media.Movie("Valerian",
                       "Time-traveling agent Valerian is sent to investigate a galactic "
                       "empire, along with his partner Laureline.",
                       "https://images-na.ssl-images-amazon.com/images/M/MV5BMTUwMzA2ODUwNl5BMl5BanBnXkFtZTgwNjk0OTQyMDI@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=RArJ8_WyfVs")

guardians = media.Movie("Guardians of the Galaxy",
                        "A group of intergalactic criminals are forced to work together "
                        "to stop a fanatical warrior from taking control of the universe.",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcQW3LbpT94mtUG1PZIIzJNxmFX399wr_NcvoppJ82k7z99Hx6in",
                        "https://www.youtube.com/watch?v=wX0aiMVvnvg")

power = media.Movie("Power Rangers",
                        "A group of high-school kids, who are infused with unique superpowers, "
                        "harness their abilities in order to save the world.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BNDA3MTk3NzE0MF5BMl5BanBnXkFtZTgwOTYxNTQyOTE@._V1_SY1000_CR0,0,648,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=6CKtFztnJ9M")

run = media.Movie("Run the Tide",
                        "When their drug abusing mother is released from prison determined to "
                        "rebuild their family, Rey kidnaps his younger brother Oliver and escapes "
                        "their desert home for the California coast.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMjMyNjIyMDg3MV5BMl5BanBnXkFtZTgwNjYyNTg0MDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=6GlYu09cxgY")

justice = media.Movie("Justice League",
                        "Fueled by his restored faith in humanity and inspired by Superman's selfless "
                        "act, Bruce Wayne enlists the help of his newfound ally, Diana Prince, to face "
                        "an even greater enemy.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BYTk1ZTVmZmQtNDY2YS00MjRiLWFiOTQtNzg0MjFhNjVlMDYwXkEyXkFqcGdeQXVyNjY1MDU0OTM@._V1_UY268_CR150,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=fIHH5-HVS9o")

blind = media.Movie("My Blind Brother",
                        "The rivalry between two brothers reaches a fever pitch during a charity swim "
                        "competition.",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczNDE2NTk5N15BMl5BanBnXkFtZTgwMDMxOTM4OTE@._V1_UY268_CR2,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=5jCQBCfJGhY")

movies = [wonder_woman, valerian, guardians, power, run, justice, blind]
fresh_tomatoes.open_movies_page(movies) """ Pass the movies array to the method """


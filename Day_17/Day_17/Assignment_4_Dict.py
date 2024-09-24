      
movies = {"avatar":  1, "the lord of the rings": 2, "star wars": 3,  
          "the matrix": 4, "inception": 5}

while True:


    print("Enter choice:\n1.Add new movie\n2.vote for a movie\n3.remove a movie\n4.Display voting result\n5.Find the top movie\n6.Exit")
    choice = int(input())


    match choice:
        case 1:
            movie_name =  input("Enter the name of the movie: ")
            movies[movie_name] = 0
            print(movies)
        case 2:
            movie_name = input("Enter the name of the movie: ")
            movies[movie_name] += 1
        case 3:
            movie_name = input("Enter the name of the movie: ")
            if movie_name in movies:
                del movies[movie_name]
            else:
                print("Movie not found")
        case 4:
            for key, value in movies.items():
                print(f"{key}: {value}")
        case 5:
            max_votes = max(movies.values())
            top_movie = [key for key, value in movies.items() if value == max_votes]
            print(top_movie)
        case 6:
            break

    print("\n")
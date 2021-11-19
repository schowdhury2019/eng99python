rating = input("Please enter valid rating: ")

ratings = ["U","12", "12A", "PG", ]

if rating == "U":
    print("Is suitable for everyone")
elif rating in ("12", "12A"):
    print("Must be 12 or over to watch")
elif rating in ("15","18"):
    print(f"Must be {rating} or over to watch")




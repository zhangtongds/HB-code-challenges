def can_two_movies_fill_flight(movie_lengths, flight_length):

    # Determine if two movie runtimes add up to the flight length
    seen = set()
    for m1 in movie_lengths:
        m2 = flight_length - m1
        if m2 in seen:
            return True
        seen.add(m1)

    return False

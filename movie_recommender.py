def quick_sort(L):
    if len(L) == 0:
        return []
    return quick_sort([x for x in L[1:] if x < L[0]]) + L[0:1] + quick_sort([x for x in L[1:] if x >= L[0]])
    
def movie_recommendation_by_flight_duration(movie_list, duration):
    dict_ord = {}
    for i in range(len(movie_list)):
        try:
            dict_ord[movie_list[i]].append(i)
        except:
            dict_ord[movie_list[i]] = [i]
        
    sorted_movie_list = quick_sort(movie_list)
    print(sorted_movie_list)
    i, j = 0, len(sorted_movie_list)-1
    max_d = 0
    while i < j:
        if sorted_movie_list[i] + sorted_movie_list[j] <= duration:
            if max_d < sorted_movie_list[i] + sorted_movie_list[j]:
                max_d = sorted_movie_list[i] + sorted_movie_list[j]
                left, right = i, j
            i += 1
        else:
            j -= 1
    
    mov1, mov2 = sorted_movie_list[left], sorted_movie_list[right]
    if dict_ord[mov1][0] == dict_ord[mov2][0]:
        return (dict_ord[mov1][1], dict_ord[mov2][0])
    else:
        return (dict_ord[mov1][0], dict_ord[mov2][0])
   
   
if __name__ == "__main__":
    """
    Given a movie list (length of duration) and flight duration, recommend
    2 free movies to the passenger such that they can stay entertained
    during the maximum length of flight time.
    NOTE: Flight Duration always greater than 135
    """ 
    movie_list = [90, 85, 75, 60, 120, 150, 125, 250]
    duration = 350
    idxs = movie_recommendation_by_flight_duration(movie_list, duration)
    recommended_movies_durations = [movie_list[idxs[0]], movie_list[idxs[1]]]
    print(recommended_movies_durations)
    print("Recommended Movie Indexes: {}, {}".format(idxs[0], idxs[1]))
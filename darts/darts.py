def score(x, y):
    dist_sq = (x**2 + y**2)
    if(dist_sq < 1):
        print("You earn 10 points")
    elif(dist_sq < 25):
        print("You earn 5 points")
    elif(dist_sq < 100):
        print("You earn 1 point")
    else:
        print("You earned no points")
    
score(0, 0)

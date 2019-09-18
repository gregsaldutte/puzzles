def leap_year(year):

    if not isinstance(year,int):
        raise TypeError("Year entered must be an integer!")
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    


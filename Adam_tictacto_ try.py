def placeX():
    try:
        coord_x = int(input("x"))
        coord_y = int(input("y"))
        if coord_x > 3 or coord_x < 1 or coord_y > 3 or coord_y < 1:
            raise ValueError
        elif (list1[coord_y])[coord_x] != " ":
            raise ValueError
        (list1[coord_y])[coord_x] = "x"
    except:
        placeX()
        
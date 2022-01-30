def findMinArrowShots( points):

    points.sort(key = lambda x : x[0])

    print(points)

    first_end = points[0][1]
    arrow = 1

    for start,end in points:
        if first_end < start:
            arrow+=1
            first_end = end

    return arrow

assert 2 == findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])


def minimumEffortPath(heights):
    path = []
    effort = 0
    x = 0
    y = 0
    size = len(heights)
    while x != size:
        if x < 0 or x > size or y < 0 or y > size:
            continue
        
    return 0


heights = [[1,2,2],[3,8,2],[5,3,5]]
print(minimumEffortPath(heights))
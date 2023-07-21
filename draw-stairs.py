# Given a number n, draw stairs using the letter "I", 
# n tall and n wide, with the tallest in the top left.
def draw_stairs(n):
    # do something
    log = "I\n"
    i = 1   
    while i < n:
        log += " " * i + "I\n"
        i += 1
    return log

print(range(3))



        


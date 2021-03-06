import os
import sys

last_movie = None
last_title = None
last_cnt = 0

def output():
    if not last_movie: return
    print "%s\t%s\t%d" % (last_movie, last_title, last_cnt)
    
for line in sys.stdin:
    movie, title, cnt = line.strip().split("\t")
    
    if movie != last_movie:
        output()
        last_movie = movie
        last_title = title
        last_cnt = 0
        
    last_cnt = last_cnt + int(cnt)

output()
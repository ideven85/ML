import ast
import graph_version
with open('test_data/songs_02.py','r') as f:
    song,target,output = ast.literal_eval(f.read())
    print(output)
    #result = graph_version.mixtape_graph(dict(song),target)
    print(sum(song[i] for i in song))
    #assert sum(song[i] for i in result) == target, "incorrect duration!"




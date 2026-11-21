class Playlist:
    def __init__(self, *songs):
        self.songs = list(songs)

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, i):
        print("get", i)
        return self.songs[i]

    def __repr__(self):
        return f"Playlist({self.songs!r})"

    def __str__(self):
        return " | ".join(self.songs)

    def __call__(self, extra):
        return Playlist(*self.songs, extra)


p = Playlist("a", "b")

print(p)
print([p])
print(f"{p!r:>10}"[:3], f"{p}")
print(len(p), bool(Playlist()), bool(p))
print(p[1])
print("b" in p)

for s in p:
    pass

q = p("c")
print(q, p is q)
print(list(reversed(p)))
#SOLUTION
a | b
[Playlist(['a', 'b'])]
Pla a | b
2 False True
get 1
b
get 0
get 1
True
get 0
get 1
get 2
a | b | c False
get 1
get 0
['b', 'a']

Process finished with exit code 0

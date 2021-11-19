from . import recm


example = [
    ("User1", "FilmA"), 
    ("User1", "FilmB"), 
    ("User2", "FilmC"), 
    ("User2", "FilmD")
]

def test_most_similar():
    assert (1.0, {"FilmA", "FilmB"}) == recm.most_similar({"FilmA", "FilmB"}, example)
    assert (0.5, {"FilmA", "FilmB"}) == recm.most_similar({"FilmA"}, example)
    assert (0.5, {"FilmC", "FilmD"}) == recm.most_similar({"FilmC"}, example)

def test_overlap():
    assert 1 == recm.overlap({"FilmA", "FilmB"}, {"FilmA", "FilmB"})
    assert 0 == recm.overlap({"FilmA", "FilmB"}, {"FilmC", "FilmD"})
     
def test_vectorize():
    assert [{"FilmA", "FilmB"}, {"FilmC", "FilmD"}] == recm.vectorize(example)
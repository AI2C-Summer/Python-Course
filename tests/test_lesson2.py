from lessons.lesson1 import add

def test_add():
    result = add(2, 3)

    assert result is not None, "You're not returning anything"
    assert result == 5, "Hint: return a + b"

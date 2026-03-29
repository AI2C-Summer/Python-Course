import subprocess
import sys

def test_lesson1():
    result = subprocess.run(
        [sys.executable, "lesson1.py"],  # uses correct Python version
        capture_output=True,
        text=True
    )
    #tests any non-empty string
    assert result.stdout.strip() != "" "You need to return a string"

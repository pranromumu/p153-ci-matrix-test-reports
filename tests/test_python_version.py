import sys

def test_python_version():
    major = sys.version_info.major
    minor = sys.version_info.minor
    
    print(f"\nRunning on Python {major}.{minor}")
    
    assert (major, minor) in [(3, 10), (3, 11), (3, 12)]
import sys
from packaging.version import Version

current_tag = sys.argv[1] if len(sys.argv) > 1 else '0.0.1'
version = Version(current_tag)
new_version = Version(f"{version.major}.{version.minor + 1}")
print(new_version)
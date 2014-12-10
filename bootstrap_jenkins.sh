virtualenv --no-setuptools .
mkdir -p buildout-cache/downloads
./bin/python bootstrap.py
./bin/buildout
./bin/develop up -f
# Xvfb :99 -a &

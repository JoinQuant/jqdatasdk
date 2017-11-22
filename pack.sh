rm -rf pack
mkdir pack
cd pack
mkdir jqdatasdk
cp -r ../../jqdatasdk/jqdatasdk jqdatasdk/
find jqdatasdk/ -name __pycache__|xargs rm -rf
find jqdatasdk/ -name *.pyc|xargs rm -f
cp ../setup.py jqdatasdk
cp ../requirements.txt jqdatasdk
cp ../README.md jqdatasdk
cp ../VERSION.txt jqdatasdk
version=$(cat jqdatasdk/VERSION.txt)
tar -czf jqdatasdk.$version.tar.gz jqdatasdk



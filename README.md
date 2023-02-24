
# STEP 1 :
```
python3 setup.py sdist bdist_wheel
```
# STEP 2 ;
```
python3 -m twine upload --repository pypi dist/*
```

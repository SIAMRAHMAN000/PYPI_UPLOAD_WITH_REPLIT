### STEP 1 :

# CREATE FILES FOR PYPI  UPLOAD 

### STEP 2 :
# AND TYPE BELOW THIS
```
python3 setup.py sdist bdist_wheel
```
### STEP 3 :
# YOU NEED TO UPLOAD PYTHON PAKAGE. TYPE THIS =>
```
python3 -m twine upload --repository pypi dist/*
```

# DONE

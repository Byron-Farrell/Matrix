# Matrix

### Generate distribution archive
```
python3 -m pip install --upgrade build
python3 -m build
```

### Upload the distribution archive
```
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```

### PIP Install
```
pip install apex_matrix
```

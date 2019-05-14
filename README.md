# Apptweak-io python3 library

## push to pypi
1. create the dist code `python3 setup.py sdist bdist_wheel`
2. Install twine `pip3 install twine --user`
3. Upload to pipy `twine upload dist/*`
For each upload, the num version should be unique !
change the version in the setup.py file

To put it in prod mode instead of dev, remove tab_build in setup.cfg
## code structure

### \_\_init\_\_.py
Contains all the global variables

### plateform.py
contains every end-point

### ios.py
Redifine Ios specific end-point behaviour

### android.py
Redifine Android specific end-point behaviour

### ressource.py
Make the actual fetch and verify some parmas

## install package locally
```bash
python3 setup.py install --user
```

## tests

```bash
python3 -m unittest tests/plateform.py -v
```
```bash
python3 -m unittest tests/apptweak.py -v
```
```bash
python3 -m unittest tests/ressource.py -v
```
## Show downloads stats 

[See the download stats](https://pypistats.org/packages/apptweak)

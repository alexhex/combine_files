# Smith Files Combiner

## Function

It scans the destination file end with "_smith.pdf" with case insensitive and find the correspoding files in the resource folder without the "_smith" suffix but the same basename, then copy those files to destination folder and delete the corresponding files in dest folder. 

However, if the resource folder doesn't include any similar file, the _smith file would not be replaced. 


## Installation

The tool is built on pyside2 and packaged by PyInstaller.

Use the following command to build the exe file:


```python
pyinstaller -F -w-i morty.ico wind.py
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
# Folder and file name checking tool
This windows tool checks file and folder names against the following criteria:

## Folders 
Folders names must follow one of the two conventions below:

- Seven-digit ID number [underscore] four-digit date, e.g. `0002268_1865`
- Seven-digit ID number [underscore] four-digit date [underscore] three-digit month [underscore] three-digit month, e.g. `0002268_1865_JAN_JUN`
    - Months should always be represented with three letters and matching is not case-sensitive


## Files
File names must be comprised of
- parent folder [underscore] four-digit number beginning `0001`, e.g.
    - 0002091_1856_Jan_Jun/
        - 0002091_1856_Jan_Jun_0001.tif
        - 0002091_1856_Jan_Jun_0002.tif
        - 0002091_1856_Jan_Jun_0003.tif
        - ...

Matching is by default case-insensitive, but this functionality can be enabled at run-time.

## Running the tool
The tool is supplied as an executable but can be run as a python script. The tool requires as an input a directory of directories, each containing files to be scanned. For instance, if the path
`C:\Users\JoeBloggs\Desktop\Files` is given, all directories within this directory, and their contents, will be scanned. Alternatively, the executable can be placed in the directory and run with an option to use the current directory.

### Running the executable version
- Open the file `nameSchemeCheck.exe` 
- Type `Y` and press `Enter` to run in case-sensitive filename checking mode, otherwise press `Enter`
- To scan the current direcory, enter `Y`
    - The default behaviour is to scan a pre-configured directory 
- Enter `N` to scan a directory of your choice
    - Unrecognised inputs set the path to the default  `\\P12B-NAS1\scandata2\HMD\RAW SCANS\Dave\FMP\Still to deliver to FMP`
- The tool checks if the directory exists and falls back to the default path if this is not the case
- Folder names and file names are scanned according to the conventions defined above 
- Any folder or file names not fulfilling these criteria have their full path written to a file 
    - nonCompliantFolders.txt
    - nonCompliantFiles.txt
- Files appear in the same directory as the executable

### Running the python script
The python script was developed using python 3.7 and requires additional modules to run. To install these with `pip`, call
```
pip install -r requirements.txt
```
It is recommended to perform this step inside a virtual environment.

To run the python script, call:

```
python nameSchemeCheck.py
```

- All steps described for the executable version apply to the python version
- Running the script allows the user to modify the default directory, hard-code case-matching options and provides a greater level of control over the program
- To recompile the script as an executable, call
```
pyinstaller -F nameSchemeCheck.py
```

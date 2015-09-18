#USDA FOIA Log Downloader
This is a small script to download all FOIA log files from the USDA.

## FOIA Log Web Page
The FOIA logs are located on [USDA web server](http://www.aphis.usda.gov/foia/).  However, their website is not rendering to the python script the same way it does a web browser.  Fortunately, the files seem to be in a standar dformat of:

```https://www.aphis.usda.gov/foia/foia_logs/<YEAR>/<MONTH NAME>.xlsx```

## Usage
1. Create a virtual environment for your script:

```$ virtualenv env ```

2. Enter the virtual environment

```$ source env/bin/activate ```

3. Install requirements

```$ pip install -r requirements.txt ```

4. Change permissions on script

```$ chmod a+x get_foia_files.py```

5. Execute script and enjoy the files

```$ ./get_foia_files.py```


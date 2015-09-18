#USDA FOIA Log Downloader
This is a small script to download all FOIA log files from the USDA.

## FOIA Log Web Page
The FOIA logs are located on [USDA web server](http://www.aphis.usda.gov/foia/).  However, their website is not rendering to the python script the same way it does a web browser.  Fortunately, the files seem to be in a standard format of:

```https://www.aphis.usda.gov/foia/foia_logs/<YEAR>/<MONTH NAME>.xlsx```

## Usage
Create a virtual environment for your script:

```$ virtualenv env ```

Enter the virtual environment

```$ source env/bin/activate ```

Install requirements

```$ pip install -r requirements.txt ```

Change permissions on script

```$ chmod a+x get_foia_files.py```

Execute script and enjoy the files

```$ ./get_foia_files.py```

Convert all excel files to CSV

```$ ./convert_to_csv.sh ```

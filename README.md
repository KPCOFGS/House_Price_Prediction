# Housing_Prediction

A simple script that predicts the house price using Zillow's csv data file

## Download

You can download the script using `git`
```bash
cd 
```
You can install the dependencies using pip:
```bash
pip install -r requirements.txt
```

## Parameters

`"CITY_NAME"` Required. The city name

`"STATE_NAME"` Required. The state name

`TIME_LENGTH` Required. Prediction time length in days

`"CSV_DATA_FILE"` Required. Zillow home value csv data file

## Usage
To use the script, you need to specify the parameters. For example:
```bash
python script.py "CITY_NAME" "STATE_NAME" TIME_LENGTH "CSV_DATA_FILE"
```

## Note
- This script only uses csv data file from Zillow
- The data file needs an update as time goes by
- The script assumes the csv data file structure is consistent from time to time

## License
This repository is licensed under the [Unlicense](LICENSE)

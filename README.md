# fcp-mpdp-postcodes

Get parliamentary constituency and admin county from Making Payment Data Public (MPDP) data.

## Pre-requisites
- Docker
- Python3
- Pandas
- [Postcodes.io](https://postcodes.io/docs#Install-notes) container running with port `8000` exposed
- Data Warehouse `.csv` extract with MPDP data (see schema below)

## Data Warehouse data schema

`.csv` file with the following data.  [Script](Script.py) assumes this name is `WIP_ActualDataSet.csv`.


| Column Name | Example |
|-------------|---------|
| Payee_Name  | John Doe |
| Full_Postcode | SW1A 1AA |
| Part_Postcode | SW1A |
| Town | London |
| Parliamentary_Constituency | `<Empty column>` |
| County | `<Empty column>` |
| Scheme | SFI |
| Activity Detail | Introductory |
| Amount | 0.98 |

## Running the script

Run the `Script.py` script with the following command with Python:

```bash
python3 Script.py > results.csv
```

## Output

A file named `results.csv` will be created that includes the `parliamentary_constituency` and `admin_county` values for each row in the input.

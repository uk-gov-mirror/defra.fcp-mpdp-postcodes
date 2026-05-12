# fcp-mpdp-postcodes

Get parliamentary constituency and admin county from Making Payment Data Public (MPDP) data using postcodes and partial postcodes.

## Pre-requisites

- Docker
- Python 3
- [Postcodes.io](https://github.com/ideal-postcodes/postcodes.io) repository cloned locally

## Setup

### Install Python dependencies

```bash
pip install pandas requests
```

### Start the Postcodes API

Clone the postcodes.io repository and start it with Docker Compose:

```bash
git clone https://github.com/ideal-postcodes/postcodes.io.git
cd postcodes.io
docker compose up
```

This will start the API on port `8000`.

## Input data schema

A `.csv` file with the following columns:

| Column Name | Example |
|-------------|---------|
| payee_name | John Doe |
| full_postcode | SW1A 1AA |
| part_postcode | SW1A |
| town | London |
| parliamentary_constituency | `<Empty column>` |
| county_council | `<Empty column>` |
| scheme | SFI |
| amount | 0.98 |
| financial_year | 24/25 |
| payment_date | |
| scheme_detail | Partial Payment |
| activity_level | |

If `full_postcode` is provided it is used for a more accurate lookup. If it is missing, `part_postcode` is used as a fallback.

## Running the script

```bash
python3 get-data-from-postcodes.py <input_csv_file> > results.csv
```

For example:

```bash
python3 get-data-from-postcodes.py input.csv > results.csv
```

## Output

Results are written to stdout (redirect to a file as shown above). Each line contains the `parliamentary_constituency` and `admin_county` values for the corresponding row in the input.

When using a part postcode, the API may return multiple results for a field (since a partial postcode can span multiple areas). In this case the field is left empty, as a single value cannot be determined.

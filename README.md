# roth-conversion-pdf

This tool is for people who need to regularly perform Roth conversions. (For example, converting after-tax 401(k) balances to Roth balances each pay period.)

It's helpful for providers that still don't have a web form for these requests and require a printed and signed PDF to be scanned in.

## Prerequisites

You should have python and ghostscript installed.

If you don't have them, try [installing homebrew](https://brew.sh) then running `brew install python gs`.

## Usage

Download this repo.

Copy your plan's PDF file into the folder you downloaded and rename it `input.pdf`.

The input PDF should be completely filled out except for the date.

Run the script:

```bash
python add_date.py
```

If all goes well, you'll now have a dated output file in the format `output-YYYY-MM-DD.pdf` and this will be printed to your printer. You can now sign the document, scan it, and upload it or mail it in.

## Configuration options

If you want to customize the script

Open `config.yml` in a text editor if you want to customize

- `rect`: where the date prints on the date page
- `date_page`: which page the date is on
- `print_range`: the page range to send to your printer; blank if you don't want to print

These values default to good values for Empower Retirement's Roth In-Plan Conversion PDF.

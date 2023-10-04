import datetime
from os import SEEK_SET
from typing import TextIO


def get_year() -> int:
    """Return the current year as an integer."""
    return datetime.datetime.now().year


def parse_invoice_number(invoice_number: str) -> tuple[int, int]:
    """Split a well-formed invoice "number" into its component parts.

    :param invoice_number: A string of the form YYYY-NNNN
        YYYY is the 4 digit year.
        NNNN is a 4 digit invoice number, left padded with zeros.
        The 2 parts are separated with a "-" character.
    :return: The returned tuple will contain:
        the 4 digit year as an integer,
        the invoice number as an integer.
    """
    year , index = invoice_number.split("-")
    return int(year),int(index)



def next_invoice_number(invoice_number: str) -> str:
    """ Produce the next invoice "number" in sequence.

    The format of `invoice_number` is described in `parse_invoice_number`.

    :param invoice_number: A string representing an invoice number.
    :return: A string representing the next invoice number.
        The numerical part will be incremented, unless the current year
        isn't the same as the year in `invoice_number`. In that case,
        the new invoice number will contain the current year, and the
        numerical part will be set to "0001".
    """
    invoice_test = parse_invoice_number(invoice_number)
    final_invoice_no = str(invoice_test[1]+1).zfill(4)
    if invoice_test[0] == get_year():
        # return (str(invoice_test[0]))+"-"+final_invoice_no
        return f'{invoice_test[0]}-{final_invoice_no}'
    else:
        return str(str(get_year()))+"-"+"0001"


# print(next_invoice_number("2022-0006"))


def record_invoice(invoice_file: TextIO,
                   company: str,
                   amount: float,last_line_ptr : int = 0) -> int:
    """Create a new invoice number, and write it to a file on disk.

    :param invoice_file: An open text file, opened using r+.
    :param company: The name of the company being invoiced.
    :param amount: The amount of the invoice.
    :param last_line_pointer : poisition of start of last line
    :return : position of last line in file
    """
    #below loop starts from the last pointer poistion in invoice_file
    # it moveds the file pointer to empty line
    # we need to save position of pointer before writing to it
    # use the saved position  to reset to that position before we read
    # reading will bring us to next line , where we can write
    # store position again before writing
    # last_line_ptr = 0
    ## 0 is sek set , which puts file pointer to beginning of file
    ## this allows for loop below that to reiterate stream again
    ## not very efficient - we shuold ideally save pointer position
    invoice_file.seek(last_line_ptr, 0)
    for line in invoice_file:
        last_row = line
    if last_row:
        last_invoice = last_row.split("\t")[0]
        new_invoice = next_invoice_number(last_invoice)
    else:
        year=get_year()
        new_invoice=f"{year}-{1:04d}"
    last_line_ptr = invoice_file.tell()
    print(f"{new_invoice}\t{company}\t{amount}",file=invoice_file)
    return last_line_ptr

data ='invoices.csv'
with open(data,'r+',encoding="utf-8",newline="") as inps:
    last_line = record_invoice(inps,"ACME",18.4)
    last_line = record_invoice(inps,"Squirrel",300.1,last_line)

# Test code for invoice number:
# current_year = get_year()
# test_data = [
#     ('2019-0005', (2019, 5), f'{current_year}-0001'),
#     (f'{current_year}-8514', (current_year, 8514), f'{current_year}-8515'),
#     (f'{current_year}-0001', (current_year, 1), f'{current_year}-0002'),
#     (f'{current_year}-0023', (current_year, 23), f'{current_year}-0024'),
# ]
#
# for test_string, result, next_number in test_data:
#     parts = parse_invoice_number(test_string)
#     if parts == result:
#         print(f'{test_string} parsed successfully')
#     else:
#         print(f'{test_string} failed to parse. Expected {result} got {parts}')
#
#     new_number = next_invoice_number(test_string)
#     if next_number == new_number:
#         print(f'New number {new_number} generated correctly for {test_string}')
#     else:
#         print(f'New number {new_number} is not correct for {test_string}')
#
#     print('-' * 80)


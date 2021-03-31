# GUI controls
ENTRY_TYPE_INVOICE_RECORD = "invoice"
ENTRY_TYPE_GENERAL_LEDGER = "general ledger"

# Hard coded file names
EXCEL_LOOKUP_LOG_FILE = ".//log//excel_lookup.log"
EXTERNAL_SALES_MATCHING_FILE = "External_Sales_GUI.xlsx"

# General
LENGTH_COMPANY_NAME_CHECK = 6
EXCHANGE_RATE_LEADING_CHRS = "匯率:"
USD_AMOUNT_CHRS = "美金未稅"
FUNCTION_CURRENCY_USD = "USD"
FUNCTION_CURRENCY_NTD = "NTD"
DATA_SOURCE_INVOICE_DETAIL = 0
DATA_SOURCE_GENERAL_LEDGER = 1
#
# Invoice related constants
# Input invoice file is of .xls format, and is loaded using xlrd package, in which the way to access
# cells is of 0-based index
#
COL_INVOICE_NO = 0
COL_INVOICE_REMARK = 1
COL_INVOICE_STATUS = 3
COL_INVOICE_DATE = 4
COL_INVOICE_BUYER = 6
COL_INVOICE_SALES = 10
COL_INVOICE_VAT = 11
COL_INVOICE_TOTAL = 12
COL_INVOICE_CHECKED = 14

# general ledger related constants
# xlrd is 0-based indexing
COL_GL_VOUCHER_TYPE = 0
COL_GL_INVOICE_NO = 2
COL_GL_INVOICE_DATE = 4
COL_GL_ACCOUNT_DESCRIPTION = 11
COL_GL_INVOICE_CURRENCY = 14
COL_GL_EXCHANGE_RATE = 15
COL_GL_DEBIT_AMT = 16
COL_GL_CREDIT_AMT = 17
COL_GL_AMOUNT = 18
COL_GL_TEXT = 22

# column arrangement of external sales spreadsheet
COL_GL_ES_OFFSET = 3
COL_ES_VOUCHER_TYPE = 0
COL_ES_INVOICE_NO = 2
COL_ES_UNIFIED_INVOICE_NO = 3
COL_ES_UINV_AMT = 4
COL_ES_INVOICE_MATCHED = 5
COL_ES_INVOICE_DATE = COL_GL_INVOICE_DATE + COL_GL_ES_OFFSET
COL_ES_ACCOUNT_DESCRIPTION = COL_GL_ACCOUNT_DESCRIPTION + COL_GL_ES_OFFSET
COL_ES_INVOICE_CURRENCY = COL_GL_INVOICE_CURRENCY + COL_GL_ES_OFFSET
COL_ES_EXCHANGE_RATE = COL_GL_EXCHANGE_RATE + COL_GL_ES_OFFSET
COL_ES_DEBIT_AMT = COL_GL_DEBIT_AMT + COL_GL_ES_OFFSET
COL_ES_CREDIT_AMT = COL_GL_CREDIT_AMT + COL_GL_ES_OFFSET
COL_ES_AMOUNT = COL_GL_AMOUNT + COL_GL_ES_OFFSET
COL_ES_TEXT = COL_GL_TEXT + COL_GL_ES_OFFSET


TARGET_ACCOUNT_IN_GL = "Accounts Receivable"
AMOUNT_DIFF_THRESHOLD_RATIO = 0.01

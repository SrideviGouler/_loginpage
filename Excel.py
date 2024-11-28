import xlrd

path = r'C:\Users\sride\PycharmProjects\Framework_demowebshop\test_data\Demo_webshop_data.xls'

work_book=xlrd.open_workbook(path)
work_sheet=work_book.sheet_by_name("Sheet1")

log_rows=work_sheet.get_rows()
header=next(log_rows)

def log_locators():
    log_details={}
    for row in log_rows:
        log_details[row[0].value]=(row[1].value,row[2].value)
    # print(log_details)
log_locators()
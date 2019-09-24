


def open_workbook_get_sheet(file_path: str, sheet_name: str):
    import xlwings as xw
    book = xw.Book(file_path)
    sheet = book.sheets[sheet_name]
    return sheet


def close_workbook(sheet):
    book = sheet.book
    book.close()

from openpyxl import load_workbook


def use_excel_file(filepath):
    sheet_name = input('Input sheet name: ')
    cell_names = list(map(str.strip, input('Input start_cell and finish_cell names, e.g. A1:A10').split(':')))       # Q10:Q124

    # load file, activate sheet in it, select targeted cell's
    wb = load_workbook(filename=filepath)
    wb_sheet = wb.active if sheet_name == '' else wb[sheet_name]

    '''
    # create dictionary with keys==cell's coords, values==cell's values
    cells_with_serial_numbers = ft.create_cells_dictionary(wb_sheet, cell_names)

    # change serial numbers for each cell using randomiser, rewrite new serial numbers in file and save it
    for key, values in cells_with_serial_numbers.items():
        wb_sheet[key] = ', '.join([ft.random_last_symbols(value) for value in values])
    '''

    wb.save(f"new_{create_new_filename(filepath)}")


def create_new_filename(filepath):
    return filepath if '/' not in filepath else filepath[filepath.rfind('/')+1:]

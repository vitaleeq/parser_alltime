from openpyxl import load_workbook
import string


def use_excel_file(filepath):
    sheet_name = input('Input sheet name: ')
    lst = input("Input vendor_code's column letter, first_row and last_row(e.g. B, 10, 64): ").split(', ')
    vendor_codes_col = [int(elem) if elem.isdigit() else string.ascii_uppercase.find(elem.upper()) for elem in lst]
    # Here we got smth like this: [1{0-26}, 10{1-inf}, 64{1-inf}]

    # load file, activate sheet in it, select targeted cell's
    wb = load_workbook(filename=filepath)
    wb_sheet = wb.active if sheet_name == '' else wb[sheet_name]
    #body_col, back_cover_col, mechanism_type_col, bracelet_col, indication_col, glass_col, additional_functions_col, insertions_col
    required_cols = select_required_cols(vendor_codes_col[1] - 1, wb_sheet)
    print(required_cols)

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


def select_required_cols(attrs_row_number, wb_sheet):
    search_dict = {'body_col': 'Корпус',
                   'back_cover_col': 'Задняя крышка',
                   'mechanism_type_col': 'Тип механизма',
                   'bracelet_col': 'Тип браслета',
                   'indication_col': 'Индикация',
                   'glass_col': 'Стекло',
                   'additional_functions_col': 'Дополнительные функции',
                   'insertions_col': 'Вставки'}
    required_cols_dict = {}
    for elem in search_dict:
        for row in wb_sheet.iter_rows(min_row=attrs_row_number, max_row=attrs_row_number, min_col=wb_sheet.min_column, max_col=wb_sheet.max_column):
            for cell in row:
                if cell.value is None:
                    continue
                if search_dict[elem].strip().lower() in cell.value.strip().lower():
                    required_cols_dict[elem] = cell.coordinate
    return required_cols_dict

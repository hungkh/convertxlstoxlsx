import os
import pandas as pd

def convert_all_xls_to_xlsx(directory):
    # Duyệt qua tất cả các file trong thư mục
    for filename in os.listdir(directory):
        if filename.endswith(".xls"):
            # Đọc file .xls
            data_frame = pd.read_excel(os.path.join(directory, filename), engine='xlrd')

            # Tạo tên file .xlsx
            new_filename = os.path.splitext(filename)[0] + ".xlsx"

            # Ghi dữ liệu vào file .xlsx
            data_frame.to_excel(os.path.join(directory, new_filename), engine='openpyxl', index=False)

# Sử dụng hàm
convert_all_xls_to_xlsx('/home/kali/xls/')

import pandas as pd
import glob

# Đường dẫn đến tất cả các file CSV trong thư mục
file_paths = glob.glob('E:/Project DS/CleanData/Data_DS_Clean/*.csv')

# Đọc từng file và gộp vào một DataFrame
dfs = [pd.read_csv(file) for file in file_paths]
merged_df = pd.concat(dfs)

# Chuyển cột "date" sang định dạng datetime
merged_df['date'] = pd.to_datetime(merged_df['date'], format='%Y-%m-%d %H:%M:%S')

# Sắp xếp DataFrame theo cột "date"
merged_df.sort_values(by='date', inplace=True)

# Lưu DataFrame đã gộp và sắp xếp thành file mới
merged_df.to_csv('E:/Project DS/CleanData/Data_DS_Clean/merged_and_sorted.csv', index=False)

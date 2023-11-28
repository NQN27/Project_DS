import re
import csv
def removeContentError(text): 
    text = str(text)
    text = text.lower()
    text = re.sub(r'[^\w\s]', ' ', text) 
    text = re.sub(r'\s+', ' ', text.strip())
    text = re.sub(r'\S+ đã viết', '!', text)
    pattern = r'(gộp bài viết \S+ \S+ \S+ bài cũ \S+ \S+ \S+)'
    text = re.sub(pattern, '!', text) 
    text = re.sub(r'xem tất cả', ' !', text) 
    return text

def removeTitleErrror(text) :
    text = str(text)
    return re.sub(r'[^\w\s]', ' ', text.lower())

def clean_csv(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        fieldnames = reader.fieldnames

        with open(output_file, 'w', encoding='utf-8', newline='') as output_csv:
            writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
            writer.writeheader()

            for row in reader:
                cleaned_title =  removeTitleErrror(row['title'])
                cleaned_content = removeContentError(row['content'])
                
                row['title'] = cleaned_title
                row['content'] = cleaned_content
                writer.writerow(row)

import os
outpath = r"E:\Project DS\CleanData\Data_DS_Clean"
inpath = r"E:\Project DS\CleanData\Data_DS"
folder_path = r'E:\Project DS\CleanData\Data_DS'  # Thay đổi đường dẫn này thành đường dẫn thực tế của thư mục của bạn
file_names = os.listdir(folder_path)
for file in file_names :
    clean_csv(inpath + "\\" + file, outpath + '\\' + file[:-4] + '_clean.csv')

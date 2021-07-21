from PIL import Image
import PIL
import os
from time import sleep
import sys
import ntpath
from pdf2image import convert_from_path
import pathlib

path = getattr(sys, '_MEIPASS', os.getcwd())
os.chdir(path)

# print('Hello to Photo converter')
# fullname = input('What is your file name including the extension? (press enter when you done)\n')
image_path = sys.argv[1]
output_dir = sys.argv[2]
# assert os.path.isfile(image_path)
# image_path = r'C:\Users\priel\Downloads\old_projects\PhotoConverter\pic3.pdf'
# output_dir = r'C:\Users\priel\Downloads\old_projects\PhotoConverter'
fullname = ntpath.basename(image_path)
name, ext = fullname.split('.')
NewFullName = name + '.pdf'
New_image_path = os.path.join(output_dir, NewFullName)
if ext == 'pdf':
    # print('converts pdf to jpeg')
    if str(pathlib.Path(image_path).parent.absolute()) == output_dir:
        NewFullName = name + '_.pdf'
        New_image_path = os.path.join(output_dir, NewFullName)
    pages = convert_from_path(image_path, poppler_path="./poppler-0.90.0/bin")
    image_path = os.path.join(str(pathlib.Path(image_path).parent.absolute()), f'{name}.jpg')
    for page in pages:
        page.save(image_path, 'JPEG')
# print('\nThe default converts are:\n\nBlack and white convert,\nResize image to 1660 on 2260 pixels(200DPI if prints on A4),\nConvert to pdf type,\n\nConverts starting...')
DPI_200_SIZE_FOR_A4 = (1654, 2339)
image_file = Image.open(image_path) # open colour image
image_file = image_file.convert('1') # convert image to black and white
image_file = image_file.resize(DPI_200_SIZE_FOR_A4, PIL.Image.ANTIALIAS)
image_file = image_file.convert('RGB')

image_file.save(New_image_path, format='pdf', optimize=True)

# print(f'New picture size is {int(os.stat(New_image_path).st_size)//1000} KB after first compression')
if os.stat(New_image_path).st_size > 100000:
    # print('The size is still big after first compression, execute second compression...')
    os.remove(New_image_path)
    # qualityNum = 1
    image_file.save(New_image_path, format='pdf', optimize=True, quality=1)
    # print(f'New picture size is {int(os.stat(New_image_path).st_size)//1000} KB after second compression')

#optional increase quality
    # if os.stat(New_image_path).st_size > 100000:
    #     # print('in quality 1 the size is bigger than 100kb')
    #     if ext == 'pdf':
    #         os.remove(image_path)
    #     print(0)
    # else:
    #     print('in quality 1 the size is lesssss than 100kb')
    #     while os.stat(New_image_path).st_size < 100000 and qualityNum < 91:
    #         sleep(1)
    #         os.remove(New_image_path)
    #         qualityNum +=5
    #         image_file.save(New_image_path, format='pdf', optimize=True, quality=qualityNum)
    #         print(f'New picture size is {int(os.stat(New_image_path).st_size)//1000} KB, quality on scale from 1 to 95 equals {qualityNum}')

    #    if os.stat(New_image_path).st_size > 100000:
    #        qualityNum -=5
    #        image_file.save(New_image_path, format='pdf', optimize=True, quality=qualityNum)
if ext == 'pdf':
    os.remove(image_path)
print(0)




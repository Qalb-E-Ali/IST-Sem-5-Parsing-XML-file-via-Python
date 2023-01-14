import xml.etree.ElementTree as ET
import pandas as pd
tree = ET.parse('compiler.xml')
root = tree.getroot()

#storing data
data = []

for book in root.findall('book'):
    book_id = book.get('id')
    author = book.find('author').text
    title = book.find('title').text
    genre = book.find('genre').text
    price = book.find('price').text
    publish_date = book.find('publish_date').text
    description = book.find('description').text
    print('\nBook Id:', book_id, '\nAuthor:', author,'\nTitle:', title,'\nGenre:', genre, '\nPrice:', price, '\nPublish Date:', publish_date, '\nDesc:',description)

    # add the extracted data to the list
    data.append([book_id, author, title, genre, price, publish_date, description])

# write the extracted data to an excel file
df = pd.DataFrame(data, columns=["Book Id", "Author Name", "Title", "Genre", "Price", "Publish_Date", "Description"])
df.to_excel("200901105_Assign_03.xlsx", index=False)
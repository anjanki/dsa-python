import fitz  # PyMuPDF

doc = fitz.open("C:/Users/anjan/Desktop/pdf/anjan report.pdf")

page = doc[0]  # first page

# Add new text
page.insert_text((100, 100), "Hello Anjan!", fontsize=12)

doc.save("edited.pdf")
page.insert_text((200, 200), "New Text")
# Draw white rectangle (hide old text)
page.draw_rect((100, 100, 300, 130), color=(1,1,1), fill=(1,1,1))

# Add new text
page.insert_text((100, 110), "Updated Text", fontsize=12)
doc.save("edited.pdf")

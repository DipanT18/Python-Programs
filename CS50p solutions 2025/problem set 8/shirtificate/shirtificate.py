from fpdf import FPDF
pdf = FPDF(orientation="portrait", format="A4")
pdf.set_font("Times",size=30)
pdf.add_page()
pdf.cell(0,60,"Cs50 shirtificate",new_x="LMARGIN",new_y="NEXT",align="C")
pdf.image("shirtificate.png",w=pdf.epw)
pdf.set_font_size(45)
pdf.set_text_color(255,255,255)
pdf.text(x=47.5,y=140,text=f"{input("enter your name: ")} took CS50")

pdf.output("shirtificate.pdf")


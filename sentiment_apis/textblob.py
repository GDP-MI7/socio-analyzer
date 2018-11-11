from textblob import TextBlob

from openpyxl import load_workbook
wb = load_workbook(filename='../input_files/Manualvalidation_weather.xlsx')
ws = wb['Sheet2']

op = open("../output_files/outputTextBlob.csv","w")

for row in ws.rows:
    for cell in row:
        result = TextBlob(cell.value)
        if result.sentiment.polarity > 0:
            op.write("Positive\n")
        elif result.sentiment.polarity == 0:
            op.write("Neutral\n")
        else:
            op.write("Negative\n")

op.close()
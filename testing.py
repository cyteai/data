input_data = """<output>\n6| residence in india \n7| misc</output>"""

raw = input_data.split('<output>')[1].strip().split('</output>')[0].strip().split('\n')
print(raw)
c=0
output={}
for i in range(len(raw)):
    output[i] = raw[i].split('|')[1]


print(output)
    


def MakeDict(data):
    f = open("DictionaryFormat.txt","w+")
    output = ''
    acceptable_distance = 0.01
    shape_begin = 0
    shape_end = 0
    name_begin = 0
    name_end = 0
    in_shape = False
    in_name = False
    found_name = False
    name = ''
    count = 0
    for i in range(len(data)):
        if(i>20):
            if (data[i-len('<SimpleData name="ctyua17nm">'):i]) == '<SimpleData name="ctyua17nm">':
                name_begin = i
                in_name = True
                print('found name')
            if (data[i-len('</SimpleData>'):i]) == '</SimpleData>' and in_name:
                found_name = True
                in_name = False
                name_end = i-len('</SimpleData>') - 1
                name = data[name_begin:name_end+1]
                print(name)
            if (data[i-len("<coordinates>"):i]) == "<coordinates>":
                print("found coordinate " + str(count) + " " + str(i/len(data)*100) + "%")
                count += 1
                in_shape = True
                shape_begin = i
            if (data[i-len("</coordinates>"):i]) == "</coordinates>":  
                shape_end = i-len("</coordinates>") - 1
                if found_name:
                    found_name = False
                    output += '\n'
                    output += '{"' + name + '", new List<Pos>(){'
                    coordinate_array = data[shape_begin:shape_end].split(" ")
                    n = len(coordinate_array)
                    for j in range(n):
                       output += " new Pos("
                       output += coordinate_array[j]
                       if j == n-1:
                          output += ')'
                       else:
                          output += '),'
                    output += ' } },'

                in_shape = False
    output = output[:-1]
    f.write(output)
    f.close()

def MakeAverageDict(data):
    f = open("DictionaryFormatAverage.txt","w+")
    output = ''
    acceptable_distance = 0.01
    shape_begin = 0
    shape_end = 0
    name_begin = 0
    name_end = 0
    in_shape = False
    in_name = False
    found_name = False
    name = ''
    count = 0
    for i in range(len(data)):
        if(i>20):
            if (data[i-len('<SimpleData name="ctyua17nm">'):i]) == '<SimpleData name="ctyua17nm">':
                name_begin = i
                in_name = True
                print('found name')
            if (data[i-len('</SimpleData>'):i]) == '</SimpleData>' and in_name:
                found_name = True
                in_name = False
                name_end = i-len('</SimpleData>') - 1
                name = data[name_begin:name_end+1]
                print(name)
            if (data[i-len("<coordinates>"):i]) == "<coordinates>":
                print("found coordinate " + str(count) + " " + str(i/len(data)*100) + "%")
                count += 1
                in_shape = True
                shape_begin = i
            if (data[i-len("</coordinates>"):i]) == "</coordinates>":  
                shape_end = i-len("</coordinates>") - 1
                if found_name:
                    found_name = False
                    output += '\n'
                    output += '{"' + name + '", new Pos('
                    coordinate_array = data[shape_begin:shape_end].split(" ")
                    n = len(coordinate_array)
                    sumlat = 0
                    sumlong = 0
                    for j in range(n):
                       a = coordinate_array[j].split(",")
                       print(a[0])
                       try:
                        sumlat += float(a[0])
                        sumlong += float(a[1])
                       except:
                           print(a[0])
                    output += str(sumlat/n) + ','
                    output += str(sumlong/n) + ')},'
                    output += '\n'

                in_shape = False
    output = output[:-1]
    f.write(output)
    f.close()

#g = open("Output2.txt","r")
#content = g.read()
#MakeDict(content)


g = open("Output2.txt","r")
content = g.read()
MakeAverageDict(content)

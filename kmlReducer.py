import math

def Reduce(data):
    f = open("Output.txt","w+")
    output = ''
    acceptable_distance = 0.01
    shape_begin = 0
    shape_end = 0
    in_shape = False
    count = 0
    for i in range(len(data)):
        if not in_shape:
            output += data[i]
        if(i>20):
            if (data[i-len("<coordinates>"):i]) == "<coordinates>":
                print("found coordinate " + str(count) + " " + str(i/len(data)*100) + "%")
                count += 1
                in_shape = True
                shape_begin = i
            if (data[i-len("</coordinates>"):i]) == "</coordinates>": 
                output = output[:-1]
                shape_end = i-len("</coordinates>") - 1
                coordinate_array = data[shape_begin:shape_end].split(" ")
                prev_coordinate = [0,0]
                for j in range(len(coordinate_array)):
                    if j > 3:
                        coordinate = coordinate_array[j].split(",")
                        delta = 0
                        for k in range(len(coordinate)):
                            coordinate[k] = float(coordinate[k])
                            delta += abs(coordinate[k] - prev_coordinate[k])
                        if delta>acceptable_distance:
                            output += coordinate_array[j]
                            output += " "
                            prev_coordinate = coordinate

                output += "</coordinates><"
                in_shape = False
    f.write(output)


def FactorReducer(data):
    f = open("Output2.txt","w+")
    output = ''
    shape_begin = 0
    shape_end = 0
    in_shape = False
    count = 0
    for i in range(len(data)):
        if not in_shape:
            output += data[i]
        if(i>20):
            if (data[i-len("<coordinates>"):i]) == "<coordinates>":
                print("found coordinate " + str(count) + " " + str(i/len(data)*100) + "%")
                count += 1
                in_shape = True
                shape_begin = i
            if (data[i-len("</coordinates>"):i]) == "</coordinates>": 
                output = output[:-1]
                shape_end = i-len("</coordinates>") - 1
                coordinate_array = data[shape_begin:shape_end].split(" ")
                prev_coordinate = [0,0]
                divider = int(math.log(len(coordinate_array)))
                if(len(coordinate_array) < 20):
                    divider = int(divider/1.5)
                if(divider == 0):
                    divider = 1
                for k in range(len(coordinate_array)):
                    if k > 3:
                        coordinate = coordinate_array[k].split(",")
                        for j in range(len(coordinate)):
                            coordinate[j] = float(coordinate[j])
                        if k % divider == 0:
                            output += coordinate_array[k]
                            output += " "
                            prev_coordinate = coordinate

                output += "</coordinates>"
                in_shape = False
    f.write(output)
    f.close()

g = open("Output.txt","r")
#g = open("Boundaries.txt","r")
content = g.read()
#Reduce(content)
FactorReducer(content)

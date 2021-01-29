base_dir = "C:/Users/ranitd/Desktop/New folder/project1/pro2/"
y = y1 = 640;
x = 20;
id = 1;

xlimit=20
ygouplimit1=600
ygouplimit2=680
yuplimit1=400
yuplimit2=480
xuplimityellow=800
xuplimitgreen=400
xuplimitblue=820
mydict = {}

def split(x, y, z, id):
    if(id >= 20):
        for j in mydict:
            if(0<=mydict[j][0] and mydict[j][0]<=3):
                if (mydict[j][0] == 0 and mydict[j][1] < xuplimitblue and mydict[j][2] >= yuplimit1 and mydict[j][2] <= yuplimit2):
                    mydict[j][1] = mydict[j][1] + 20
                    myfile.write('%d\t' % mydict[j][1])
                    myfile.write('%d\t' % mydict[j][2])
                    myfile.write('%d\t' % mydict[j][0])
                    myfile.write('%d\n' % j)
                elif (mydict[j][0] == 1 and mydict[j][1] < xuplimityellow and mydict[j][2] >= yuplimit1 and mydict[j][2] <= yuplimit2):
                     mydict[j][1] = mydict[j][1] + 20
                     myfile.write('%d\t' % mydict[j][1])
                     myfile.write('%d\t' % mydict[j][2])
                     myfile.write('%d\t' % mydict[j][0])
                     myfile.write('%d\n' % j)
                elif (mydict[j][0] == 2 and mydict[j][1] < xuplimitgreen and mydict[j][2] >= yuplimit1 and mydict[j][2] <= yuplimit2):
                      mydict[j][1] = mydict[j][1] + 20
                      myfile.write('%d\t' % mydict[j][1])
                      myfile.write('%d\t' % mydict[j][2])
                      myfile.write('%d\t' % mydict[j][0])
                      myfile.write('%d\n' % j)
                elif (mydict[j][0] == 3 and mydict[j][1] == xlimit and mydict[j][2] >= yuplimit1 and mydict[j][2] <= yuplimit2):
                      myfile.write('%d\t' % mydict[j][1])
                      myfile.write('%d\t' % mydict[j][2])
                      myfile.write('%d\t' % mydict[j][0])
                      myfile.write('%d\n' % j)
                elif(mydict[j][1] == xlimit and mydict[j][2] >= yuplimit1 and mydict[j][2] <= ygouplimit2):
                      mydict[j][2] = mydict[j][2] - 20
                      myfile.write('%d\t' % mydict[j][1])
                      myfile.write('%d\t' % mydict[j][2])
                      myfile.write('%d\t' % mydict[j][0])
                      myfile.write('%d\n' % j)
                elif(mydict[j][1] > xlimit and mydict[j][2] >= ygouplimit1 and mydict[j][2] <= ygouplimit2):
                      mydict[j][1] = mydict[j][1]-20
                      myfile.write('%d\t' % mydict[j][1])
                      myfile.write('%d\t' % mydict[j][2])
                      myfile.write('%d\t' % mydict[j][0])
                      myfile.write('%d\n' % j)

    y = y + z
    myfile.write('%d\t' % x)
    myfile.write('%d\t' % y)
    if (x <= 200):
        myfile.write('1\t');
        mydict[id] = [1, x, y]
    elif (x >= 200 and x <= 400):
        myfile.write('2\t')
        mydict[id] = [2, x, y]
    elif (x >= 400 and x <= 500):
        myfile.write('3\t')
        mydict[id] = [3, x, y]
    elif (x >= 500 and x <= 700):
        myfile.write('4\t')
        mydict[id] = [4, x, y]
    else:
        myfile.write('5\t')
    myfile.write('%d\n' % id)


with open(base_dir + 'positions1' + ".txt", "w") as myfile:
    myfile.write('%d\t' % x)
    myfile.write('%d\t' % y)
    myfile.write('0\t')
    myfile.write('%d\n' % id)
    mydict[id] = [0,x,y]
    x = x + 20;
    for i in range(60):
        id = id + 1;
        split(x, y, 20, id);
        id = id + 1;
        split(x, y, 40, id);
        id = id + 1;
        split(x, y, -20, id);
        id = id + 1;
        split(x, y, -40, id);
        x = x + 20;

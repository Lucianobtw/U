import serial as RS, random as ra, time as ti

MyS = RS.Serial('COM2')
t = ''
while 1:
 if ra.randint(1,3) == 1:
    t = str(ra.randint(1,4)) + ',' + 'U\n'
    MyS.write(t)
 if ra.randint(1,3) == 2:
    t = str(ra.randint(1,4)) + ',' + 'D\n'
    MyS.write(t)
 if ra.randint(1,3) == 3:
    t = str(ra.randint(1,4)) + ',' + 'N\n'
    MyS.write(t)
 print 'Send: ' + t
 ti.sleep(0.01)
MyS.close()


# Solution to rope intranet puzzle from google code jam round 1C 2010 
# pass command line parameters of input file name and output file name
# By Zack Akil 24/05/2016 

import sys

# problem logic

def ropeIntranet( r , l ):
   output = 0
   rightWindows = [r[0]]
   leftWindows = [l[0]]
   for x in range(1, len(r)):
      for y in range(0, len(rightWindows)):
        if (r[x]>rightWindows[y])and(l[x]<leftWindows[y])or(r[x]<rightWindows[y])and(l[x]>leftWindows[y]):
           output += 1
      rightWindows.extend([r[x]])
      leftWindows.extend([l[x]])      
   return output

# small test case

leftBuilding = [1,8]
rightBuilding = [7,2]

print ('test case : {}'.format(ropeIntranet(leftBuilding,rightBuilding)))

# file reading/writing logic

if len(sys.argv) >=3:
  inputFile = sys.argv[1]
  outputFile = sys.argv[2]
else:
  inputFile = input('Enter input file name: ')
  outputFile = input('Enter output file name: ')

f = open(inputFile, 'r')

print("reading file...")
data = map(int,f.read().split())
outputs = []
testCount = data[0]
pos = 1
for x in xrange(0,testCount):
  windowCount = data[pos]
  lwind = []
  rwind = []
  for y in xrange(1,windowCount*2,2):
    lwind.extend([data[pos+y]])
    rwind.extend([data[pos+y+1]]) 
  outputs.extend([ropeIntranet(lwind,rwind)])  
  pos += (windowCount*2)+1
print(outputs)

w = open(outputFile, 'w')
for x in xrange(0,testCount):
  w.write('Case #{}: {}'.format(x+1, outputs[x]))
  if x < testCount - 1:
     w.write('\n')


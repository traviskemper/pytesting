mport os

os.getcwd()

os.chdir('/Users/tkemper/Development/streamm-tools/streamm/structure')

with open('containers.py','r') as fl:
    lines = fl.readlines()

for line in lines:
    if( 'def' in line ):
        l1 = line.replace('def','')
        l2 = l1.split('(')
        func_name = l2[0].strip()
        print('test_{}'.format(func_name))
        
        
        
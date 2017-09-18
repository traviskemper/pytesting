import os, os.path
from optparse import OptionParser

os.getcwd()


def get_options():
 
    usage = "usage: %prog file [options] \n"
    parser = OptionParser(usage=usage)
    
    parser.add_option('-t',"--testnames", dest="testnames", default=False,action="store_true", help="Print test names for all functions in python file")
    parser.add_option('-p',"--propertyfunc", dest="propertyfunc", default=False,action="store_true", help="Print property functions")
    #
    (options, args) = parser.parse_args()
        
    return options, args

def print_testnames(lines):
        
    for line in lines:
        if( 'def' in line ):
            l1 = line.replace('def','')
            l2 = l1.split('(')
            func_name = l2[0].strip()
            print('test_{}'.format(func_name))

def print_propertyfunctions(lines):
    properties = []
    for line in lines:
        if( '_property[\'' in line  and '=' in line ):
            l1 = line.split('\'')
            prop_key = l1[1]
            #
            if( prop_key not in properties ):
                dec = '@property \ndef {0}(self): \n    return self._property[\'{0}\']'.format(prop_key)
                print dec
                setter = '@{0}.setter \ndef {0}(self,value): \n    self._property[\'{0}\'] = value'.format(prop_key)
                print setter
                
                properties.append(prop_key)

def main():
    import copy
    options, args = get_options()
    
    file_path = args[0]
    print "File:{}".format(file_path)
    print options

    with open(file_path,'r') as fl:
        lines = fl.readlines()
        
    if( options.testnames ): print_testnames(lines)
    if( options.propertyfunc ):
        properties = print_propertyfunctions(lines)

if __name__ == '__main__':
    main()
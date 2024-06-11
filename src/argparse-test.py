import argparse

# other code. . .

def main(args):
    print('Hello, %s!' % args.name)
    print(f'flags {args.foo}')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'Say hello')
    
    parser.add_argument('name', help='your name, enter it')
    
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                      help='an integer for the accumulator')
    
    parser.add_argument('--sum', dest='accumulate', action='store_const',
						const=sum, default=max,
						help='sum the integers (default: find the max)')
    
    parser.add_argument('--foo', 
                         help='enter something')
						
    args = parser.parse_args()

    main(args)
import sys

# from http://automatthias.wordpress.com/2007/04/28/cartesian-product-of-multiple-sets/
def cartesian_product(L,*lists):
    if not lists:
        for x in L:
            yield (x,)
    else:
        for x in L:
            for y in cartesian_product(lists[0],*lists[1:]):
                yield (x,)+y

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        if len(line.strip()) > 0:
            length, string = line.strip().split(',')
            char_list = list(string)
            dimensions = []
            for x in range(0, int(length)):
                dimensions.append(char_list)
            
            products = set()
            for i in cartesian_product(*dimensions):
                products.add(i)
            print ','.join(''.join(product) for product in sorted(products))

            
    sys.exit(0)

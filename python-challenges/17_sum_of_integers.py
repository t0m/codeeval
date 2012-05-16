import sys

def top_cont_sum(num_list):
    top_sum = 0
    
    for idx in range(0, len(num_list)):
        cur_sum = 0
        for num in range(idx, len(num_list)):
            cur_sum += num_list[num]
            if cur_sum > top_sum:
                top_sum = cur_sum
                
    print top_sum
    

if __name__ == '__main__':
    for line in open(sys.argv[1]):
        top_cont_sum([int(n.strip()) for n in line.strip().split(',')])
         
    sys.exit(0)

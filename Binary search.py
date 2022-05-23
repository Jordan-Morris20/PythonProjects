"""
Iterative approach
"""

def binary_search(list,item):
    """_summary_
    Find item in sorted list based on binary search
    Args:
        list (seq): ordered list of even numbers
        item (number): number to find position of in list
    """
      
    start = 0
    end = len(list)-1
    
    while start <= end:
        i = (start + end)//2
        if len(list) == 0:
            return print(item,'not found in list') 
        else:
            if list[i] == item:
                return print('found at position',i)
            else:
                if list[i] < item:
                    return binary_search(list[i+1:],item)
                else:
                    return binary_search(list[:i],item)
            
            
binary_search([0,2,4,6,8,10,12,16,20],10)
def parent(num):

    def first_child():
        print('I am Anna, the first child')

    def sec_child():
        print('I am Bob, the second child')

    

    if num == 1:
        return first_child
    else:
        return sec_child
    
    

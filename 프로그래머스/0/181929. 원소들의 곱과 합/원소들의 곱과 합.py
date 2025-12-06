def solution(num_list):
    hap = 0
    gop = 1
    for i in range(len(num_list)):
        hap += num_list[i]
        gop *= num_list[i]
        
    if gop < hap**2:
        return 1
    else:
        return 0
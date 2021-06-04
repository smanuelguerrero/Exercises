def remove_nums(int_list):
  position = 3-1
  idx = 0
  len_list = (len(int_list))
  while len_list>0:
    idx = (position+idx)%len_list
    print(int_list.pop(idx))
    len_list -= 1
nums =[1,2,3,4,5,6,7,8,9]
remove_nums(nums)

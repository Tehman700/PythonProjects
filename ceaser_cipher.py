import random
import math

list =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'
       ,'Q','R','S','T','U','V','W','X','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'
       ,'Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

option = int(input("1.Encode\n2.Decode\n"))



entered = input("Enter what you want to Encode: ").lower()
shift = int(input("Enter the Shift Number: "))
# def checker(spl,list):
    



# def decode(spl,list):
    
if option == 1:
    final_text = ""
    for char in entered:
        ii = list.index(char)
        ii_n = ii+shift
        final_text +=list[ii_n]
    print(f"{final_text}")

elif option==2:
    final_text = ""
    for char in entered:
        ii = list.index(char)
        ii_n = ii-shift
        final_text +=list[ii_n]
    print(f"{final_text}")

else:
    print("You chose wrong Option!!")



# if result == True:
#     print("YES")
# else:
#     print("NOT")



# THIS IS KNOWN AS USING A LOOP APPRAOCH
# def are_characters_in_provided_list(input_list, provided_list):
#     for char in input_list:
#         if char not in provided_list:
#             return False
#     return True

# # Example usage
# input_list = ['a', 'b', 'c']
# provided_list = ['a', 'b', 'c', 'd', 'e']
# result = are_characters_in_provided_list(input_list, provided_list)
# print(result)  # Output: True

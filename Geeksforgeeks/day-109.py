# Even Positioned Characters

# You are given a String S, you need to print its characters at even indices(index starts at 0).

# Examples:
# Input: s = "Geeks"
# Output: Ges   
# Explanation: The even indices (0, 2 & 4) characters are printed.
# Input: s = "DoctorPhenomenal"
# Output: DcoPeoea
# Explanation: The even indices characters are printed.


# def utility(s):

#     for i in range(0, len(s), 2):
#         print(s[i], end="")
          

# utility("Geeks")        
# utility("DoctorPhenomenal")        

# 
# def utility(s):
#     result = ""
#     for i in range(len(s)):
#         if i % 2 ==0 :
#             result +=s[i]
#     print(result)        

# utility("Geeks")
# utility("DoctorPhenomenal")

#
def utility(s):
    result = ""
    n = len(s)
    i = 0
    while(i<n) :
        result += s[i] 
        i+=2
    print(result)    

utility("Geeks")
utility("DoctorPhenomenal")

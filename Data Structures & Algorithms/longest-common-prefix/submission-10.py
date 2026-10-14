#some exxtra things
#for list
#enumerate()
#for i,v in enumerate(list):
#index and values

#for dict
#key and value
#for k,v in dict.items():
#key
#for k in d: or for k in d.keys():
#values
#for v in d.values():

#min_len_word_inside_a_list = min(strs,key=len)
#we can give else with for loop:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            
        # Step 1: Start with the shortest string as the initial guess
        num = min(strs, key=len)
        
        # Step 2: Loop through each word to verify the prefix
        for word in strs:
            # Shorten 'num' until 'word' starts with it
            while not word.startswith(num):
                num = num[:-1]  # Slice off the last character
                
                # If it becomes empty, there is no common prefix
                if not num:
                    return ""
                    
        return num
             












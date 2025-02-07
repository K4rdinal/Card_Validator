import re   
class typer :


    def getCardType(nums):
            """
            checks card's first number with regex module. Returns value
            with if-else statement  

            """
            match = re.search(r'^4',nums)
            if match :
                return "Card type is visa."
            elif re.search(r'^5',nums):
                return "Card type is master card"
            elif re.search(r'^3',nums):
                return "Card type is american express"
            else :
                return "Card type is unknown"
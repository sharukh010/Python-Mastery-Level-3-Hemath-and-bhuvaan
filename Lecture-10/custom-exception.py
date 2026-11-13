class HemanthNotJoinedError(Exception): 
    pass 

class BhuvaanNotJoinedError(Exception): 
    pass 

class StudentNotJoinedError(Exception): 
    pass 

raise StudentNotJoinedError("Hemanth has not joined the class yet.")
# raise BhuvaanNotJoinedError("Bhuvaan has not joined the class yet.")
# raise HemanthNotJoinedError("Hemanth has not joined the class yet.")
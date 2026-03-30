class Solution:
    def countSeniors(self, details: List[str]) -> int:
        old_age_counter = 0
        for detail in details:
            age = ""
            age = age + detail[-4] + detail[-3]
            if int(age) > 60:
                old_age_counter = old_age_counter + 1 
        return old_age_counter
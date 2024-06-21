class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):

        result=0

        for i in range(len(customers)):
            if grumpy[i]==0:
                result+=customers[i]
        

        current_additional_satisfied=0
        max_additional_satisfied=0

        for i in range(len(customers)):
            if grumpy[i] == 1:
                current_additional_satisfied += customers[i]

            if i >= minutes and grumpy[i - minutes] == 1:
                current_additional_satisfied -= customers[i - minutes]

            max_additional_satisfied = max(max_additional_satisfied, current_additional_satisfied)

        return result + max_additional_satisfied
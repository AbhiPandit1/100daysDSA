class Solution(object):
    def maxDistance(self, position, m):
        # Sort the positions in ascending order
        position.sort()

        # Function to check if it's possible to place 'm' elements with at least 'force' distance apart
        def forcePossible(force):
            prevPosition = position[0]  # Initialize the previous position to the first element
            count = 1  # Start with one element placed

            # Iterate through the positions
            for i in range(1, len(position)):
                currPosition = position[i]
                if currPosition - prevPosition >= force:
                    count += 1  # Increment count if current position satisfies the distance constraint
                    prevPosition = currPosition  # Update previous position to current position
                    if count == m:
                        return True  # Return True if 'm' elements have been placed
            return False  # Return False if it's not possible to place 'm' elements with at least 'force' distance apart

        minForce = 0  # Minimum possible distance (considering the edge case where 'm == 1')
        maxForce = max(position)  # Maximum possible distance between the first and last position
        result = 0  # Initialize the result variable to store the maximum minimum distance found

        # Binary search loop to find the maximum minimum distance
        while minForce <= maxForce:
            midForce = minForce + (maxForce - minForce) // 2  # Calculate the midpoint force

            if forcePossible(midForce):
                result = midForce  # Update result to current midForce if placing 'm' elements is possible
                minForce = midForce + 1  # Adjust the search range to the right half
            else:
                maxForce = midForce - 1  # Adjust the search range to the left half

        return result  # Return the maximum minimum distance found

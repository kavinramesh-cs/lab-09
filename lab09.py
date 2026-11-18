# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first):
    #   Restate:find the two position whose values add up to target.
    #   Example: [2, 7, 11, 15], target 9 -> at 2, I need 7 (not seen yet), so
    #     remember 2. At 7, I need 2, which I saw at index 0 -> [0, 1].
    #   Brute force: try every pair, O(n^2).
    #   Faster: keep a dict of value -> index for numbers seen so far. For each
    #     number, look up (target - number). One pass, O(n).
    seen = {}
    for i,n in  enumerate(nums):
        need = target -n
        if need in seen:
            return[seen[need],i]
        seen[n] =i

def max_profit(prices):
    # Outline:
     #   Restate: best (sell price - buy price) with the buy day before the sell day.
    #   Example: [7, 1, 5, 3, 6, 4] -> cheapest so far is 1, selling at 6 gives 5.
    #   Brute force: try every (buy, sell) pair, O(n^2).
    #   Faster: walk through the days tracking the cheapest price seen so far.
    #     Each day, profit if I sold today = price - cheapest. Keep the best. O(n).
      cheapest = float("inf")
      best = 0
      for p in prices:
          cheapest = min(cheapest, p)
          best = max(best,p -cheapest )
          return best 
      
      
def max_subarray(nums):
   
     # Outline:
     #   Restate: largest sum of a block of consecutive numbers.
      #   Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> the block 4, -1, 2, 1 sums to 6.
      #   Brute force: sum every start/end pair, O(n^2).
      #   Faster: at each number, either extend the running block or start a new one
      #     here. If the running sum is negative, it only hurts, so start fresh.
      #     Track the best sum seen. O(n).
      current = best = nums[0]
      for n in nums[1:]:
        current = max(n, current + n)
        best = max(best, current)
      return best

def is_balanced(s):   # Part 4 - stretch (optional)
  # Outline:
    #   Restate: every bracket must be closed by the matching type, in the right order.
    #   Example: "([)]" -> push (, push [, then ) arrives but the top is [ -> False.
    #   Approach: stack. Push each opener. On a closer, the stack must be non-empty
    #     and its top must be the matching opener, otherwise return False.
    #     At the end, the stack must be empty (no unclosed openers).
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([2, 7, 11, 15], 9))                      # [0, 1]
    print(two_sum([3, 2, 4], 6))                           # [1, 2]
    print(max_profit([7, 1, 5, 3, 6, 4]))                  # 5
    print(max_profit([7, 6, 4, 3, 1]))                     # 0
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6
    print(max_subarray([5, 4, -1, 7, 8]))                  # 23
    print(is_balanced("()[]{}"), is_balanced("{[]}"), is_balanced("([)]"))  # True True False


if __name__ == "__main__":
    main()

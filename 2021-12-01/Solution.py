class Solution:
    def rob(self, nums):
        preprior, prior, current = 0, 0, 0
        for i in nums:
            current = max(prior, i + preprior)
            preprior = prior
            prior = current
        return current

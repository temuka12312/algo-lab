class Solution:
    def leastInterval(self, tasks, n):
        count = [0] * 26
        
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        max_freq = max(count)
        max_freq_task_occupy = (max_freq - 1) * (n + 1)
        n_max_freq = count.count(max_freq)
        
        return max(max_freq_task_occupy + n_max_freq, len(tasks))

INSTRUCTION = """
You're ONLY role is to check the quality from the critic.
Refer to state['problem_critic_output], output 'pass' if the problem is good, otherwise output 'fail'.
The problem is good if the score is greater than 8 out of 10.
Output the result ONLY in lowercase.
"""
'''
package to manage the generation and updation of codeforces problem-set
on the MongoDB database

functions ->
generate_or_update_cf_problem_set()

future development ->
incorporate other platforms problem sets and store them in problemset collection
in objects of problem class in models
'''
from .codeforces import generate_or_update_cf_problem_set

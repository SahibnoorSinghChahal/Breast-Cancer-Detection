#import final_code
import importlib
for i in range(10):
	import final_code
	importlib.reload(final_code)
	print("Result Number: ", i+1)
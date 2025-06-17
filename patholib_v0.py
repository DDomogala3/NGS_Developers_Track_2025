# patholib
#the goal is to increase access to R and python libraries for experts in the field (pathologists, clinicians) who are 
#a novice in computational biology. 
datascience_libs = ["pandas", "polars", "matplotlib", "numpy"]
ml_libs = ["pytorch", "tensorflow"]
R_packages = ["maftools","fishplot"]

path_input = input("""Hello welcome to patholib, I am your concierge, I can assist you in translating your data.
Please tell me what libraries do you want to use for your project?: """)
print("So I understand you want to install and use {}, please let me help you with that." .format(path_input))
#def patholib_intro()
class patholib():
	def __init__(self,intro,libs):
		self.intro = intro
		self.libs = libs
		
	def concierge(self):
		#maybe get a small LLM to help
		intro = input("How can I help you today?: ")
		
		
		
		
		
	
#patholib(intro)


import importlib



class ModuleFactory:

	
	def __new__(cls,name,source):

		_globals = {}
		exec(compile(source,name,'exec'),_globals)

		new_mod = ModuleFactory.new_module(name)

		for key in _globals:
			setattr(new_mod,key,_globals[key])

		return new_mod	
	
	@staticmethod
	def new_module(name):
		
		spec = importlib.machinery.ModuleSpec(name,None)
		return importlib.util.module_from_spec(spec)

functions = {}



mods = [('echo',"def run(input): return \"echo: {}\".format(input)"),
	 ('repeat',""" 
def run(input):
	return rpt(input)

def rpt(input):
	return [input for i in range(3)]

""")]

for m in mods:

	
	
	functions[m[0]]=ModuleFactory(m[0],m[1])




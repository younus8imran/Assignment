import os  
from .base import * 

if os.environ.get('assign') == 'production':
	from .production import *
else:
	from .development import * 

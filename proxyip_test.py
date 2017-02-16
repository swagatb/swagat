import json
import urllib2
#from public.models import ProxyPool
class proxy_generator(object):
	def __init__(self):
		self.proxy_dict = self.proxy_ip_gen()
		self.proxy_gen = self.proxy_gen_obj(self.proxy_dict)
		
	def proxy_ip_gen(self):
		api_url_initial='http://ninjaproxies.com/proxies/api/'
		api_key = 'key=1402490935541334796140249093514024909351164891'
		api_fields= 'fields=ip+portNum'
		api_port = 'portNum=80+8000+8080+3128'
		api_google_active = 'google=1'
		api_url = api_url_initial +'?'+api_key+'&'+api_fields+'&'+api_port+'&'+api_google_active
		p_dict=json.load(urllib2.urlopen(api_url))
		#print 'proxy_dict   ',proxy_dict['data'][0]['Proxy']
		return p_dict
	
	def proxy_gen_obj(self,proxy_dict):
		for proxy_row in self.proxy_dict['data']:
			#print 'proxy_row',proxy_row
			proxy_url= str(proxy_row['Proxy']['ip']) +':'+str(proxy_row['Proxy']['portNum'])
			#print 'proxy_url     ',proxy_url
			yield proxy_url
	def main_fun(self):
		while True:
			try:
				return next(self.proxy_gen)
			except StopIteration :
				self.proxy_dict = self.proxy_ip_gen()
				self.proxy_gen = self.proxy_gen_obj(self.proxy_dict)
				
class CustomMiddleware(object):
	def __init__(self):
		self.proxy_generator_obj = proxy_generator()
	def process_request(self, request, spider):
		try:
			print request.meta, "META INFO"
			
			while True:
				proxy_url = str(self.proxy_generator_obj.main_fun())
				#check weather proxy is valid
				try:
					invalid_proxy = ProxyPool.objects.get(url = proxy_url)
					pass
				except:
					break
			
			# Configure the middleware with the new proxy.    
			request.meta['proxy'] = "http://%s" %proxy_url
		
		except Exception as e:
		    print str(e), 'err'
		    #client.captureException()
		
		print request.meta['proxy'], 'PROXY SET'
		print request.meta, 'META DATA'
		   
if __name__=="__main__":
	
	proxy_generator_obj = proxy_generator()
	for x in xrange(100000):
		proxy_url = str(proxy_generator_obj.main_fun())
		print proxy_url

	
	

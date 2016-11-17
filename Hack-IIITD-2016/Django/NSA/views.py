from django.shortcuts import render
from django.template import loader, Context, Template
from django.http import HttpResponse, HttpResponseRedirect
import collections

def home(request):
	template = loader.get_template('nsa/home.html')
	return HttpResponse(template.render(request))
def analyse(request):
	f = open("./nsa/d.txt",'r')
	f1 = open("./nsa/dest_host.txt",'r')
	site = {}
	site_name = []
	for line in f1:
		if(line.rstrip() not in site_name):
			site_name.append(line.rstrip())
		if(line.rstrip() not in site):
			site[str(line.rstrip())] = 1
		elif(line.rstrip() in site):
			site[str(line.rstrip())] += 1 
	site_name.sort()
	print(site_name)
	print(site)
	sorted_dict = collections.OrderedDict(sorted(site.items()))
	template = loader.get_template('nsa/analyse.html')
	context = {
		'site1' : site_name[0],
		'site2' : site_name[1],
		'site3' : site_name[2],
		'site4' : site_name[3],
		'site5' : site_name[4],
		'site6' : site_name[5],
		'site1_data' : sorted_dict[site_name[0]],
		'site2_data' : sorted_dict[site_name[1]],
		'site3_data' : sorted_dict[site_name[2]],
		'site4_data' : sorted_dict[site_name[3]],
		'site5_data' : sorted_dict[site_name[4]],
		'site6_data' : sorted_dict[site_name[5]],
	}
	return HttpResponse(template.render(context, request))

def block(request):
	f0 = open("./nsa/d.txt",'r')
	f3 = open("./nsa/dest_host.txt",'r')
	f1 = open("./nsa/mac_ip.txt",'r')
	f2 = open("./nsa/user_ip.txt",'r')
	lis = []
	dest = []
	user = []
	mac = []
	for line in f3:
		dest.append(line.split())
	for line in f0:
		lis.append(line.split())
	for line in f2:
		user.append(line.split())
	for line in f1:
		mac.append(line.split())
	final1 = []
	final2 = []
	final1 = zip(user,mac)
	final2 = zip(lis,dest)
	template = loader.get_template('nsa/block.html')
	context = {
		'table' : final2,
		'mac' : final1,
	}
	return HttpResponse(template.render(context, request))	
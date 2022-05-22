import os
import pathlib

def ten_exp(num):
	d = 0
	while 9 < (num//(10**d)):
		d += 1
	return d

def zeros_string(num, dec):
	res = ""
	for i in range(0,dec-ten_exp(num)):
		res = "0" + res
	res = res + str(num)
	return res

def zeros_numbers(num_elements):
	nums_str = [""]*num_elements

	for i in range(0,num_elements):
		nums_str[i] = zeros_string(i+1, ten_exp(num_elements))
	return nums_str

def rename_shu(path):
	files = os.listdir(path)
	for f in files:
		chap = path + "/" + f
		os.chdir(chap)
		images = os.listdir(".")
		nums = zeros_numbers(len(images))
		for image in images:
			for i in range(0,len(images)):
				if ("_"+str(i+1)+".") in image:
					print("Cambie nombere de "+image+"   a   "+"c"+f[-2:]+"_"+nums[i]+".png")
					os.rename(image,"c"+f[-2:]+"_"+nums[i]+".png")
		os.chdir("..")

rename_shu("/mnt/e/Mangas/Shuumatsu no Valkirie Record of ragnarok")

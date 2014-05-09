def gen_submission():
	num=1
	file=open('submission_svc_poly_degree_3_c_1.txt','w')
	file.write('ImageId,Label\n')
	for line in open('svc_poly_degree_3_c_1.txt'):
		file.write(str(num)+','+str(line.strip())+'\n')
		num+=1
	file.close()


if __name__=='__main__':
	gen_submission()

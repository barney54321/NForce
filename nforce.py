try:
	height=int(input("Enter height: "))
except ValueError:
	print("")
	print("Invalid height.")
	quit()

if height>20 or height<1:
	print()
	print("Invalid height.")
	quit()
try:
	rows=int(input("Enter number of rows: "))
except ValueError:
	print("")
	print("Invalid number of rows.")
	quit()
print("")
if rows>20 or rows<1:
	print("Invalid number of rows.")
	quit()
def printtri(h,s):
	for n in range (0,h-1):
		if len(s)<n+1:
			s.append("")
		if n==h-2:
			s[n]=s[n]+("/"+"_"*(2*n)+"\\")
		else:
			s[n]+=(" "*(h-n-2)+"/"+" "*(2*n)+"\\"+" "*(h-n-2))
	return s
ss=[]
printset=printtri(height+1,ss)
def comtri(r,ro,h,s):
	for item in s:
		item+=item*r
		item=" "*(ro-r-1)*(h)+item
		item=item.rstrip()
		print(item)
i=0
while i<rows:
	comtri(i,rows,height,printset)
	i=i+1

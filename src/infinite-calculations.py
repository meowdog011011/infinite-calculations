# Minified by python-minifier.com
U=range
Q='How many digits would you like to calculate? '
P=str
M=int
H=ValueError
G=input
from time import sleep as B
V=print
def print(string):V(string,end='',flush=True)
print('Welcome to Infinite Calculations\nVersion: 0.3.0-beta\nCopyright 2024 Te Du\n\n')
B(1)
print("What would you like to calculate?\n(A) π: Chudnovsky Algorithm\n(B) π: Gosper's series\n(C) √2\n(D) Fibonacci Sequence\n\n")
B(1)
try:
	K=G('Type A, B, C or D: ').lower();print('\n')
	if K=='a':
		from decimal import Decimal as D,getcontext as N
		def L(a,b):
			if a+1==b:A=-(6*a-5)*(2*a-1)*(6*a-1);B=0x26dd041d878000*a**3;C=A*(545140134*a+13591409)
			else:D=(a+b)//2;E,G,H=L(a,D);I,F,J=L(D,b);A=E*I;B=G*F;C=F*H+E*J
			return A,B,C
		print('Infinite Calculations: The π Calculator\nMethod: Chudnovsky Algorithm\n\n');B(1);A=M(G(Q))
		if A<1:raise H
		N().prec=A+4
		if A+4<28:R,C,E=L(1,2)
		else:from math import ceil;R,C,E=L(1,ceil(A+5/14))
		del R;print('\nπ: '+P(426880*D(10005).sqrt()*D(C)/(13591409*D(C)+D(E)))[:A+2])
	elif K=='b':
		C=60;E=13440;O=10080;F=3;print("Infinite Calculations: The π Calculator\nMethod: Gosper's series\nCredits: Original JavaScript code written by @trincot\n\n");B(1);A=M(G(Q))
		if A<1:raise H
		print('\n\nπ: 3.')
		for S in U(A):T=((F*27-12)*C+E*5)//(O*5);print(T);I=F*3;I=(I+1)*3*(I+2);E=I*10*(C*(F*5-2)+E-O*T);C*=10*F*(F*2-1);F+=1;O*=I
	elif K=='c':
		from decimal import Decimal as D,getcontext as N;print('Infinite Calculations: The √2 Calculator\n\n');B(1);A=M(G(Q))
		if A<1:raise H
		N().prec=A+4;print('\n√2: '+P(D(2).sqrt())[:A+2])
	elif K=='d':
		J=[0,1];print('Infinite Calculations: The Fibonacci Calculator\n\n');B(1);A=M(G('How many terms would you like to calculate? '))
		if A<1:raise H
		print('\nFibonacci Sequence: 0')
		if A>1:print(', 1')
		if A>2:
			for S in U(A-2):
				if S!=A-2:print(', ')
				J.append(J[0]+J[1]);print(J[-1]);del J[0]
	else:raise H
except H:print('\nERROR: Invalid value.')
except MemoryError:print('\nERROR: Not enough memory to complete process.')
except Exception as W:print('\nERROR: '+P(W))
B(1)
G('\n\nPress Enter to exit...')
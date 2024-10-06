# Minified by python-minifier.com
T='How many digits would you like to calculate? '
S=range
K=int
F=ValueError
E=input
from time import sleep as C
X=print
def print(string):X(string,end='',flush=True)
print('Welcome to Infinite Calculations\nVersion: 0.2.0-beta\nCopyright 2024 Te Du\n\n')
C(1)
print("What would you like to calculate?\n(A) π: Chudnovsky Algorithm\n(B) π: Gosper's series\n(C) √2\n(D) Fibonacci Sequence\n\n")
C(1)
try:
	I=E('Type A, B, C or D: ').lower();print('\n')
	if I=='a':
		from decimal import Decimal as B,getcontext as L;M=B(1);N=B(13591409);U=B(1);O=B(6);V=N;print('Infinite Calculations: The π Calculator\nMethod: Chudnovsky Algorithm\n\n');C(1);A=K(E(T))
		if A<1:raise F
		L().prec=A+4
		for J in S(1,A):M=(O**3-16*O)*M/J**3;N+=545140134;U*=-0x3a4b862c4b40000;V+=M*N/U;O+=12
		Y=B(426880)*B(10005).sqrt()/V;print('\nπ: '+str(Y)[:A+2])
	elif I=='b':
		P=60;Q=13440;R=10080;D=3;print("Infinite Calculations: The π Calculator\nMethod: Gosper's series\nCredits: Original JavaScript code written by @trincot\n\n");C(1);A=K(E(T))
		if A<1:raise F
		print('\n\nπ: 3.')
		for J in S(A):W=((D*27-12)*P+Q*5)//(R*5);print(W);G=D*3;G=(G+1)*3*(G+2);Q=G*10*(P*(D*5-2)+Q-R*W);P*=10*D*(D*2-1);D+=1;R*=G
	elif I=='c':
		from decimal import Decimal as B,getcontext as L;print('Infinite Calculations: The √2 Calculator\n\n');C(1);A=K(E(T))
		if A<1:raise F
		L().prec=A+4;print('\n√2: '+str(B(2).sqrt())[:A+2])
	elif I=='d':
		H=[0,1];print('Infinite Calculations: The Fibonacci Calculator\n\n');C(1);A=K(E('How many terms would you like to calculate? '))
		if A<1:raise F
		print('\nFibonacci Sequence: 0')
		if A>1:print(', 1')
		if A>2:
			for J in S(A-2):
				if J!=A-2:print(', ')
				H.append(H[0]+H[1]);print(H[-1]);del H[0]
	else:raise F
except F:print('\nERROR: Invalid value.')
except MemoryError:print('\nERROR: Not enough memory to complete process.')
except:print('\nERROR: Unknown error.')
C(1)
E('\n\nPress Enter to exit...')
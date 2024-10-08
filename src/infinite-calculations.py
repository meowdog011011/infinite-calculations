W=range
R='How many digits would you like to calculate? '
P=str
O=int
F=ValueError
E=input
from time import sleep as C
X=print
def print(string):X(string,end='',flush=True)
print('Welcome to Infinite Calculations\nVersion: 0.3.0-beta\nCopyright 2024 Te Du\n\n')
C(1)
print("What would you like to calculate?\n(A) π: Chudnovsky Algorithm\n(B) π: Gosper's series\n(C) √2\n(D) e\n(E) Fibonacci Sequence\n\n")
C(1)
try:
	I=E('Type A, B, C or D: ').lower();print('\n')
	if I=='a':
		from decimal import Decimal as B,getcontext as J
		def Q(a,b):
			if a+1==b:A=-(6*a-5)*(2*a-1)*(6*a-1);B=0x26dd041d878000*a**3;C=A*(545140134*a+13591409)
			else:D=(a+b)//2;E,G,H=Q(a,D);I,F,J=Q(D,b);A=E*I;B=G*F;C=F*H+E*J
			return A,B,C
		print('Infinite Calculations: The π Calculator\nMethod: Chudnovsky Algorithm\n\n');C(1);A=O(E(R))
		if A<1:raise F
		J().prec=A+4
		if A+4<28:U,D,G=Q(1,2)
		else:from math import ceil;U,D,G=Q(1,ceil(A+5/14))
		del U;print('\nπ: '+P(426880*B(10005).sqrt()*B(D)/(13591409*B(D)+B(G)))[:A+2])
	elif I=='b':
		D=60;G=13440;S=10080;H=3;print("Infinite Calculations: The π Calculator\nMethod: Gosper's series\nCredits: Original JavaScript code written by @trincot\n\n");C(1);A=O(E(R))
		if A<1:raise F
		print('\n\nπ: 3.')
		for K in W(A):V=((H*27-12)*D+G*5)//(S*5);print(V);L=H*3;L=(L+1)*3*(L+2);G=L*10*(D*(H*5-2)+G-S*V);D*=10*H*(H*2-1);H+=1;S*=L
	elif I=='c':
		from decimal import Decimal as B,getcontext as J;print('Infinite Calculations: The √2 Calculator\n\n');C(1);A=O(E(R))
		if A<1:raise F
		J().prec=A+4;print('\n√2: '+P(B(2).sqrt())[:A+2])
	elif I=='d':
		from decimal import Decimal as B,getcontext as J;from fractions import Fraction as Y;T=1;M=0;K=1;print('Infinite Calculations: The e Calculator\n\n');C(1);A=O(E(R))
		if A<1:raise F
		J().prec=A+5
		while B('2e'+P(A))>=T:M+=Y(1,T);T*=K;K+=1
		print('\ne: '+P(B(M.numerator)/B(M.denominator))[:A+2])
	elif I=='e':
		N=[0,1];print('Infinite Calculations: The Fibonacci Calculator\n\n');C(1);A=O(E('How many terms would you like to calculate? '))
		if A<1:raise F
		print('\nFibonacci Sequence: 0')
		if A>1:print(', 1')
		if A>2:
			for K in W(A-2):
				if K!=A-2:print(', ')
				N.append(N[0]+N[1]);print(N[-1]);del N[0]
	else:raise F
except F:print('\nERROR: Invalid value.')
except MemoryError:print('\nERROR: Not enough memory to complete process.')
except Exception as M:print('\nERROR: '+P(M))
C(1)
E('\n\nPress Enter to exit...')
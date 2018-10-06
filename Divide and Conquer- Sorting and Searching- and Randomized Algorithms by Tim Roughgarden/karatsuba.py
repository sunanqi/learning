class Solution:
    def karatsuba(self, n1, n2):
        """
        :type num1, num2: str type of an int
        :rtype: str type of an int
        """
        def m(num1, num2):
            print('num1,num2=', num1,num2)
            if len(num1)<=1 or len(num2)<=1:
                return str(int(num1)*int(num2))
            else:
                if len(num1)>len(num2) or (len(num1)==len(num2) and num1>num2):
                    num1, num2 = num2, num1
                n=len(num1)//2
                a,b = num1[:-n], num1[-n:]
                c,d = num2[:-n], num2[-n:]
                #print('a,b,c,d=',a,b,c,d)
                ac = m(a, c)
                bd = m(b, d)
                abcd = m(str(int(a)+int(b)), str(int(c)+int(d)))
                adbc = str(int(abcd)-int(ac)-int(bd))
                r = int(ac+'0'*(2*n))+int(adbc+'0'*n)+int(bd)
                #print('r=', r)
            return (str(r))

        return m(n1,n2)

n1 = '3141592653589793238462643383279502884197169399375105820974944592'
n2 = '2718281828459045235360287471352662497757247093699959574966967627'
# 123456789*987654321987654321=
test=Solution()
print(test.karatsuba(n1, n2))

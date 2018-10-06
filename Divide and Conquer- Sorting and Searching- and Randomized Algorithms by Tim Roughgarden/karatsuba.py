class Solution:
    def m(self, num1, num2):
        """
        :type num1, num2: str type of an int
        :rtype: str type of an int
        """
        print(num1,num2)
        if len(num1)<=1 and len(num2)<=1:
            return str(int(num1)*int(num2))
        else:
            n=len(num1)//2
            a,b = num1[:n], num1[n:]
            c,d = num2[:n], num2[n:]
            print(a,b,c,d)
            ac = self.m(a, c)
            bd = self.m(b, d)
            abcd = self.m(a+b, c+d)
            adbc = abcd-ac-bd
            r = int(ac+'0'*(2*n))+int(adbc+'0'*n)+bd
            return (str(r))

n1, n2 = '12','13'
test=Solution()
print(test.m(n1, n2))

import java.util.*;
class armstrong
{
public static void main(String args[])
{
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
int t = n;
while(t>0)
{
int d = t%10;
sum = sum+d*d*d;
t = t/10;
}
if(sum==n)
{
System.out.println("yes");
}
else
{
System.out.println("No");
}
}
}

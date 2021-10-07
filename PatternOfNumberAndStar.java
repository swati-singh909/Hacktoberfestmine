/*
 * for n = 5
 * INVALID NUMBER
 * 
 * for n = 6
 * 1*2*5*6
 *   3*4
 * 
 * for n = 20
 * 1*2*3*4*17*18*19*20
 *   5*6*7*14*15*16
 *     8*9*12*13
 *      10*11
 *      
 * for n = 30
 * 1*2*3*4*5*26*27*28*29*30
 *   6*7*8*9*22*23*24*25
 *     10*11*12*19*20*21
 *        13*14*17*18
 *           15*16
 */

import java.io.*;
class PatternOfNumberAndStar
{
    public static void main(String args[])throws IOException
    {
        int n=0;
        BufferedReader brd = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter a Number : ");
        try
        {
            n=Integer.parseInt(brd.readLine());
        }
        catch(NumberFormatException e)
        {
            System.err.println("Enter numeric data!!");
        }
        if((int)Math.sqrt(4*n+1)*(int)Math.sqrt(4*n+1)==(4*n+1))
        {
            int l=((int)Math.sqrt(4*n+1)-1)/2;
            int k=1;
            for(int i=0;i<l;i++)
            {
                for(int j=0;j<i;j++)
                    System.out.print("  ");
                
                for(int j=0;j<l-i;j++)
                    System.out.print(k++ +"*");
                    
                for(int j=0;j<l-i;j++)
                {
                    System.out.print(n-k+2+j);
                    if(j!=l-i-1)
                        System.out.print("*");
                }
                System.out.println("");
            }
        }
        else
            System.out.println("INVALID NUMBER");
    }
}
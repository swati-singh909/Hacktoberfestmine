import java.util.*;
public class Frequency {

    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        System.out.println("Enter String");
        String str = sc.nextLine();
        System.out.println("Enter Character to be searched");
        char ch = sc.next().charAt(0);
        int frequency = 0;

        for(int i = 0; i < str.length(); i++) {
            if(ch == str.charAt(i)) {
                ++frequency;
            }
        }

        System.out.println("Frequency of " + ch + " = " + frequency);
    }
}
import java.util.Scanner;
public class sol{
    public static boolean ispalin(int n){
        int rev=0;
        int t=n;
        while(n>0){
            int r=n%10;
            rev=rev*10+r;
            n=n/10;
        }
        if(rev==t){
            return true;
        }
       return false; 
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        if(ispalin(n)){
            System.out.println("Palindrome");
        }else{
            System.out.println("Not Palindrome");
        }
    }
}
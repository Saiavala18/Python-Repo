import java.util.Scanner;
public class sol{
    public static void main(String []args){
        Scanner sc=new Scanner(System.in);
        int c=0;
        String str=sc.nextLine();
        String words[]=str.trim().split("\\s+");
        c=words.length;
        System.out.println(c);
    }
}
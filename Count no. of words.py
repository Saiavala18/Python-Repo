import java.util.Scanner;
public class sol{
    public static void main(String []args){
        int c=0;
        Scanner sc=new Scanner(System.in);
        String str=sc.nextLine();
        String word[]=str.trim().split("\\s+");
        c=word.length;
        System.out.println(c);

    }
}
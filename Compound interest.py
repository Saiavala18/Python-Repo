import java.util.Scanner;
public class sol{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int p=sc.nextInt();
        int r=sc.nextInt();
        int t=sc.nextInt();
        double c=(p*(Math.pow((1+r/100.0),t)));
        System.out.printf("%.2f",c);
    }
}
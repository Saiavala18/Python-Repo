import java.util.Scanner;
public class sol{
    public static boolean isexpressed(int n){
        for(int i=0;i*i<=n;i++){
            int sq1=i*i;
            int rem=n-sq1;
            if(rem>=0){
                int sq2=(int)Math.sqrt(rem);
            if(sq2*sq2==rem && sq2!=i){
                return true;
            }
            }
        }
        return false;
    }
    public static void main(String[] args){
        Scanner sc= new Scanner(System.in);
        int n=sc.nextInt();
        if(isexpressed(n)){
            System.out.println("True");
        }else
        System.out.println("False");
    }
}
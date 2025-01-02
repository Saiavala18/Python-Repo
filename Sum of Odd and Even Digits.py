import java.util.Scanner;
public class sol{
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int s=0,sum=0;
        int n=sc.nextInt();
        int []arr=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
            if(i%2==0){
                s+=arr[i];
            }else{
                sum+=arr[i];
            }
        }
        if(s==sum)
        System.out.println("YES");
        else
        System.out.println("NO");
    }
}
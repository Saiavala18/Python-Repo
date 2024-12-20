import java.util.Scanner;
public class sol{
public static void readArray(int arr[],int i,Scanner sc){
    if(i==arr.length){
        return;
    }else{
        arr[i]=sc.nextInt();
        readArray(arr,i+1,sc);
    }
   
}
public static int sumArray(int arr[],int i){
    if(i==arr.length){
        return 0;
    }else{
        return arr[i]+sumArray(arr,i+1);
    }
}
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int []arr=new int[n];
        readArray(arr,0,sc);
        int sum=sumArray(arr,0);
        System.out.println(sum);
    }
}

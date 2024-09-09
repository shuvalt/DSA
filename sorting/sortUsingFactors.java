// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.*;
class HelloWorld {
    public static void main(String[] args) {
        int[] nums = {6,9,8,3,25,24};
        int[][] record = new int[nums.length][2];
        int i = 0;
        for(int num:nums){
            noOfFactors(num,record,i);
            i++;
        }
        Comparator<int[]> com = new Comparator<int[]>(){
            public int compare(int[] a,int[] b){
                if(a[1]<b[1]){
                    return 1;
                }else{
                    return -1;
                }
            }  
        };
        Arrays.sort(record,com);
        for(int[] arr:record){
            System.out.print(arr[0]+" ");
        }
        
     }
    public static void noOfFactors(int n,int[][] record,int j){
        int factors = 0;
        for(int i=1;i<=Math.sqrt(n);i++){
            if(n%i==0){
                factors++;
                if(i!=n/i){
                    factors++;
                }
            }
        }
        record[j][0]=n;
        record[j][1]=factors;
    }
}

import java.util.*;
class HelloWorld {
    public static void main(String[] args) {
        int[] arr = {10,36,54,89,12};
        int[][] result = new int[arr.length][2];
        int i = 0;
        for(int num:arr){
            int weight=0;
            if(isPerfect(num)){
                weight+=5;
            }
            if(num%4==0&&num%6==0){
                weight+=4;
            }
            if(num%2==0){
                weight+=3;
            }
            result[i][0]=num;
            result[i][1]=weight;
            i++;
        }
        Arrays.sort(result,new Comparator<int[]>(){
            public int compare(int[] a,int[] b){
                if(a[1]>b[1]){
                    return 1;
                }else{
                    return -1;
                }
            }
        });
        for(int[] arr1:result){
            for(int num:arr1){
                System.out.print(num+" ");
            }
            System.out.println();
        }
    }
    public static boolean isPerfect(int num){
        if(num==1 || num==0){
            return true;
        }
        int start = 1;
        int end = num;
        while(start<end){
            int mid = start + (end-start)/2;
            if(mid*mid==num){
                return true;
            }else if(mid*mid<num){
                start = mid+1;
            }else{
                end = mid-1;
            }
        }
        return false;
    }
}

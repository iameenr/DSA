

public class NKLadder {
    public static void main(String[] args){
        int N = 7;
        int K = 3;
        int[] stepsFor = new int[N+1];
        

        stepsFor = NKLadderBU(N, K, stepsFor);
        for(int steps: stepsFor) 
            System.out.print((steps)+" ");
        System.out.println("\n"+stepsFor[N]);

        stepsFor = NKLadderBUOpt(N, K, stepsFor);
        for(int steps: stepsFor) 
            System.out.print((steps)+" ");
        System.out.println("\n"+stepsFor[N]);      
    }

    static int[] NKLadderBU(int N, int K,int[] stepsFor) {
        stepsFor[0] = 1;
        for (int steps= 1; steps<= N; steps++) 
            for (int jump= 1; jump<= K; jump++) 
                if(steps-jump>= 0)
                    stepsFor[steps] += stepsFor[steps-jump];

        return stepsFor;
    }

    static int[] NKLadderBUOpt(int N, int K, int[] stepsFor){
        stepsFor[0] = 1;
        stepsFor[1] = 1;
        for (int steps= 2; steps<= K; steps++) 
            stepsFor[steps] = 2*stepsFor[steps-1];
        
        for (int steps= K+1; steps<= N; steps++) 
            stepsFor[steps] = (2*stepsFor[steps-1]) - stepsFor[steps-K-1];
        
        return stepsFor;     
    }
}

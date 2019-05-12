package seeds;

import java.util.*;
import java.io.*;
/**
 * author Nicholas and Luciano
 */
public class Seeds {

  
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        int tamanho = scanner.nextInt();
        int gotas   = scanner.nextInt();
        int maxDistP = 0;
        int maxDistCF = 0;
        boolean[] papel = new boolean[tamanho];
        for(int i=0; i<gotas;i++){
            int pos = scanner.nextInt();
            papel[pos] = true;
            
            
        }
        
        
        if(maxDistP > maxDistCF)
            System.out.println(maxDistP);
        else
            System.out.println(maxDistCF);
        
    }
    
}

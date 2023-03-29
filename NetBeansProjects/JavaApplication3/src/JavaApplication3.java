
import java.util.Scanner;

public class JavaApplication3 {
    public static void main(String[] args) {
      Scanner entrada= new Scanner(System.in);
            int n, f;
        n=0;
        f=1;
      System.out.print("digite el numero que quiera: ");
      n= entrada.nextInt();
            for(int i=2; i<=n; i++){
        f*=i;
    }
      System.out.print("El factorial de "+n);
      System.out.print(" es: "+f);
    }
    
}

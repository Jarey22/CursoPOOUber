import java.util.Scanner;

public class bfh {
        public static void main(String [] args){
            Scanner entrada= new Scanner(System.in);
            int n, f;
            n=0x0;
            f=1;
            System.out.print("Digite el valor de la ");
            n= entrada.nextInt();
            for(int i=2; i<=n; i++){
                f*=i;
            }
            System.out.print("el factorial de "+n);
            System.out.print("es:"+f);
        }
}

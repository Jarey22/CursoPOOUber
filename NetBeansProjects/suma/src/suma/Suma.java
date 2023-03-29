package suma;
import java.util.Scanner;
public class Suma {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n1, n2, n3;
        System.out.println("Introduzca el primer numero");
        n1 = sc.nextInt();
        System.out.println("Introduzca el segundo numero");
        n2 = sc.nextInt();
        System.out.println("Introduzca el tercer numero");
        n3 = sc.nextInt();
        if(n1>n2){
            if(n1>n3) {
                System.out.println("El mayor es: " + n1);    
            } else{
                System.out.println("El mayor es: " + n3);
            } if (n2>n3){
                System.out.println("El mayor es: " + n2);
            } else{
                System.out.println("El mayor es: " + n3);
            }
        }
    }
    
}

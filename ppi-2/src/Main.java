import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner t = new Scanner(System.in);
		System.out.println("Digite um nome: ");
		
		String str = t.next();
		
		StringBuffer strBuffer = new StringBuffer(str);
		
		StringBuffer inverso = strBuffer.reverse();
		System.out.println(inverso);
	}

}

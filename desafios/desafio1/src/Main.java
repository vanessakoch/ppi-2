import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner t = new Scanner(System.in);

		System.out.println("Digite uma frase para inverte-la: ");

		String str = t.nextLine();

		// inverteString1(str);
		inverteString2(str);

		t.close();
	}

	public static void inverteString1(String str) {
		StringBuffer strBuffer = new StringBuffer(str);
		StringBuffer inverso = strBuffer.reverse();
		System.out.println(inverso);
	}

	public static void inverteString2(String str) {
		int tamanho = str.length();

		char[] temp = new char[tamanho];
		char[] character = new char[tamanho];

		for (int i = 0; i < tamanho; i++) {
			temp[i] = str.charAt(i);
		}

		for (int j = 0; j < tamanho; j++) {
			character[j] = temp[tamanho - 1 - j];
		}

		String inverso = new String(character);
		System.out.println(inverso);
	}

}

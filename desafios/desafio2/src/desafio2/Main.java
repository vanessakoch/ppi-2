package desafio2;

public class Main {

	public static void main(String[] args) {
		int x = 0;
		int y = 2;
//		int temp = x;
//		x = y;
//		y = temp;
		
		x = reverse(y, y = x);
		System.out.println("X = " + x);
		System.out.println("Y = " + y);
	}
	
	public static int reverse(int x, int y) {
		return x;
	}
	
}

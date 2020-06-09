package Inc;

public class DuckNumber {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Integer number[]={302,450,022,333};
		
		for (int i = 0; i < number.length; i++) {
			if(number[i]/findDiviser(number[i]) != 0){
				if(number[i].toString().contains("0")){
					System.out.println(number[i]);
				}
			}
		}
	}
	private static int findDiviser(long base) {
		int result = 0;
		for (int i = 10; i > 9; i *= 10) {
			if ((base / i) == 0) {
				result = i;
				break;
			}
		}
		return result/10;
	}

}

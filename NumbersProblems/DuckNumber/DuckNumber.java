package Inc;

public class DuckNumber {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Integer number[]={302,450,022,333};
		
		for (int i = 0; i < number.length; i++) {
				if(! number[i].toString().startsWith("0") && number[i].toString().contains("0")){
					System.out.println(number[i]);
			}
		}
	}

}

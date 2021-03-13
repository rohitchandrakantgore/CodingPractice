package Inc;

public class CaptilOvel {

	public static void main(String[] args) {
		String input="Mininatoueh",vovel="aeiou";
		String result="";
		for (int i = 0; i < input.length(); i++) {
			Character c=input.charAt(i);
			if(vovel.contains(c.toString())){
				c=Character.toUpperCase(c);
			}
			result+=c;
		}
		System.out.println(result);
	}

}

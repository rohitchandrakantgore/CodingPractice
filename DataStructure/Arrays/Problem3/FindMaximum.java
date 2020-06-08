package Inc;

import java.util.ArrayList;
import java.util.Map;
import java.util.SortedMap;
import java.util.TreeMap;

public class FindMaximum {

	public static void main(String[] args) {
		int[] inputArray = { 2, 5, 3, 30, 34, 5, 9, 4, 54, 546, 548, 60 };
		int totalcases = inputArray[0];
		int starter = 2, arraysize = inputArray[1];
		int arraylimit;
		for (int i = 0; i < totalcases; i++) {
			arraylimit = starter + arraysize;
			long first = inputArray[starter];
			ArrayList<Long> pointer = new ArrayList<Long>();
			int second=starter+1; 
			Long[] max; // first position max number
						// second diviser
			for (int j = starter; j < arraylimit-1; j++, second++) {
				max = formLargeNumber(pointer, first, inputArray[second]);
				first=max[0];
				pointer.add(max[1]);
			}

			if (arraylimit < inputArray.length - 1) {
				arraysize = inputArray[arraylimit];
				starter = arraylimit + 1;
			}
			System.out.println(first);
		}
		System.out.println();

	}

	private static Long[] formLargeNumber(ArrayList<Long> pointer, long first, int second) {
		long number;
		Long[] array = new Long[2];
		long diviser = 0;
		SortedMap<Long, Long> numbers = 
                 new TreeMap<Long, Long>().descendingMap();
		// add at start
		diviser = findDiviser(first);
		number = second * diviser + first;
		numbers.put(number, diviser);
		// add add end
		diviser = findDiviser(second);
		number = first * diviser + second;
		numbers.put(number, diviser);
		if (pointer != null) {
			for (Long d : pointer) {
				long first_1 , second_1,second_2,diviser_2;	
				first_1=first / d;
				second_2= first % d;
 				diviser_2=findDiviser(second)*d;
 				second_1=(int) (second*d);
				first_1=first_1*diviser_2;	
				number= second_1 + second_2 + first_1;
				
				numbers.put((long) number, diviser_2);
			}

		}
		
		//System.out.println(numbers);
		
		Map.Entry<Long, Long> firstentry=numbers.entrySet().iterator().next();
		array[0]=firstentry.getKey();
		array[1]=firstentry.getValue();
		return array;
	}

	private static int findDiviser(long base) {
		int result = 0;
		for (int i = 10; i > 9; i *= 10) {
			if ((base / i) == 0) {
				result = i;
				break;
			}
		}
		return result;
	}
}

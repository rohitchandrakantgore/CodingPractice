package Inc;

public class Pyramid1 {

	public static void main(String[] args) {
		// take row
		int row = 7;
		// find column
		int column = 2 * row - 1;
		// find mid
		int mid = (column / 2);
		int left = mid - 1, right = mid + 1;
		// iterate till row#3
		for (int i = 0; i < row; i++) {
			// iterate over column
			// left=mid-1, right=mid+1
			boolean section=true;
			for (int j = 0; j < column; j++) {
				if (j > left && j < right && section) {
					System.out.print("*");
					section=false;
				}else {
					section=true;
					System.out.print(" ");
				}
			}
			left--;
			right++;
			System.out.println();
		}
	}

}

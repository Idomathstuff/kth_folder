// Java program to compute GCD of
// two numbers using general
// approach
import java.util.Scanner;

class lab1 {

	static int L (String S){
		int max_length = 0;
		int i = 0;
		while (i<S.length()){
			String obs_str = String.valueOf(S.charAt(i));
			for (int y = i+1; y < S.length(); y++){
				if (S.charAt(y-1) <= S.charAt(y)){
					obs_str += S.charAt(y);
				}else{
					break;
				}
			}
			int obs_length = obs_str.length();
			i+=obs_length;
			if (obs_length>max_length){
				max_length = obs_length;
			}
		}	
		return max_length;

	}
	public static void main(String[] args)
	{
		String in_str;
		while (true){
			Scanner in = new Scanner(System.in);
			in_str = in.nextLine();
			if (in_str != ""){
				System.out.println(L(in_str));
				}
			else{
				// in.close();
				break;}
		}
		// in = new Scanner(System.in);
		// System.out.println(L(in.nextLine()));
		// String tmp_str = "123abcABCDabcc1234";
		// System.out.println(L(tmp_str));
	}
}	

class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();
        for(String i : strs) {
            encoded.append(i.length());
            encoded.append("#");
            encoded.append(i);
        }
        return encoded.toString();
    }

    public List<String> decode(String str) {
        String prefix = "";
        List<String> strs = new ArrayList<>();
        int i = 0;
        while(i<str.length()) {
            if ('#'== str.charAt(i)) {
                int counter = Integer.parseInt(prefix);
                strs.add(str.substring(i + 1, i + 1 + counter));
                i += counter+1;
                prefix = "";
            }
            else {
                prefix +=str.charAt(i);
                i++;
            }
        }
        return strs;
    }
}

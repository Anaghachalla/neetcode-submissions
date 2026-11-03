class Solution {

    public String encode(List<String> strs) {
        List<String> encodeArr = new ArrayList<>();
        for(String i : strs) {
            encodeArr.add(String.valueOf(i.length()));
            encodeArr.add("#");
            encodeArr.add(i);
        }
        return String.join("", encodeArr);
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

class Solution {
    public String[] findOcurrences(String text, String first, String second) {
        String[] words = text.split(" ");
        ArrayList<String> result = new ArrayList<String>();
    
        
        int prev, oneBeforePrev;
        for (int i = 2; i < words.length; i++) {
            prev = i-1;
            oneBeforePrev = i-2;
            if(first.equals(words[oneBeforePrev]) && second.equals(words[prev])) {
                result.add(words[i]);
            } 
        }
        return result.toArray(new String[0]);
    }
}
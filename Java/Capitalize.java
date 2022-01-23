class Solution {
    public String capitalizeTitle(String title) {
        String.toLowerCase(title);
        String res = "";

        String[] words = new String[];
        words = title.split(" ");

        for(String i : words){
            if(i.length() <= 2)
                 res.append(i+" ");
            else 
                res.append(i.substring(0,1).toUpperCase() + i.substring(1));
        }

        return res;
    }
}
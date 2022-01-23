import java.util.ArrayList;

class CombinationIterator {
    
    private String characters;
    private int combinationLength;
    private ArrayList<Integer> list;
    int lengthOfCharacters;


    public CombinationIterator(String characters, int combinationLength) {
        this.characters = characters;
        this.combinationLength = combinationLength;    
        list = new ArrayList<Integer>(combinationLength);
        lengthOfCharacters = characters.length();
    }
    
    public String next() {
        
    }
    
    public boolean hasNext() {
        int maxFirstIndex = ((lengthOfCharacters -1)-combinationLength);
        for (int i = 1; i < list.size(); i++) {
            if (list.get(i) == maxFirstIndex + i) {continue;}
            else return true;
        
        return false;
    }
}
}


/**
 * Your CombinationIterator object will be instantiated and called as such:
 * CombinationIterator obj = new CombinationIterator(characters, combinationLength);
 * String param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */




 //     if(list.get(i) == (maxFirstIndex + i)) 
        //         flag = false;
        // }
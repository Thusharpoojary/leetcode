class Solution {
    public String frequencySort(String s) {
        HashMap<Character,Integer> map=new HashMap<>();

        for(int i=0;i<s.length();i++){
            char c= s.charAt(i);
            map.put(c,map.getOrDefault(c,0)+1);

        }
        PriorityQueue<Character> heap=new PriorityQueue<>(
            (a,b)->map.get(b)-map.get(a)
        );

        for(char c:map.keySet()){
            heap.offer(c);
        }
        StringBuilder str=new StringBuilder();
        while(heap.size()!=0){
            char c=heap.poll();
            for(int i=0;i<map.get(c);i++){
                str.append(c);
            }

        }

        return str.toString();
    }
}
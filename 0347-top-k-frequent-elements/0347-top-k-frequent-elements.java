class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        HashMap<Integer,Integer> map=new HashMap<>();

        for(int n:nums){
            map.put(n,map.getOrDefault(n,0)+1);
        }

        PriorityQueue<Integer> q=new PriorityQueue<>(
            (a,b)->map.get(a)-map.get(b)
        );

        for(int i:map.keySet()){
            q.offer(i);
            if(q.size()>k){
                q.poll();
            }
        }
        int[] arr=new int[k];
        for(int i=0;i<k;i++){
            arr[i]=q.poll();
        }
        return arr;
    }
}
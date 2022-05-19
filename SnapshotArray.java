import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

class SnapshotArray {
    private List<Map<Integer, Integer>> db;
    int snapId;

    public SnapshotArray(int length) {
        db = new ArrayList<>();
    }
    
    public void set(int index, int val) {
        if (db.size() == snapId) {
            db.add(new HashMap<>());
        }
        db.get(snapId).put(index, val);
    }
    
    public int snap() {
        if (db.size() == snapId) {
            db.add(new HashMap<>());
        }
        
        return snapId++;
    }
    
    public int get(int index, int snap_id) {
        Integer result = null;
        for (int i = snap_id; i >= 0; --i) {
            result = db.get(i).get(index);
            if (result != null) {
                return result;
            }
        }
        
        return 0;
    }
}

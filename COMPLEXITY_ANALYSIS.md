# **COMPLEXITY_ANALYSIS.md**

# PlayWise Music Engine - Space-Time Complexity Analysis

**Problem 6: Playback Optimization using Space-Time Analysis**

This document provides a comprehensive analysis of time and space complexity for all core methods across the PlayWise system (Problems 1-5), along with optimization recommendations.

---

## **Table of Contents**
1. [Problem 1: Playlist Engine](#problem-1-playlist-engine)
2. [Problem 2: Playback History](#problem-2-playback-history)
3. [Problem 3: Song Rating Tree](#problem-3-song-rating-tree)
4. [Problem 4: Song Lookup Map](#problem-4-song-lookup-map)
5. [Problem 5: Time-based Sorting](#problem-5-time-based-sorting)
6. [System-wide Summary](#system-wide-summary)
7. [Optimization Recommendations](#optimization-recommendations)

***

## **Problem 1: Playlist Engine**

### **DoublyLinkedList Class**

| Method | Time Complexity | Space Complexity | Explanation |
|--------|----------------|------------------|-------------|
| `add_song(song)` | **O(1)** | **O(1)** | Append to tail using tail pointer; constant pointer manipulation |
| `delete_song(index)` | **O(n)** | **O(1)** | Must traverse to index position (n/2 on average), then unlink node |
| `move_song(from_idx, to_idx)` | **O(n)** | **O(1)** | Traverse to both positions, extract and reinsert node |
| `reverse_playlist()` | **O(n)** | **O(1)** | Iterate through all nodes, swap prev/next pointers |
| `get_all_songs()` | **O(n)** | **O(n)** | Traverse entire list, create new list of songs |

**Analysis:**
- **Strengths:** O(1) insertion at head/tail makes adding songs very efficient
- **Bottlenecks:** Index-based operations require traversal (no random access)
- **Memory:** In-place operations minimize extra space usage

### **Playlist Class**

| Method | Time Complexity | Space Complexity | Explanation |
|--------|----------------|------------------|-------------|
| `add_song(title, artist, duration)` | **O(1)** | **O(1)** | Creates Song object, delegates to DoublyLinkedList |
| `delete_song(index)` | **O(n)** | **O(1)** | Delegates to DoublyLinkedList.delete_song() |
| `move_song(from_idx, to_idx)` | **O(n)** | **O(1)** | Delegates to DoublyLinkedList.move_song() |
| `reverse_playlist()` | **O(n)** | **O(1)** | Delegates to DoublyLinkedList.reverse_playlist() |
| `get_all_songs()` | **O(n)** | **O(n)** | Delegates to DoublyLinkedList.get_all_songs() |

---

## **Problem 2: Playback History**

### **PlaybackHistory Class**

| Method | Time Complexity | Space Complexity | Explanation |
|--------|----------------|------------------|-------------|
| `push(song)` | **O(1)** | **O(1)** | Python list append is amortized O(1) |
| `pop()` | **O(1)** | **O(1)** | Remove and return last element from list |
| `peek()` | **O(1)** | **O(1)** | Access last element without removal |
| `is_empty()` | **O(1)** | **O(1)** | Check if length is zero |

**Analysis:**
- **Optimal:** All stack operations run in constant time
- **Memory:** Stack grows linearly with playback history; consider maximum size limit for production

### **PlaybackController Class**

| Method | Time Complexity | Space Complexity | Explanation |
|--------|----------------|------------------|-------------|
| `play_song(title, artist, duration)` | **O(1)** | **O(1)** | Add to playlist (O(1)) + push to stack (O(1)) |
| `undo_last_play()` | **O(1)** | **O(1)** | Pop from stack (O(1)) |
| `get_playlist_songs()` | **O(n)** | **O(n)** | Delegates to playlist.get_all_songs() |

***

## **Problem 3: Song Rating Tree**

### **RatingBucket Class**

| Method | Time Complexity | Space Complexity | Explanation |
|--------|----------------|------------------|-------------|
| `add_song(song)` | **O(1)** | **O(1)** | Append song to internal list |
| `remove_song(song_id)` | **O(m)** | **O(1)** | Linear search through m songs in bucket, then remove |
| `get_songs()` | **O(m)** | **O(m)** | Return copy of all m songs in bucket |

*where m = number of songs in this rating bucket*

### **BSTNode Class**
- No operations; just data structure

### **RatingBST Class**

| Method | Time Complexity | Space Complexity | Explanation |
|--------|----------------|------------------|-------------|
| `insert_song(song, rating)` | **O(log n)** avg<br>**O(n)** worst | **O(log n)** recursion | Binary search to find rating node, insert if not exists |
| `search_by_rating(rating)` | **O(log n)** avg<br>**O(n)** worst | **O(log n)** recursion | Binary search traversal to rating node |
| `delete_song(song_id)` | **O(n·m)** | **O(log n)** recursion | Must search all nodes (n) and within buckets (m) |

*where n = number of rating nodes, m = avg songs per rating*

**Analysis:**
- **Best Case:** Balanced tree with O(log n) search/insert
- **Worst Case:** Unbalanced tree degenerates to O(n) (linked list behavior)
- **Optimization Needed:** Consider self-balancing BST (AVL, Red-Black) for guaranteed O(log n)

### **SongRatingEngine Class**
- Delegates to RatingBST; same complexities

***

## **Problem 4: Song Lookup Map**

### **SongLookupMap Class**

| Method | Time Complexity | Space Complexity | Explanation |
|--------|----------------|------------------|-------------|
| `add_song(song)` | **O(1)** avg<br>**O(n)** worst | **O(1)** | Dictionary insertion; worst case with hash collisions |
| `remove_song(song_id)` | **O(1)** avg<br>**O(n)** worst | **O(1)** | Dictionary deletion from both maps |
| `lookup_song_by_id(song_id)` | **O(1)** avg<br>**O(n)** worst | **O(1)** | Dictionary key lookup |
| `lookup_song_by_title(title)` | **O(1)** avg<br>**O(n)** worst | **O(1)** | Dictionary key lookup |

**Analysis:**
- **Optimal Performance:** Python's dict uses efficient hashing with O(1) average
- **Collision Handling:** Python handles collisions internally; worst case rarely occurs
- **Memory Trade-off:** Maintains two dictionaries for dual-key access (2× space)
- **Scalability:** Excellent for large datasets; ideal for instant search

---

## **Problem 5: Time-based Sorting**

### **SortCriteria Class**
- Enum/constants; no operations

### **SortEngine Class**

| Method | Time Complexity | Space Complexity | Explanation |
|--------|----------------|------------------|-------------|
| `merge_sort(songs, criteria)` | **O(n log n)** | **O(n)** | Divide-and-conquer; creates temporary sublists |
| `_merge(left, right, criteria)` | **O(n)** | **O(n)** | Merge two sorted lists into one |
| `_compare(song_a, song_b, criteria)` | **O(1)** | **O(1)** | Simple attribute comparison |

**Analysis:**
- **Consistent Performance:** O(n log n) in all cases (best, average, worst)
- **Stability:** Merge sort preserves relative order of equal elements
- **Memory Cost:** Requires O(n) auxiliary space for merging
- **Alternative:** Could use in-place quicksort for O(log n) space, but loses stability

***

## **System-wide Summary**

### **Overall Operation Complexity Table**

| Operation | Data Structure | Time (Best) | Time (Avg) | Time (Worst) | Space |
|-----------|---------------|-------------|------------|--------------|-------|
| Add song | DoublyLinkedList | O(1) | O(1) | O(1) | O(1) |
| Delete by index | DoublyLinkedList | O(1) | O(n) | O(n) | O(1) |
| Move song | DoublyLinkedList | O(n) | O(n) | O(n) | O(1) |
| Reverse playlist | DoublyLinkedList | O(n) | O(n) | O(n) | O(1) |
| Playback undo | Stack | O(1) | O(1) | O(1) | O(1) |
| Insert by rating | BST | O(log n) | O(log n) | O(n) | O(log n) |
| Search by rating | BST | O(log n) | O(log n) | O(n) | O(log n) |
| Lookup by ID/title | HashMap | O(1) | O(1) | O(n) | O(1) |
| Sort playlist | Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |

***

## **Optimization Recommendations**

### **1. Lazy Reversal (DoublyLinkedList)**
**Current:** O(n) — physically swap all prev/next pointers  
**Optimized:** O(1) — toggle boolean flag, adjust traversal direction  

**Implementation:**
```python
# Maintain a reversed flag
self.is_reversed = False

def reverse_playlist(self):
    # Just flip the flag instead of physically reversing
    self.is_reversed = not self.is_reversed
    # Swap head and tail conceptually
    self.head, self.tail = self.tail, self.head
```

**Benefits:** 
- Instant reversal regardless of playlist size
- Traversal methods respect the flag

***

### **2. Size Caching (DoublyLinkedList)**
**Current:** O(n) — traverse entire list to count  
**Optimized:** O(1) — maintain size counter  

**Implementation:**
```python
self._size = 0

def add_song(self, song):
    # ... add logic ...
    self._size += 1

def delete_song(self, index):
    # ... delete logic ...
    self._size -= 1

def size(self):
    return self._size  # O(1) instead of O(n)
```

***

### **3. Balanced BST (RatingBST)**
**Current:** O(n) worst case for unbalanced tree  
**Optimized:** O(log n) guaranteed with AVL or Red-Black tree  

**Recommendation:**
- Implement self-balancing after insertions/deletions
- Or use library: `sortedcontainers.SortedDict` for production

***

### **4. Index Optimization (DoublyLinkedList)**
**Current:** O(n) for index-based access  
**Consideration:** 
- If frequent random access needed, consider hybrid: list of nodes
- Trade-off: More memory for O(1) index access

---

### **5. History Size Limit (PlaybackHistory)**
**Current:** Unlimited stack growth  
**Optimized:** Cap at maximum history size (e.g., 100 songs)  

**Implementation:**
```python
MAX_HISTORY = 100

def push(self, song):
    if len(self.history_stack) >= MAX_HISTORY:
        self.history_stack.pop(0)  # Remove oldest
    self.history_stack.append(song)
```

***

## **Key Takeaways**

1. **Know Your Data Structures:** Each has trade-offs between time and space
2. **Analyze Before Optimizing:** Profile to find actual bottlenecks
3. **Document Complexity:** Makes maintenance and scaling decisions clear
4. **Consider Use Cases:** Optimize for common operations, not edge cases
5. **Space-Time Trade-offs:** Sometimes using more memory saves time (and vice versa)

***

## **Conclusion**

This analysis demonstrates that the PlayWise system uses appropriate data structures for each problem:
- **O(1) operations** where speed is critical (add, undo, lookup)
- **O(log n) search** with BST for rating organization
- **O(n log n) sorting** with stable merge sort

Future optimizations should focus on:
- Lazy evaluation techniques
- Self-balancing trees
- Caching frequently accessed data
- Memory limits for unbounded growth

**Engineering Mindset:** Always annotate complexity, measure performance, and optimize intelligently based on real-world usage patterns.

---

**Prepared by:** SALA ANIL KUMAR  


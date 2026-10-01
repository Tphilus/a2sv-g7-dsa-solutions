<h2><a href="https://codeforces.com/contest/4/problem/A">Watermelon</a></h2>

**Language:** Python 3 &nbsp;&nbsp;|&nbsp;&nbsp; **Difficulty:** Easy (rating 800) &nbsp;&nbsp;|&nbsp;&nbsp; **Platform:** Codeforces &nbsp;&nbsp;|&nbsp;&nbsp; **Submitted:** October 1, 2026 at 8:11 PM

---

### 📝 Problem Statement

<div>
<p>One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed <span class="tex-span"><i>w</i></span> kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.</p><p>Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.</p>
</div>

---

### 💡 Solution

```python
w = int(input())

if w % 2 == 0 and w > 2:
    print("YES")
else:
    print("NO")
```

---

### 📊 Complexity

- **Time:** O(1)
- **Space:** O(1)

> _Estimated from a static scan of loop nesting and allocation patterns, not true algorithmic analysis._
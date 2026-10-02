<h2><a href="https://codeforces.com/contest/723/problem/A">The New Year: Meeting Friends</a></h2>

**Language:** PyPy 3-64 &nbsp;&nbsp;|&nbsp;&nbsp; **Difficulty:** Easy (rating 800) &nbsp;&nbsp;|&nbsp;&nbsp; **Platform:** Codeforces &nbsp;&nbsp;|&nbsp;&nbsp; **Submitted:** October 2, 2026 at 11:07 AM

---

### 📝 Problem Statement

<div>
<div><p>There are three friend living on the straight line <span class="tex-span"><i>Ox</i></span> in Lineland. The first friend lives at the point <span class="tex-span"><i>x</i><sub class="lower-index">1</sub></span>, the second friend lives at the point <span class="tex-span"><i>x</i><sub class="lower-index">2</sub></span>, and the third friend lives at the point <span class="tex-span"><i>x</i><sub class="lower-index">3</sub></span>. They plan to celebrate the New Year together, so they need to meet at one point. What is the minimum total distance they have to travel in order to meet at some point and celebrate the New Year?</p><p>It's guaranteed that the optimal answer is always integer.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of the input contains three <span class="tex-font-style-bf">distinct</span> integers <span class="tex-span"><i>x</i><sub class="lower-index">1</sub></span>, <span class="tex-span"><i>x</i><sub class="lower-index">2</sub></span> and <span class="tex-span"><i>x</i><sub class="lower-index">3</sub></span> (<span class="tex-span">1 ≤ <i>x</i><sub class="lower-index">1</sub>, <i>x</i><sub class="lower-index">2</sub>, <i>x</i><sub class="lower-index">3</sub> ≤ 100</span>)&nbsp;— the coordinates of the houses of the first, the second and the third friends respectively. </p></div><div class="output-specification"><div class="section-title">Output</div><p>Print one integer&nbsp;— the minimum total distance the friends need to travel in order to meet together.</p></div><div class="sample-tests"><div class="section-title">Examples</div><div class="sample-test"><div class="input"><div class="title">Input</div><pre>7 1 4<br></pre></div><div class="output"><div class="title">Output</div><pre>6<br></pre></div><div class="input"><div class="title">Input</div><pre>30 20 10<br></pre></div><div class="output"><div class="title">Output</div><pre>20<br></pre></div></div></div><div class="note"><div class="section-title">Note</div><p>In the first sample, friends should meet at the point <span class="tex-span">4</span>. Thus, the first friend has to travel the distance of <span class="tex-span">3</span> (from the point <span class="tex-span">7</span> to the point <span class="tex-span">4</span>), the second friend also has to travel the distance of <span class="tex-span">3</span> (from the point <span class="tex-span">1</span> to the point <span class="tex-span">4</span>), while the third friend should not go anywhere because he lives at the point <span class="tex-span">4</span>.</p></div>
</div>

---

### 💡 Solution

```pypy364
# a,*b = map(int, input().split())
a,b, c = map(int, input().split())

mn = float("inf")
for point in range(1, 101):
    total_distance = abs(point - a) + abs(point - b) + abs(point - c)
    
    mn = min(mn, total_distance)

print(mn)
```

---

### 📊 Complexity

- **Time:** O(1)
- **Space:** O(1)

> _Estimated from a static scan of loop nesting and allocation patterns, not true algorithmic analysis._
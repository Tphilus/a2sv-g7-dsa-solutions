<h2><a href="https://codeforces.com/contest/1703/problem/A">YES or YES?</a></h2>

**Language:** PyPy 3-64 &nbsp;&nbsp;|&nbsp;&nbsp; **Difficulty:** Easy (rating 800) &nbsp;&nbsp;|&nbsp;&nbsp; **Platform:** Codeforces &nbsp;&nbsp;|&nbsp;&nbsp; **Submitted:** October 2, 2026 at 11:08 AM

---

### 📝 Problem Statement

<div>
<div><p>There is a string $$$s$$$ of length $$$3$$$, consisting of uppercase and lowercase English letters. Check if it is equal to "<span class="tex-font-style-tt">YES</span>" (without quotes), where each letter can be in any case. For example, "<span class="tex-font-style-tt">yES</span>", "<span class="tex-font-style-tt">Yes</span>", "<span class="tex-font-style-tt">yes</span>" are all allowable.</p></div><div class="input-specification"><div class="section-title">Input</div><p>The first line of the input contains an integer $$$t$$$ ($$$1 \leq t \leq 10^3$$$)&nbsp;— the number of testcases.</p><p>The description of each test consists of one line containing one string $$$s$$$ consisting of three characters. Each character of $$$s$$$ is either an uppercase or lowercase English letter.</p></div><div class="output-specification"><div class="section-title">Output</div><p>For each test case, output "<span class="tex-font-style-tt">YES</span>" (without quotes) if $$$s$$$ satisfies the condition, and "<span class="tex-font-style-tt">NO</span>" (without quotes) otherwise.</p><p>You can output "<span class="tex-font-style-tt">YES</span>" and "<span class="tex-font-style-tt">NO</span>" in any case (for example, strings "<span class="tex-font-style-tt">yES</span>", "<span class="tex-font-style-tt">yes</span>" and "<span class="tex-font-style-tt">Yes</span>" will be recognized as a positive response).</p></div><div class="sample-tests"><div class="section-title">Example</div><div class="sample-test"><div class="input"><div class="title">Input</div><pre><div class="test-example-line test-example-line-even test-example-line-0">10</div><div class="test-example-line test-example-line-odd test-example-line-1">YES</div><div class="test-example-line test-example-line-even test-example-line-2">yES</div><div class="test-example-line test-example-line-odd test-example-line-3">yes</div><div class="test-example-line test-example-line-even test-example-line-4">Yes</div><div class="test-example-line test-example-line-odd test-example-line-5">YeS</div><div class="test-example-line test-example-line-even test-example-line-6">Noo</div><div class="test-example-line test-example-line-odd test-example-line-7">orZ</div><div class="test-example-line test-example-line-even test-example-line-8">yEz</div><div class="test-example-line test-example-line-odd test-example-line-9">Yas</div><div class="test-example-line test-example-line-even test-example-line-10">XES</div></pre></div><div class="output"><div class="title">Output</div><pre>YES
YES
YES
YES
YES
NO
NO
NO
NO
NO
</pre></div></div></div><div class="note"><div class="section-title">Note</div><p>The first five test cases contain the strings "<span class="tex-font-style-tt">YES</span>", "<span class="tex-font-style-tt">yES</span>", "<span class="tex-font-style-tt">yes</span>", "<span class="tex-font-style-tt">Yes</span>", "<span class="tex-font-style-tt">YeS</span>". All of these are equal to "<span class="tex-font-style-tt">YES</span>", where each character is either uppercase or lowercase.</p></div>
</div>

---

### 💡 Solution

```pypy364
t = int(input())

dic_letters = {
    "YES", "yES", "Yes","yes","YeS", "YEs", "YeS" 
}

for _ in range(t):
    letters = input().lower()
    
    if letters in dic_letters:
        print("YES")
    else:
        print("NO")
```

---

### 📊 Complexity

- **Time:** O(1)
- **Space:** O(1)

> _Estimated from a static scan of loop nesting and allocation patterns, not true algorithmic analysis._
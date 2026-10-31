<div align="center">

# LeetCode Solutions

My accepted LeetCode solutions, pushed here automatically every time I solve a problem.

[![LeetCode](https://img.shields.io/badge/LeetCode-vigesh-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/vigesh/)
[![GitHub](https://img.shields.io/badge/GitHub-Vigesh--VS-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Vigesh-VS)

<a href="https://leetcode.com/u/vigesh/">
  <img src="https://leetcard.jacoblin.cool/vigesh?theme=dark&font=Inter&ext=heatmap" alt="LeetCode stats for vigesh" />
</a>

</div>

---

## About

Every solution in this repository passed all of LeetCode's test cases before it was committed. Nothing is copied in by hand: when a submission is **Accepted**, it is synced here by **LeetSync**, a Chrome extension I built for this.

- Only accepted submissions are pushed. Wrong answers, errors and "Run" attempts never are.
- If I resubmit a problem with improved code, the file is updated with an `Update:` commit.
- Resubmitting identical code creates no commit.

## Repository layout

Each problem gets its own folder, named by its LeetCode number and title:

```
0412-fizz-buzz/
├── README.md       # problem statement, difficulty and topics
└── solution.py     # my accepted solution
```

- Folder numbers are zero-padded (`0001` to `9999`) so they sort in order.
- If I solve a problem in more than one language, each one is saved as its own `solution.<ext>` file in the same folder.
- Commit messages record the result, for example:
  `Add: 412. Fizz Buzz (Python3) - Runtime 0 ms, Memory 19.5 MB`

## Finding a problem

- Browse the folders above, which are sorted by problem number.
- Press <kbd>T</kbd> on this page to search by name, for example `two-sum`.
- Each problem's own `README.md` links back to it on LeetCode.

## How LeetSync works

1. When I submit on leetcode.com, the extension waits for LeetCode's verdict.
2. If it is **Accepted**, it reads the code, language, runtime and memory, plus the problem statement.
3. It commits the solution and a problem README to this repository through the GitHub API.

LeetSync uses no third-party servers. It talks only to LeetCode (with my own session) and to `api.github.com`, using a token scoped to this one repository.

---

<div align="center">

If you're preparing for coding interviews too, feel free to look around. ⭐

</div>

## Progress

⬜ Lesson 1  
⬜ Lesson 2  
⬜ Lesson 3  

👉 Your progress is tracked in Pull Requests

# 🚀 How to Use This Repo

Welcome! This course is completed by submitting **Pull Requests (PRs)** and getting automated feedback.

---

## ⚠️ First-Time Setup (REQUIRED)

1. Go to the **Actions** tab in this repo
2. Click **“Enable workflows”**

👉 Without this, your code will NOT be tested.

---

## 🧠 How Lessons Work

Each lesson follows this flow:

1. Create a new branch for the lesson
2. Complete the code in the `lessons/` folder
3. Open a Pull Request
4. Wait for feedback from the bot

---

## 🧑‍💻 Step-by-Step

### 1. Clone your repo

```bash
git clone <your-repo-url>
cd <repo-name>
```

---

### 2. Create a lesson branch

```bash
git checkout -b lesson-1
```

👉 Branch names must follow this format:

```
lesson-1
lesson-2
lesson-3
```

---

### 3. Complete the lesson

* Open the file:

```
lessons/lesson1.py
```

* Follow the instructions in the file
* Write your solution

---

### 4. Test locally (recommended)

```bash
pip install pytest
pytest tests/test_lesson1.py
```

---

### 5. Commit and push

```bash
git add .
git commit -m "complete lesson 1"
git push origin lesson-1
```

---

### 6. Open a Pull Request

* Go to GitHub
* Open a PR from:

```
lesson-1 → main
```

---

## 🤖 What Happens Next

Once you open a PR:

* ✅ Your code is automatically tested
* 💬 You’ll get feedback as a comment
* 🏷️ A label is added if you pass

---

## ✅ Passing a Lesson

If your code is correct:

* You’ll see a message like:

```
✅ Lesson complete!
```

* Your PR will get a label:

```
lesson-1-complete
```

* You can move to the next lesson

---

## ❌ If You Fail

Don’t worry—that’s part of the process.

You’ll get hints like:

* “Check your return value”
* “Function name doesn’t match”

👉 Fix your code and **push again to the same branch**

---

## 🔓 Moving to the Next Lesson

After passing:

```bash
git checkout main
git pull
git checkout -b lesson-2
```

Then repeat the process.

---

## ⚠️ Important Rules

* Always use the correct branch name (`lesson-X`)
* Do NOT edit tests
* Do NOT skip lessons
* Keep working in the same PR until it passes

---

## 🧹 Cleaning Up (Optional)

After finishing a lesson:

```bash
git checkout main
git branch -d lesson-1
git push origin --delete lesson-1
```

---

## 🆘 Need Help?

* Read the PR feedback carefully
* Run tests locally
* Ask questions if you're stuck

---

## 🎯 Goal

By the end, you’ll complete all lessons and build real Python skills through hands-on practice.

Good luck 🚀

# Common Viva Questions

## Q: Is this project platform-dependent?

**A:**  
The project is **partially platform-dependent**.

---

### Explanation

- The **core logic** (CPU scheduling simulation, memory simulation) is written in standard C++
- This part is **platform-independent**
- The **system monitoring module** depends on the operating system

In this project:

- Linux-specific monitoring is implemented using the `/proc` filesystem
- OS-specific code is isolated using the `SystemMonitor` interface

---

### Design advantage

- Core logic can run on any OS
- Only a new system monitor implementation is required for another platform

---

### One-line viva answer

> “The core logic is platform-independent; only system monitoring is OS-specific.”

---

## Q: Why is Qt chosen for GUI?

**A:**  
Qt is chosen because it provides **cross-platform GUI support** and integrates naturally with C++.

---

### Explanation

Qt offers:

- Native C++ support
- Rich GUI widgets
- Signal–slot mechanism for event handling
- Cross-platform compatibility (Linux, Windows, macOS)

It allows the GUI to remain separate from system and core logic.

---

### Academic relevance

- Matches Computer Graphics and OOP concepts
- Widely used in industry
- Suitable for desktop-based academic projects

---

### One-line viva answer

> “Qt is chosen for its cross-platform support, C++ integration, and rich GUI features.”

---

## Q: Can this project run on Windows?

**A:**  
Yes, the project **can run on Windows** with a Windows-specific implementation of the system monitoring module.

---

### Explanation

- The current implementation uses Linux `/proc` files
- Windows does not provide `/proc`
- A Windows version would use Windows APIs for CPU and memory data

Because the project uses an abstract interface (`SystemMonitor`):

- The GUI and core logic remain unchanged
- Only the monitoring module needs replacement

---

### Design benefit

This demonstrates:

- Extensibility
- Good object-oriented design
- Platform abstraction

---

### One-line viva answer

> “Yes, by implementing a Windows-specific SystemMonitor without changing the core logic.”

---

## Q: Is this a real-time system?

**A:**  
No, this project is **not a real-time system**.

---

### Explanation

- A real-time system has strict timing constraints
- This project performs monitoring and simulation
- Delays do not cause system failure

The CPU scheduling shown is **educational simulation**, not kernel-level scheduling.

---

### Important distinction

- Monitoring ≠ controlling
- Simulation ≠ real-time execution

---

### One-line viva answer

> “No, it is a monitoring and simulation tool, not a real-time operating system.”

---

## Q: How is this project useful academically?

**A:**  
The project helps bridge the gap between **theoretical OS concepts and practical understanding**.

---

### Explanation

It allows students to:

- Visualize CPU scheduling algorithms
- Understand memory usage and fragmentation
- Observe real system statistics
- Connect theory with real system behavior

This improves conceptual clarity compared to textbook-only learning.

---

### Educational value

- Strong alignment with BCA syllabus
- Enhances OS, C++, and design understanding
- Encourages system-level thinking

---

### One-line viva answer

> “It visualizes operating system concepts that are otherwise taught only theoretically.”

📌 **Goes into:** `docs/viva/common_questions.md`
(because this is a _tooling / workflow_ viva-style question; you can also keep it as personal dev notes)

---

## Q: How can I view README / Markdown files in VS Code exactly as they appear on GitHub?

**A:**
By using VS Code’s **Markdown Preview** along with a **GitHub-flavored Markdown extension**, README files can be rendered almost exactly as they appear on GitHub.

---

### 1️⃣ Built-in Markdown Preview (MANDATORY)

VS Code already has this.

#### How to use:

- Open any `.md` file
- Press:

  ```
  Ctrl + Shift + V
  ```

  **OR**

- Right-click → **Open Preview**

This renders Markdown visually.

---

## Git & Version Control – Setup Issues (Viva Notes)

## Q: What issues did you face while setting up Git in Linux (WSL)?

**A:**  
While setting up Git in Linux (WSL), Git could not create commits because the user identity (name and email) was not configured.

---

### Explanation

- Git requires `user.name` and `user.email` to attach author information to commits
- In WSL, Git configuration is separate from Windows Git
- Since Git was freshly installed in Linux, no identity was set

This resulted in the error:
Author identity unknown

---

### Solution

The issue was resolved by configuring Git globally:
git config --global user.name "Akhil Semwal"
git config --global user.email "akhil392semwal@gmail.com"

---

### One-line viva answer

> “Git requires user identity to create commits, which must be configured separately inside WSL.”

---

## Q: Why did Git ask for username and password while pushing to GitHub?

**A:**  
Git asked for authentication because pushing to a remote repository requires verification of the user’s identity.

---

### Explanation

- The repository uses HTTPS for remote access
- GitHub requires authentication for write operations
- The username requested is the GitHub username

---

### One-line viva answer

> “Git requires authentication to verify user identity before pushing to a remote repository.”

---

## Q: Why can’t GitHub password be used for Git push?

**A:**  
GitHub has disabled password-based authentication for Git operations over HTTPS for security reasons.

---

### Explanation

- Password authentication was removed in August 2021
- GitHub now requires Personal Access Tokens (PATs)
- PATs provide limited, revocable access

This improves security and prevents account compromise.

---

### One-line viva answer

> “GitHub does not allow password authentication; it requires Personal Access Tokens for HTTPS Git access.”

---

## Q: What is a Personal Access Token (PAT)?

**A:**  
A Personal Access Token is a secure token generated by GitHub that acts as a replacement for a password when using Git over HTTPS.

---

### Explanation

- PATs have limited scope (e.g., repository access only)
- They can be revoked at any time
- They are more secure than passwords

In this project, a PAT was used to authenticate Git push operations.

---

### One-line viva answer

> “A PAT is a secure token used instead of a password for GitHub authentication.”

---

## Q: Why was a `.env.local` file used to store the GitHub PAT?

**A:**  
The `.env.local` file is used to store sensitive environment variables so they are not hard-coded into source files.

---

### Explanation

- Credentials should never be committed directly into code
- `.env.local` allows secrets to be loaded at runtime
- This follows security best practices

The file is meant for **local use only**.

---

### One-line viva answer

> “`.env.local` is used to store sensitive credentials securely without hard-coding them.”

---

## Q: Should `.env.local` be committed to GitHub?

**A:**  
No, `.env.local` should **never** be committed to version control.

---

### Explanation

- It may contain sensitive data such as tokens or keys
- Committing it can expose credentials publicly
- Such files must be added to `.gitignore`

---

### Correct practice

`.gitignore` should contain:
.env
.env.local

---

### One-line viva answer

> “No, `.env.local` should not be committed because it may contain sensitive information.”

---

## Q: What happens if a Personal Access Token is accidentally exposed?

**A:**  
If a PAT is exposed, it must be revoked immediately from GitHub settings.

---

### Explanation

- Anyone with the token can access the repository
- GitHub allows instant revocation of tokens
- A new token can be generated with limited scope

---

### One-line viva answer

> “If a PAT is exposed, it should be revoked immediately and replaced with a new one.”

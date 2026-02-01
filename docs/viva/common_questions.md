# Common Viva Questions

- [Common Viva Questions](#common-viva-questions)
  - [Q: Is this project platform-dependent?](#q-is-this-project-platform-dependent)
    - [Explanation](#explanation)
    - [Design advantage](#design-advantage)
    - [One-line viva answer](#one-line-viva-answer)
  - [Q: Why is Qt chosen for GUI?](#q-why-is-qt-chosen-for-gui)
    - [Explanation](#explanation-1)
    - [Academic relevance](#academic-relevance)
    - [One-line viva answer](#one-line-viva-answer-1)
  - [Q: Can this project run on Windows?](#q-can-this-project-run-on-windows)
    - [Explanation](#explanation-2)
    - [Design benefit](#design-benefit)
    - [One-line viva answer](#one-line-viva-answer-2)
  - [Q: Is this a real-time system?](#q-is-this-a-real-time-system)
    - [Explanation](#explanation-3)
    - [Important distinction](#important-distinction)
    - [One-line viva answer](#one-line-viva-answer-3)
  - [Q: How is this project useful academically?](#q-how-is-this-project-useful-academically)
    - [Explanation](#explanation-4)
    - [Educational value](#educational-value)
    - [One-line viva answer](#one-line-viva-answer-4)
  - [Q: How can I view README / Markdown files in VS Code exactly as they appear on GitHub?](#q-how-can-i-view-readme--markdown-files-in-vs-code-exactly-as-they-appear-on-github)
    - [1️⃣ Built-in Markdown Preview (MANDATORY)](#1️⃣-built-in-markdown-preview-mandatory)
      - [How to use:](#how-to-use)
  - [Q: What issues did you face while setting up Git in Linux (WSL)?](#q-what-issues-did-you-face-while-setting-up-git-in-linux-wsl)
    - [Explanation](#explanation-5)
    - [Solution](#solution)
    - [One-line viva answer](#one-line-viva-answer-5)
  - [Q: Why did Git ask for username and password while pushing to GitHub?](#q-why-did-git-ask-for-username-and-password-while-pushing-to-github)
    - [Explanation](#explanation-6)
    - [One-line viva answer](#one-line-viva-answer-6)
  - [Q: Why can’t GitHub password be used for Git push?](#q-why-cant-github-password-be-used-for-git-push)
    - [Explanation](#explanation-7)
    - [One-line viva answer](#one-line-viva-answer-7)
  - [Q: What is a Personal Access Token (PAT)?](#q-what-is-a-personal-access-token-pat)
    - [Explanation](#explanation-8)
    - [One-line viva answer](#one-line-viva-answer-8)
  - [Q: Why was a `.env.local` file used to store the GitHub PAT?](#q-why-was-a-envlocal-file-used-to-store-the-github-pat)
    - [Explanation](#explanation-9)
    - [One-line viva answer](#one-line-viva-answer-9)
  - [Q: Should `.env.local` be committed to GitHub?](#q-should-envlocal-be-committed-to-github)
    - [Explanation](#explanation-10)
    - [Correct practice](#correct-practice)
    - [One-line viva answer](#one-line-viva-answer-10)
  - [Q: What happens if a Personal Access Token is accidentally exposed?](#q-what-happens-if-a-personal-access-token-is-accidentally-exposed)
    - [Explanation](#explanation-11)
    - [One-line viva answer](#one-line-viva-answer-11)
  - [Q: How did you work on the project from multiple systems?](#q-how-did-you-work-on-the-project-from-multiple-systems)
    - [Explanation](#explanation-12)
    - [One-line viva answer](#one-line-viva-answer-12)
  - [Q: Why was GitHub chosen instead of file transfer methods?](#q-why-was-github-chosen-instead-of-file-transfer-methods)
    - [Explanation](#explanation-13)
    - [One-line viva answer](#one-line-viva-answer-13)
  - [Q: How do you avoid conflicts when working from multiple systems?](#q-how-do-you-avoid-conflicts-when-working-from-multiple-systems)
    - [Explanation](#explanation-14)
    - [One-line viva answer](#one-line-viva-answer-14)
  - [Q: Is internet connectivity required at all times?](#q-is-internet-connectivity-required-at-all-times)
    - [Explanation](#explanation-15)
    - [One-line viva answer](#one-line-viva-answer-15)
  - [Q: How are sensitive files handled in this workflow?](#q-how-are-sensitive-files-handled-in-this-workflow)
    - [Explanation](#explanation-16)
    - [One-line viva answer](#one-line-viva-answer-16)
  - [Q: Why was Git asking for username and password on every `git push`?](#q-why-was-git-asking-for-username-and-password-on-every-git-push)
    - [Explanation](#explanation-17)
    - [One-line viva answer](#one-line-viva-answer-17)
  - [Q: Why did installing `git-credential-manager` fail on Kali Linux?](#q-why-did-installing-git-credential-manager-fail-on-kali-linux)
    - [Explanation](#explanation-18)
    - [One-line viva answer](#one-line-viva-answer-18)
  - [Q: How was the repeated authentication problem solved on Kali Linux?](#q-how-was-the-repeated-authentication-problem-solved-on-kali-linux)
    - [Explanation](#explanation-19)
    - [One-line viva answer](#one-line-viva-answer-19)
  - [Q: Why was credential caching chosen instead of storing credentials permanently?](#q-why-was-credential-caching-chosen-instead-of-storing-credentials-permanently)
    - [Explanation](#explanation-20)
    - [One-line viva answer](#one-line-viva-answer-20)
  - [Q: Does Git use `.env.local` for authentication?](#q-does-git-use-envlocal-for-authentication)
    - [Explanation](#explanation-21)
    - [One-line viva answer](#one-line-viva-answer-21)
  - [Q: What is the long-term recommended authentication method for GitHub?](#q-what-is-the-long-term-recommended-authentication-method-for-github)
    - [Explanation](#explanation-22)
    - [One-line viva answer](#one-line-viva-answer-22)
  - [Q: How did you organize and navigate large documentation files efficiently?](#q-how-did-you-organize-and-navigate-large-documentation-files-efficiently)
    - [Explanation](#explanation-23)
    - [One-line viva answer](#one-line-viva-answer-23)
  - [Q: How do you jump directly to a specific question without scrolling?](#q-how-do-you-jump-directly-to-a-specific-question-without-scrolling)
    - [Explanation](#explanation-24)
    - [One-line viva answer](#one-line-viva-answer-24)
  - [Q: What tool did you use to generate tables of contents?](#q-what-tool-did-you-use-to-generate-tables-of-contents)
    - [Explanation](#explanation-25)
    - [One-line viva answer](#one-line-viva-answer-25)
  - [Q: Why is a separate `docs/viva/README.md` file used?](#q-why-is-a-separate-docsvivareadmemd-file-used)
    - [Explanation](#explanation-26)
    - [One-line viva answer](#one-line-viva-answer-26)
  - [Q: Why is this approach better than a single long README file?](#q-why-is-this-approach-better-than-a-single-long-readme-file)
    - [Explanation](#explanation-27)
    - [One-line viva answer](#one-line-viva-answer-27)


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


## Q: How did you work on the project from multiple systems?

**A:**  
The project was developed using a GitHub-centric workflow, where GitHub acts as the single source of truth.

---

### Explanation

- The repository is hosted on GitHub
- The project is cloned on both home and college systems
- Changes are synchronized using Git commit and push operations
- Updates from other systems are fetched using Git pull

This allows seamless development from multiple locations.

---

### One-line viva answer

> “I used GitHub as the central repository and synchronized work using Git commits and pulls.”

---

## Q: Why was GitHub chosen instead of file transfer methods?

**A:**  
GitHub was chosen because it provides version control, change history, and conflict management.

---

### Explanation

- File transfer methods like USB or cloud drives can overwrite changes
- Git tracks every modification with commit history
- Mistakes can be reverted safely

This makes GitHub more reliable and professional.

---

### One-line viva answer

> “GitHub provides version control and is safer than manual file transfers.”

---

## Q: How do you avoid conflicts when working from multiple systems?

**A:**  
Conflicts are avoided by always pulling the latest changes before starting work and committing logical changes frequently.

---

### Explanation

- `git pull` ensures the local copy is up to date
- Small, meaningful commits reduce conflict chances
- Git automatically handles most merges

---

### One-line viva answer

> “I avoid conflicts by pulling before work and committing changes frequently.”

---

## Q: Is internet connectivity required at all times?

**A:**  
Internet connectivity is required only when pushing or pulling changes from GitHub.

---

### Explanation

- Coding and testing can be done offline
- Synchronization happens when internet is available
- This makes the workflow flexible in college environments

---

### One-line viva answer

> “Internet is required only for synchronization, not for development.”

---

## Q: How are sensitive files handled in this workflow?

**A:**  
Sensitive files are stored locally and excluded from version control using `.gitignore`.

---

### Explanation

- Files like `.env.local` contain sensitive data
- These files are ignored using `.gitignore`
- This prevents accidental exposure on GitHub

---

### One-line viva answer

> “Sensitive files are kept local and excluded from Git using `.gitignore`.”


## Q: Why was Git asking for username and password on every `git push`?

**A:**  
Git was asking for credentials repeatedly because HTTPS authentication was being used and **no credential helper was configured** to store authentication details.

---

### Explanation

- The repository remote uses HTTPS
- GitHub requires authentication for every push
- By default, Git does not remember credentials in a fresh Linux/WSL setup
- Therefore, Git prompted for username and token on every push

---

### One-line viva answer

> “Git prompted repeatedly because no credential helper was configured to cache credentials.”

---

## Q: Why did installing `git-credential-manager` fail on Kali Linux?

**A:**  
The installation failed because `git-credential-manager` is **not available in Kali Linux repositories**.

---

### Explanation

- Kali Linux is security-focused and has a limited package set
- Git Credential Manager is available on Ubuntu, not Kali
- Therefore, `apt install git-credential-manager` results in a package not found error

This is expected behavior and not a system issue.

---

### One-line viva answer

> “Git Credential Manager is not available in Kali repositories, so installation failed.”

---

## Q: How was the repeated authentication problem solved on Kali Linux?

**A:**  
The issue was solved by configuring Git’s **built-in credential cache**.

---

### Explanation

The following command was used:
git config --global credential.helper 'cache --timeout=28800'

- This stores credentials temporarily in memory
- The token does not need to be re-entered during the session
- Credentials are not written to disk, improving security

---

### One-line viva answer

> “The issue was fixed by enabling Git’s credential cache in memory.”

---

## Q: Why was credential caching chosen instead of storing credentials permanently?

**A:**  
Credential caching was chosen to avoid storing sensitive tokens in plain text on disk.

---

### Explanation

- Permanent storage saves tokens in a readable file
- Caching keeps credentials only in memory
- This is safer for personal and college environments

---

### One-line viva answer

> “Credential caching was used to avoid storing sensitive tokens on disk.”

---

## Q: Does Git use `.env.local` for authentication?

**A:**  
No, Git does **not** use `.env.local` for authentication.

---

### Explanation

- `.env.local` is meant for application environment variables
- Git authentication is handled by credential helpers
- Git ignores `.env.local` completely

Sensitive files like `.env.local` are excluded from version control using `.gitignore`.

---

### One-line viva answer

> “Git does not read `.env.local`; authentication is handled by credential helpers.”

---

## Q: What is the long-term recommended authentication method for GitHub?

**A:**  
The long-term recommended method is **SSH-based authentication**.

---

### Explanation

- SSH does not require passwords or tokens during push
- It is more secure and convenient
- It is widely used in industry

For this project, credential caching was sufficient and appropriate.

---

### One-line viva answer

> “SSH authentication is the long-term recommended method for GitHub access.”

## Q: How did you organize and navigate large documentation files efficiently?

**A:**  
The documentation was indexed using Markdown headings, a central index file, and auto-generated tables of contents.

---

### Explanation
- Each major topic is stored in a separate Markdown file
- Headings are used for every question
- GitHub automatically generates anchor links for headings
- A central `docs/viva/README.md` file acts as a navigation index

This avoids scrolling and allows direct access to specific questions.

---

### One-line viva answer
> “I used a central index, heading-based anchors, and tables of contents for fast navigation.”

---

## Q: How do you jump directly to a specific question without scrolling?

**A:**  
Direct navigation is achieved using GitHub anchor links and tables of contents.

---

### Explanation
- GitHub converts headings into clickable anchors
- Each question heading can be linked directly
- Tables of contents provide one-click navigation to questions

This works both in VS Code preview and on GitHub.

---

### One-line viva answer
> “Questions are accessed using heading anchors and table-of-contents links.”

---

## Q: What tool did you use to generate tables of contents?

**A:**  
The **Markdown All in One** extension in VS Code was used.

---

### Explanation
- The extension automatically generates a table of contents
- It updates links when headings change
- It prevents broken or incorrect anchors

This keeps documentation consistent as it grows.

---

### One-line viva answer
> “I used the Markdown All in One extension to generate and maintain tables of contents.”

---

## Q: Why is a separate `docs/viva/README.md` file used?

**A:**  
The file is used as a central index to navigate all viva documentation.

---

### Explanation
- It lists links to all topic-wise documentation files
- It provides quick access to frequently asked questions
- It avoids mixing navigation with actual content

---

### One-line viva answer
> “`docs/viva/README.md` acts as a central index for all viva notes.”

---

## Q: Why is this approach better than a single long README file?

**A:**  
A single long README becomes difficult to navigate and revise.

---

### Explanation
- Large files require excessive scrolling
- Indexed files allow topic-wise separation
- Navigation becomes faster and more structured

This approach improves usability during viva preparation.

---

### One-line viva answer
> “Indexed documentation is easier to navigate than a single long README.”

# OpenAI  SDK Hosted Tools:

##   Hosted Tools Kya Hote Hain?

**Hosted Tools** woh tools hain jo AI agents ke sath already ready-made integrated hote hain. Inka fayda yeh hota hai ke aapko naye code likhne
ki zarurat nahi hoti — bas `Agent()` ke andar `tools=[...]` me add karo, aur AI automatically samajh jaata hai ke kis tool ka use karna hai.

##   Hosted Tools Kaise Kaam Karte Hain?

Jab aap kisi AI agent ko Hosted Tools ke sath create karte ho, to wo ek **multi-tool assistant** ban jaata hai.

### Example Prompt:

> "Weather check karo aur mujhe batao kahan coffee shop best hai?"

AI is request ko samajh ke:

1. Pehle weather check karega (WebSearchTool se)
2. Phir coffee shop ke suggestions dega

Yeh sab tools ke zariye hota hai — bina aapko bataye ke kaunsa tool use hua.



##   List of All 7 Hosted Tools (Simple Explanation ke Sath)

### 1. **WebSearchTool** – "AI ka Google"

* **Kya karta hai?** AI ko live internet search karne ki power deta hai.
* **Kab use hota hai?** Jab kisi latest ya updated information ki zarurat ho.
* **Example:**

  > "Aaj Karachi ka weather kya hai?"



### 2. **FileSearchTool** – "AI ka File Reader"

* **Kya karta hai?** AI aapki di hui file (PDF, DOCX, TXT) mein se information dhoondh sakta hai.
* **Kab use hota hai?** Jab aapne koi file upload ki ho aur usi se question poocha ho.
* **Example:**

  > "Mere resume mein skills kya likhe hain?"

  

### 3. **ComputerTool** – "AI ka Mouse & Keyboard"

* **Kya karta hai?** AI aapke computer pe buttons click, file open, ya software chala sakta hai.
* **Kab use hota hai?** Jab AI ko GUI applications ke sath interact karna ho (remote desktop ya automation environment).
* **Example:**

  > "Excel file open karo: report.xlsx"



### 4. **CodeInterpreterTool** – "AI ka Calculator + Programmer"

* **Kya karta hai?** AI coding karta hai (mostly Python mein), aur uska result nikal ke deta hai.
* **Kab use hota hai?** Jab aapko kuch calculate karwana ho ya data manipulate karwana ho.
* **Example:**

  > "1 se 10 tak ke numbers ka average nikal ke do"



### 5. **HostedMCPTool** – "AI doosri apps ke tools use karta hai"

* **Kya karta hai?** AI aapki external applications ke APIs ko access kar ke data le ya bhej sakta hai.
* **Example:**

  > "CRM se user ka profile read karo"

  

### 6. **ImageGenerationTool** – "AI artist ban jaata hai"

* **Kya karta hai?** AI likhi hui description se image generate karta hai.
* **Example:**

  > "Ek ladki jo rocket par baithi hai aur haath mein laptop hai"



### 7. **LocalShellTool** – "AI terminal commands chalay"

* **Kya karta hai?** AI aapke system pe command line commands run kar sakta hai (agar allowed ho).
* **Example:**

  > "Ek folder banao desktop pe — naam ho MyProject"
  >
  > Command: `mkdir MyProject`



## ✅ Summary:

| Tool Name           | Kya karta hai (Summary)                            |
| ------------------- | -------------------------------------------------- |
| WebSearchTool       | Internet pe live search karta hai                  |
| FileSearchTool      | Uploaded files se data read karta hai              |
| ComputerTool        | Computer ke buttons/file open automation karta hai |
| CodeInterpreterTool | Python code run karke result deta hai              |
| HostedMCPTool       | External apps ke APIs use karta hai                |
| ImageGenerationTool | Tasveer banata hai likhi hui description se        |
| LocalShellTool      | System pe terminal command chalay                  |



##  Use Case Example:

* **Research karni ho?** → `WebSearchTool`
* **Resume/file ke answers chahiye?** → `FileSearchTool`
* **Image design chahiye?** → `ImageGenerationTool`
* **Coding + Calculation chahiye?** → `CodeInterpreterTool`
* **Desktop task automation?** → `ComputerTool`
* **Command line ka kaam?** → `LocalShellTool`
* **App integration chahiye?** → `HostedMCPTool`


Ab aap jab bhi agent banayein, bas zarurat ke tools `tools=[...]` mein include kar dein — AI samajh jaayega kaunsa tool kab use karna hai!





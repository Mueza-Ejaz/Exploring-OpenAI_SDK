# Conversations / Chat Threads:

run() method ek complete user turn represent karta hai:

Matlab:
Jab bhi user koi text input deta hai aur hum run() call karty hy, to SDK ka poora process (chahe 1 agent ho ya multiple agents + tools) ek logical
conversation turn kehlata hai.

Flow Example:
Suppose ye user turn hai:
User types: “Find the capital of France and translate it to Urdu.”

## SDK flow (internally):

User input
↓
Agent 1 → uses LLM → calls tool "search"
↓
Gets "Paris"
↓
Agent 1 → handoff to Agent 2
↓
Agent 2 → calls translation tool
↓
Final output = "پیرس"

Ye sab kuch internally ek hi run() method me hota hai — ek single logical turn kehlata hai.

## RunResultBase.to_input_list() Method:

 to_input_list() method pehle run ka poora sawal-jawab yaad rakhta hai,taake hum agla sawaal usi context ke sath poochh saken,jisme AI ko pehli baat bhi yaad rahe.
 
 - Hum to_input_list() se agent ko purani baat yaad dila kar naye sawal ka sahi jawab le sakte hain.hum manually bhi kar sakte hy conversation chat history
   sy lakin us me galti k zada chances hy.



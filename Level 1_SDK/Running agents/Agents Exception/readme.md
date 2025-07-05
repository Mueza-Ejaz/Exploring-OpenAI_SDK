# AgentsException (Base Class)
Kya hai?

 Ye base class hai — iska matlab jitni bhi SDK me exceptions hain, wo is class ko inherit karti hain.


Example:
 Agar koi bhi error SDK ke through aata hai, to AgentsException ki type ka ho sakta hai.


Use case:

 Hum global try-except me except AgentsException: likh kar saare SDK-related errors ko pakar sakty hy.

## 1- MaxTurnsExceeded
 Jab hum run() method ko kisi agent par call karty hy aur usme max_turns ka parameter set karty hy (e.g., 5 rounds), agar woh limit cross ho jaye to ye exception raise hoti hai.
          Example:
          
          run(agent, max_turns=5)  
          # agar agent 6th turn par chala gaya to ye exception



## 2- Model Behaviour Error
Kis wajah se?

 Jab model kuch unexpected output deta hai:

- Malformed JSON (JSON format galat ho).
- Koi tool call karne ki koshish jo exist hi nahi karta.


Example:

 Hamara model keh raha hai "tool": "non_existing_tool" → error aayegi.


## 3- UserError
Kis liye?

 Jab developer (user of SDK) koi galti karta hai. Yani hamara apna code SDK ka ghalat use kar raha ho.


Example:

Hum agent ko run karne ki koshish karty hy bina initialize kiye
Hum required input fields nahi dety.


UserError tab hota hai jab developer (user of SDK) SDK ka use galat tareeqay se karta hai — jaise method ghalat call karna, required input na dena, ya structure follow na karna.



## 5. InputGuardrailTripwireTriggered & OutputGuardrailTripwireTriggered
Guardrails kya hain?

 Guardrails kuch safety checks hote hain jo input ya output validate karte hain.


Ye exceptions kab aayengi?

 Jab:

- Hamara input koi unsafe ya disallowed text hai.
  
- Model ka output koi violation kare (jaise sensitive data, etc.)


Example:

 Agar guardrail set hai ke model profanity na bole — agar bole to OutputGuardrailTripwireTriggered raise ho jayega.
 

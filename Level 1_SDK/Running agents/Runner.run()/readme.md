# Runner :

Runner ek helper hai jo agent ko kaam deta hai aur us ka jawab laata hai.Agent khud se kuch nahi karega jab tak Runner usay kaam nahi dega.

## Three Methods of Runner:

## 1- Runner.run():
Runner.run(agent, prompt) ek asynchronous method hota hai jo Agent ko prompt deta hai aur background mein uska response generate
karwata hai. Kyunki ye async hota hai, is liye iske sath await lagana zaroori hota hai. Jab tak agent apna kaam complete nahi karta, 
hamara program rukta nahi — balkay dusra kaam karta rehta hai. Jab agent ka response tayar hota hai, to Runner.run() humein ek RunResult 
object return karta hai. 


## RunResult kya hota hai aur kya karta hai?

RunResult aik object hota hai jo hame Runner.run() ya Runner.run_sync() ke baad milta hai.Is object ke andar Agent ka final 
jawab, kaam ka tareeqa, aur useful extra info hoti hai. Isse tum sirf jawab nahi, balkay AI ke thinking steps bhi samajh sakte hai.

## RunResult kya karta hai?

final_output:
 ➤ Ye wo final jawab hota hai jo Agent ne hamary prompt ka diya.
 
 Example: "Sure! Here's a haiku about recursion..."


input:
 ➤ Jo prompt humny agent ko diya tha — wo yaad rehta hai.
 Example: "Write a haiku about recursion."


## Intermediate_steps:

 ➤ Agent ne agar kisi tool ka use kiya ho (jaise function ya calculator) to uska pura process hota hai hum dekh sakty hy k AI ne kaise socha aur kaise kaam kiya.

## 2- run_sync():

run_sync() ek method hai jo Runner class ka part hota hai.Ye method hamary Agent ko prompt deta hai aur seedha jawab laa ke deta hai, bina await ke.


## 3- Runner.run_streamed():

Ye ek asynchronous method hota hai — matlab background mein kaam karta hai aur hamey await lagana padta hai.ye kya karta hai? Ye 
hamare Agent ko prompt bhejta hai, aur uska jawab streaming mode mein le kar aata hai.

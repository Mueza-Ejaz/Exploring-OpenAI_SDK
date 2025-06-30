
"Dependency Injection ka matlab hai:

Ham apne code ko asaan aur saaf banate hain,
un cheezon ko alag se define kar ke
jo baar baar repeat hoti hain (jaise login check, DB connection, etc),
aur phir unhe Depends() ke zariye inject kar lete hain jahan zarurat ho."**


🧠 Socho Dependency Injection aise hai:
Tum kehti ho:

"Mujhe bas cake banana hai,
login check tum sambhalo!"

Yani tum sirf apna main kaam karti ho,
aur FastAPI extra kaam pehle se tayar kar ke inject kar deta hai.

"Dependency Injection = Repeat hone wala kaam alag likhna, aur zarurat pe use karna"

--------------------------------------------------------------------------------------------------

why use Dependency Injection: 

Tum kehti ho:
“Mujhe bas cake banana hai,
order check aur payment ka kaam koi aur karay!” ✅

Bas yahi Dependency Injection hai!
Har kaam ko alag kar ke,
jahan zarurat ho, inject kar do.


How it works :
Annotated = Aik tag lagana value ke sath — taake FastAPI ya Python ko extra instructions mil sakein.
(Yahan instruction ye hai: “is value ko Depends se inject karo!”)


FOR DEEP LEARNING:
LINK = https://github.com/panaversity/learn-agentic-ai/tree/main/04_daca_agent_native_dev/01_intro_fastapi/04_dependency_injection
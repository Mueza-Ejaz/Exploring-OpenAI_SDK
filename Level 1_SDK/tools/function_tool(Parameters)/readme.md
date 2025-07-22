#  @function_tool — OpenAI Agent SDK Tool Decorator:

## Simple Definition

`@function_tool` ek decorator hai jo kisi bhi Python function ko OpenAI Agent SDK ke compatible **tool** mein convert karta hai.


## Kya Ye Sirf Decorator Hai?

**Nahi!** Ye sirf decorator nahi balki:

* Function ko **wrap** karta hai (uske behavior ko modify karta hai).
* LLM ke liye **metadata/schema** generate karta hai.
* SDK ko batata hai ke **ye function ek tool hai** jo LLM use kar sakta hai.


## Syntax

```python
@function_tool(   #  Yeh decorator hai
    name_override="my_tool",
    description_override="Does X",
    use_docstring_info=True,
    docstring_style="google",
    hidden=False,
    manual_schema=None,
    tool_config=None
)
def my_function(...):
    ...
```


## Under the Hood

Jab aap `@function_tool` lagate ho, to:

* Function **register** hota hai as a tool.
* Function ka metadata:

  * Name
  * Description
  * Parameters
  * Return Type
  * Schema
  * Config
    ... sab kuch **LLM ke liye JSON schema** mein convert hota hai.

LLM is schema ko dekh kar function ko call karta hai:

```python
fetch_weather(city="Lahore")
```


## Example Visualization

```python
@function_tool(name_override="get_weather")
def fetch_weather(city: str) -> str:
    """Returns the weather of a given city."""
```

Backend conversion:

```json
{
  "name": "get_weather",
  "description": "Returns the weather of a given city.",
  "parameters": {
    "type": "object",
    "properties": {
      "city": {"type": "string"}
    },
    "required": ["city"]
  }
}
```


##  @function_tool Parameters:

### 1️ `name_override`

**Purpose:** Tool ka naam manually specify karta hai.

**Example:**

```python
@function_tool(name_override="weather_checker")
def get_weather(): ...
```

**Use Cases:**

* Jab multiple tools same kaam kar rahe ho (test versions etc.)
* Jab LLM ko cleaner ya specific naam chahiye ho


### 2️⃣ `description_override`

**Purpose:** Tool ke liye manually ek description specify karta hai.

**Example:**

```python
@function_tool(description_override="Fetch weather using external API.")
def get_weather(): ...
```

**Use Cases:**

* Jab docstring se alag ya detailed/simple description chahiye ho


### 3️⃣ `use_docstring_info`

**Purpose:** SDK ko batata hai ke docstring se parameter info nikaalni hai ya nahi.

**Default:** `True`

**Example:**

```python
@function_tool(use_docstring_info=False)
```

**Use Cases:**

* Jab manually schema ya parameter info specify karni ho


### 4️⃣ `docstring_style`

**Purpose:** SDK ko batata hai ke docstring kis style me likhi gayi hai.

**Accepted Styles:**

* `"google"`
* `"numpy"`
* `"sphinx"`

**Example:**

```python
@function_tool(docstring_style="google")
def get_city_info(city: str):
    """Get info about a city.

    Args:
        city (str): Name of the city
    """
```


### 5️⃣ `manual_schema`

**Purpose:** Apna custom JSON schema define karta hai jab SDK ka schema sahi na ho.

**Example:**

```python
@function_tool(manual_schema={
    "name": "add_custom",
    "description": "Add two numbers",
    "parameters": {
        "type": "object",
        "properties": {
            "x": {"type": "integer"},
            "y": {"type": "integer"}
        },
        "required": ["x", "y"]
    }
})
def add_custom(x: int, y: int) -> int:
    return x + y
```

**Use Cases:**

* Jab SDK automatic schema sahi nahi banata
* Jab advanced control chahiye


### 6️⃣ `hidden`

**Purpose:** LLM se tool ko chhupata hai

**Example:**

```python
@function_tool(hidden=True)
def get_secret_code():
    return "TOP-SECRET-123"
```

**LLM Behavior:**

* Tool LLM ke suggestion list me nahi aata
* Lekin developer manually LLM ko bol kar use karwa sakta hai:

```python
llm.run("Use the secret code tool", tools=[get_secret_code])
```


### 7️⃣ `tool_config`

**Purpose:** Tool ke execution behavior ko control karta hai

**Common Config Options:**

| Key                  | Meaning                           |
| -------------------- | --------------------------------- |
| `tool_choice`        | "required" (force use) / "auto"   |
| `parallel`           | `True` = run tools simultaneously |
| `stop_on_first_tool` | `True` = stop after first success |

**Example:**

```python
@function_tool(tool_config={"tool_choice": "required"})
def search_flight(...): ...
```

**Real Use Case:**

```python
agent = autogen.AssistantAgent(
    tools=[get_weather, get_news, get_currency_rate],
    tool_config={
        "parallel": True,
        "stop_on_first_tool": False
    }
)
```

## ✅ Summary

* `@function_tool` Python function ko LLM-compatible tool me convert karta hai
* LLM ke liye JSON schema create karta hai
* Parameters se tool ka behavior customize kar sakte ho
* `hidden` aur `tool_config` jaise options advanced control dete hain



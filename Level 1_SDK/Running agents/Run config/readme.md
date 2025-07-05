## Run config:

Agent ka behaviour ya workflow me changes karna ya define karna.

## Methods:

*run_config* = global settings object

*Model* :  sab agents ke liye model fix karta hai.

*Model_provider* :  konsi company ka LLM use hoga (default: OpenAI).

*model_settings* :  temperature/top_p override karta hai.

*Guardrails* :  input/output filtering.

*handoff_input_filter* :  agent handoff ke input modify karta hai.

*tracing_disabled* :  debug logging band kar deta hai.

*Trace_include_sensitive_data* :  tracing mein sensitive data shamil kare ya nahi.

*workflow_name* :  trace ko identify karne ka naam.

*Trace_metadata* :  extra tracing info add karta hai.

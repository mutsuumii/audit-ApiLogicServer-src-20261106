# Security audit: ApiLogicServer/ApiLogicServer-src

Date: 2026-11-06 | Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Found 3 issue(s): 3 high.

## Findings

### 1. [HIGH] Path traversal via unsanitized input

**CWE-22** | `api_logic_server_cli/prototypes/manager/samples/modernization/demo_eai_native/tests/features/steps/steps.py` line 89

File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

```
context.partner_msg = json.load(open(MESSAGES + "order_b2b.json"))
```

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.
---

### 2. [HIGH] Path traversal via unsanitized input

**CWE-22** | `api_logic_server_cli/prototypes/manager/samples/modernization/demo_eai_native/tests/features/steps/steps.py` line 101

File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

```
context.partner_msg = json.load(open(MESSAGES + "order_b2b.json"))
```

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.
---

### 3. [HIGH] Path traversal via unsanitized input

**CWE-22** | `api_logic_server_cli/prototypes/manager/samples/modernization/demo_eai_native/tests/features/steps/steps.py` line 163

File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

```
shape = json.load(open(MESSAGES + "order_shipping.json"))
```

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.
---

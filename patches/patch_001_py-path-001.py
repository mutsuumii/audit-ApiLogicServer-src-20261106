# Path traversal via unsanitized input
# CWE-22 | Severity: HIGH
# File: api_logic_server_cli/prototypes/manager/samples/modernization/demo_eai_native/tests/features/steps/steps.py line 89

**Risk:** File path built from user input. Attacker reads/writes arbitrary files using ../ sequences.

**Fix:** Use os.path.realpath() and verify result starts with the expected base directory.

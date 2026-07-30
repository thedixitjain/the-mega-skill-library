#!/usr/bin/env bash

# @file example-test.sh
# @brief This script demonstrates how to test a CLI tool for UX issues.
#        Adapt this template for your specific tool.
# @usage ./example-test.sh
# @author Alister Lewis-Bowen <alister@lewis-bowen.org>

set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Test counter
TESTS_RUN=0
TESTS_PASSED=0
TESTS_FAILED=0

# Function to print test results
print_result() {
    local test_name="$1"
    local result="$2"
    local details="${3:-}"

    TESTS_RUN=$((TESTS_RUN + 1))

    if [[ "$result" == "PASS" ]]; then
        echo -e "${GREEN}✓${NC} $test_name"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    elif [[ "$result" == "FAIL" ]]; then
        echo -e "${RED}✗${NC} $test_name"
        if [[ -n "$details" ]]; then
            echo -e "  ${YELLOW}Details:${NC} $details"
        fi
        TESTS_FAILED=$((TESTS_FAILED + 1))
    else
        echo -e "${BLUE}•${NC} $test_name"
    fi
}

# Function to run a command and capture output
run_test() {
    local description="$1"
    local command="$2"
    local expected_pattern="${3:-}"

    echo -e "\n${BLUE}Testing:${NC} $description"
    echo -e "${BLUE}Command:${NC} $command"

    # Run command and capture output and exit code
    set +e
    read -ra cmd_array <<< "$command"
    output=$("${cmd_array[@]}" 2>&1)
    exit_code=$?
    set -e

    echo -e "${BLUE}Exit code:${NC} $exit_code"
    echo -e "${BLUE}Output:${NC}"
    echo "$output" | head -20

    # Check against expected pattern if provided
    if [[ -n "$expected_pattern" ]]; then
        if echo "$output" | grep -q "$expected_pattern"; then
            print_result "$description" "PASS"
        else
            print_result "$description" "FAIL" "Expected pattern '$expected_pattern' not found"
        fi
    fi

    return $exit_code
}

# ==============================================================================
# Test Suite Configuration
# ==============================================================================

# Set your CLI command here
CLI_COMMAND="${CLI_COMMAND:-mytool}"

# Path to the CLI tool (if it needs to be sourced)
CLI_SOURCE="${CLI_SOURCE:-}"

echo "========================================================================"
echo "CLI UX Testing Suite"
echo "========================================================================"
echo "Command: $CLI_COMMAND"
echo "Time: $(date)"
echo "========================================================================"
echo ""

# Source the CLI if needed
if [[ -n "$CLI_SOURCE" ]]; then
    echo "Sourcing: $CLI_SOURCE"
    source "$CLI_SOURCE"
    echo ""
fi

# ==============================================================================
# Test 1: Help Discovery
# ==============================================================================

echo -e "\n${YELLOW}=== Test Group: Help Discovery ===${NC}\n"

run_test "Help flag --help" "$CLI_COMMAND --help" "Usage:"
run_test "Help flag -h" "$CLI_COMMAND -h" "Usage:"
run_test "Help command" "$CLI_COMMAND help" ""

# ==============================================================================
# Test 2: Version Information
# ==============================================================================

echo -e "\n${YELLOW}=== Test Group: Version Information ===${NC}\n"

run_test "Version flag --version" "$CLI_COMMAND --version" ""
run_test "Version flag -v" "$CLI_COMMAND -v" ""

# ==============================================================================
# Test 3: Error Handling
# ==============================================================================

echo -e "\n${YELLOW}=== Test Group: Error Handling ===${NC}\n"

run_test "No arguments" "$CLI_COMMAND" ""
run_test "Invalid command" "$CLI_COMMAND invalid_command_xyz" "Error:"
run_test "Invalid flag" "$CLI_COMMAND --invalid-flag-xyz" "Error:"
run_test "Missing required argument" "$CLI_COMMAND command" ""

# ==============================================================================
# Test 4: Basic Functionality
# ==============================================================================

echo -e "\n${YELLOW}=== Test Group: Basic Functionality ===${NC}\n"

# Add your specific command tests here
# Example:
# run_test "Info message" "$CLI_COMMAND info 'test'" "test"
# run_test "Warning message" "$CLI_COMMAND warn 'test'" "test"

# ==============================================================================
# Test 5: Interactive Features
# ==============================================================================

echo -e "\n${YELLOW}=== Test Group: Interactive Features ===${NC}\n"

# Note: Interactive features require special handling
echo "ℹ️  Interactive features require manual testing or expect/pexpect"

# ==============================================================================
# Test 6: Output Formats
# ==============================================================================

echo -e "\n${YELLOW}=== Test Group: Output Formats ===${NC}\n"

# Test different output formats if your tool supports them
# Example:
# run_test "JSON output" "$CLI_COMMAND list --format json" "{"
# run_test "YAML output" "$CLI_COMMAND list --format yaml" ""

# ==============================================================================
# Test 7: Performance
# ==============================================================================

echo -e "\n${YELLOW}=== Test Group: Performance ===${NC}\n"

# Test startup performance
start_time=$(date +%s%N)
$CLI_COMMAND --help > /dev/null 2>&1 || true
end_time=$(date +%s%N)
duration_ms=$(( (end_time - start_time) / 1000000 ))

echo "Help command response time: ${duration_ms}ms"
if [[ $duration_ms -lt 100 ]]; then
    print_result "Help response time (<100ms)" "PASS"
elif [[ $duration_ms -lt 500 ]]; then
    print_result "Help response time (<500ms)" "INFO" "${duration_ms}ms"
else
    print_result "Help response time" "FAIL" "${duration_ms}ms (too slow)"
fi

# ==============================================================================
# Summary
# ==============================================================================

echo ""
echo "========================================================================"
echo "Test Summary"
echo "========================================================================"
echo -e "Total tests:  $TESTS_RUN"
echo -e "${GREEN}Passed:${NC}       $TESTS_PASSED"
echo -e "${RED}Failed:${NC}       $TESTS_FAILED"
echo ""

if [[ $TESTS_FAILED -eq 0 ]]; then
    echo -e "${GREEN}All tests passed!${NC}"
    exit 0
else
    echo -e "${RED}Some tests failed${NC}"
    exit 1
fi
